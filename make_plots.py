import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import pickle
from preprocessing import clean_df
from preprocessing import create_target
from preprocessing import create_feature_dataframe
from model import create_split
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler
from basis_expansions import NaturalCubicSpline
from sklearn.linear_model import HuberRegressor


def make_prediction(pipe, df_pred):
    """Function to create predictions using a provided model
    Inputs
    -------
    Pipe: object from model.py to make predictions
    df_pred: dataframe to be predicted

    Outputs
    -------
    Yearly energy usage in BTU
    """
    energy_prediction = pipe.predict(df_pred)
    energy_prediction = (energy_prediction)**2

    return energy_prediction

def plot_univariate_smooth(ax, x, y, x_lim=None, mask=None, smooth=True,
                           n_knots=6, bootstrap=False):
    """Draw a scatter plot of some (x, y) data, and
    optionally superimpose a cubic spline.
    Parameters
    ----------
    ax: A Matplotlib axis object to draw the plot on.

    x: A np.array or pd.Series object containing the data.

    y: A np.array or pd.Series object containing the y data.

    x_lim: A tuple contining limits for the x-axis of the plot.  If not
    supplied, this is computed as the minimum and maximum of x.

    mask: A boolean np.array or pd.Series containing a mask for the x and y
    data, if supplied only the unmasked data contributes to the plot.

    smooth: A boolean, draw the cubic spline or not?

    n_knots: The number of knots to use in the cubic spline.

    bootstrap: False or an integer.  The number of time to boostrap the data
    when drawing the spline.  If not False, draw one spline per bootstrap
    sample of the data.

    Returns:
    --------
    None
    """
    if isinstance(x, pd.Series):
        x = x.values
    if isinstance(y, pd.Series):
        y = y.values
    if mask is not None:
        if isinstance(mask, pd.Series):
            mask = mask.values
        x = x[mask]
        y = y[mask]
    if not x_lim:
        x_lim = (np.min(x), np.max(x))
    x, y = x.reshape(-1, 1), y.reshape(-1, 1)

    ax.scatter(x, y, color='grey', alpha=0.25, label="Data")
    if smooth:
        if bootstrap:
            for _ in range(bootstrap):
                x_boot, y_boot = resample(x, y)
                plot_smoother(ax, x_boot, y_boot, x_lim, n_knots,
                              alpha=0.5, color="lightblue", label=None)
        plot_smoother(ax, x, y, x_lim, n_knots, linewidth=3,
                      color="blue", label="Trend")

def make_natural_cubic_regression(n_knots):
    return Pipeline([
           ('standardizer', StandardScaler()),
           ('nat_cubic', NaturalCubicSpline(-2, 2, n_knots=n_knots)),
           ('regression', HuberRegressor())
    ])


def plot_smoother(ax, x, y, x_lim, n_knots, **kwargs):
    ncr =  make_natural_cubic_regression(n_knots)
    ncr.fit(x, y)
    t = np.linspace(x_lim[0], x_lim[1], num=250)
    y_smoothed = ncr.predict(t.reshape(-1, 1))
    ax.plot(t, y_smoothed, **kwargs)


def create_results_plot(energy_prediction, y_test):
    '''
    Creates a plot of predicted vs actual results

    Inputs
    --------
    pipe: pipe model from create_model
    X_test: feature dataframe of the hold out data
    y_test: target dataframe of the hold out data

    Outputs
    --------
    Creates a plot of predicted vs actual of the test data
    and stores it in the current working directort
    '''

    plt.xlim(0, 400000)
    plt.ylim(0, 400000)
    plt.gca().set_aspect('equal', adjustable='box')
    x = np.linspace(0, 400000)
    plt.plot(x, x, color='black')
    plt.scatter(y_test, energy_prediction, alpha=.5)
    plt.ylabel('Predicted Energy Useage')
    plt.xlabel('Reported Energy Usage')
    plt.rcParams["figure.figsize"] = [8, 8]
    plt.savefig('images/pred_vs_act.png')


def plot_one_univariate(ax, var_name, mask=None):
    '''
    Create a univariate plot including boostrap samples
    and stores it in the current working directory

    Inputs
    -------
    ax: figure to plot on
    var_name: variable to be plotted

    Outputs
    -------
    Univariate plot for selected variable
    '''

    fig, ax = plt.subplots(figsize=(12, 3))

    if mask is None:
        plot_univariate_smooth(ax,
                               X_test[var_name].values.reshape(-1, 1),
                               y_test, bootstrap=200)
    else:
        plot_univariate_smooth(ax,
                               X_test[var_name].values.reshape(-1, 1),
                               y_test, mask=mask, bootstrap=200)

    ax.set_title(var_name)
    plt.ylabel('Reported Energy Use')
    plt.xlabel(var_name)
    plt.savefig("images/" + str(var_name) + "_univariate.png")


def plot_residual(energy_prediction, y_test):
    '''
    Function to plot the residuals as a function of reported energy use
    Inputs
    -------
    energy_prediction: target values predicted by the model
    y_test: Reported energy values
    Outputs
    -------
    Plot of residuals
    '''

    residual = energy_prediction - y_test
    plt.scatter(energy_prediction, residual)
    plt.ylabel('Residual')
    plt.xlabel('Predicted Energy Usage')
    plt.minorticks_on()
    plt.grid(True)
    plt.savefig('images/residuals.png')

if __name__=="__main__":
    df = pd.read_csv("data/recs2009_public.csv")
    df = clean_df(df)
    y = create_target(df)
    X = create_feature_dataframe(df)
    X_train, X_test, y_train, y_test = create_split(X, y)
#    X_test = pd.read_csv("X_test.csv")
#    y_test = pd.read_csv("y_test.csv")
    with open('pipe_model.p', 'rb') as f:
        pipe = pickle.load(f)
    energy_prediction = make_prediction(pipe, X_test)
    create_results_plot(energy_prediction, y_test)
    fig, ax = plt.subplots()
    plot_one_univariate(ax, "TOTSQFT")
    fig, ax = plt.subplots()
    plot_one_univariate(ax, "ACROOMS")
    plot_residual(energy_prediction, y_test)
