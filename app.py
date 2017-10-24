from __future__ import division
from flask import Flask, render_template, request, jsonify
from final_pipeline import Process_Result

app = Flask(__name__)
data_model = Process_Result('pipe_model.p') 

@app.route('/')
def index():
    equations = data_model.get_prior_equations()
    return render_template('index.html', equations = equations)


@app.route('/solve', methods=['POST'])
def solve():
    user_data = request.json
    data_model.create_pred_df(user_data)
    prediction = data_model.make_new_prediction()  
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
