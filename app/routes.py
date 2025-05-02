from app import app
from app.model_load import load_model
from app.transform_data import transform_data
from flask import request, render_template, jsonify
import pandas as pd
import pickle


try:
    model = load_model()
    model_status = "Waiting for predictions.."
except Exception as e:
    model = None
    model_status = f"Model failed to load with exception: {e}"

@app.route("/")
@app.route('/health')
def index():
    return (jsonify({'status':model_status}))

@app.route('/form', methods=["GET"])
def form():
    return render_template("index.html", prediction=None)

@app.route('/form_predict', methods = ['POST'])
def form_predict():
    if model is None:
        return render_template('index.html', prediction="Model failed to load")
    else:
        try:
            data = request.form.to_dict()
            transformed_data = transform_data(data)
            df = pd.DataFrame([transformed_data])
            prediction = round(model.predict(df)[0], 0)
            return render_template('index.html', prediction=prediction)
        except Exception as e:
            return render_template("index.html", prediction=f"Error: {e}")

@app.route('/predict', methods=["POST"])
def predict():
    if model is None:
        return(jsonify({'error':'Model not loaded'})), 500
    else:
        try:
            data = request.get_json()
            transformed_data = transform_data(data)
            df = pd.DataFrame([transformed_data])
            return(jsonify({'predicted_score':model.predict(df).tolist()}))
        except Exception as e:
            return(jsonify({'status': str(e)}))

@app.route('/test_predict')
def test_predict():
    if model is None:
        return(jsonify({'error':'Model not loaded'})), 500
    else:
        try:
            test_data = {"FG":{"5":12.0},"FGA":{"5":23.0},"FG%":{"5":0.522},
                         "3P":{"5":7},"3PA":{"5":15.0},"3P%":{"5":0.467},
                         "2P":{"5":5},"2PA":{"5":8.0},"2P%":{"5":0.625},
                         "eFG%":{"5":0.674},"FT":{"5":2},"FTA":{"5":2.0},
                         "TOV":{"5":4},"PF":{"5":1},"GmSc":{"5":23.2},
                         "designation_away":{"5":0},"designation_home":{"5":1},
                         "Opp_ATL":{"5":0},"Opp_BOS":{"5":0},"Opp_BRK":{"5":0},
                         "Opp_CHI":{"5":0},"Opp_CHO":{"5":0},"Opp_CLE":{"5":0},
                         "Opp_DAL":{"5":0},"Opp_DEN":{"5":0},"Opp_DET":{"5":0},
                         "Opp_HOU":{"5":0},"Opp_IND":{"5":0},"Opp_LAC":{"5":0},
                         "Opp_LAL":{"5":0},"Opp_MEM":{"5":0},"Opp_MIA":{"5":0},
                         "Opp_MIL":{"5":0},"Opp_MIN":{"5":0},"Opp_NOP":{"5":0},
                         "Opp_NYK":{"5":0},"Opp_OKC":{"5":0},"Opp_ORL":{"5":0},
                         "Opp_PHI":{"5":0},"Opp_PHO":{"5":0},"Opp_POR":{"5":0},
                         "Opp_SAC":{"5":0},"Opp_SAS":{"5":1},"Opp_TOR":{"5":0},
                         "Opp_UTA":{"5":0},"Opp_WAS":{"5":0}}
            df = pd.DataFrame.from_dict(test_data)
            return(jsonify({'predicted_score':model.predict(df).tolist()}))
        except Exception as e:
            return(jsonify({'status': str(e)}))

