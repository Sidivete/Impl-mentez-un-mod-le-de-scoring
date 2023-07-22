from flask import Flask, jsonify, request, render_template
import joblib
import pandas as pd
import numpy as np
import shap
import json
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import plotly.express as px
import plotly
import pickle
import os


app = Flask(__name__)

# load models, threshold, data and explainer
model = joblib.load('Models/best_model_XGBC.joblib')
best_thresh = joblib.load('Models/best_thresh_XGBC.joblib')
data = joblib.load('Models/X_test.pkl')
shap_values = joblib.load('Models/shap_values.pkl')
shap_values1 = joblib.load('Models/shap_values1.pkl')
columns = shap_values.feature_names



# compute mean of absolute values for shap values
vals = np.abs(shap_values1).mean(0)
# compute feature importance as a dataframe containing vals
feature_importance = pd.DataFrame(list(zip(columns, vals)),\
    columns=['col_name','feature_importance_vals'])
# Define top 10 features for customer details
top_10 = feature_importance.sort_values(by='feature_importance_vals', ascending=False)[0:10].col_name.tolist()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/predict/<int:Client_Id>")
def predict(Client_Id :int):
    # Customer index in the corresponding array
    data_idx = data.loc[data["SK_ID_CURR"]==int(Client_Id)].index[0]
    # Customer data based on customer index in final X_test array
    ID_to_predict = pd.DataFrame(data.iloc[data_idx,:]).T
    # on réalise la prédiction de ID_to_predict avec le modèle 
    prediction = sum((model.predict_proba(ID_to_predict)[:, 1]>best_thresh)*1)
    if prediction == 0:
        decision = "granted"
    else :
        decision = "not granted"
    prob_predict = float(model.predict_proba(ID_to_predict)[:, 1])
    # on renvoie la prédiction
    return json.dumps({"decision" : decision, "prediction" : int(prediction), "prob_predict": prob_predict, "ID_to_predict" : ID_to_predict.to_json(orient='columns')})

#provide data for shap features importance on selected customer's credit decision 
@app.route("/cust_vs_group/<int:Client_Id>")
def cust_vs_group(Client_Id: int):
    # utiliser idx pour former le graph via Flask et l'importer dans streamlit
    data_idx = data.loc[data["SK_ID_CURR"]==int(Client_Id)].index[0] #string ou pas
    # customer data based on customer index in final X_test array
    ID_to_predict = pd.DataFrame(data.iloc[data_idx,:]).T
    # on réalise la prédiction de ID_to_predict avec le modèle 
    prediction = sum((model.predict_proba(ID_to_predict)[:, 1]>best_thresh)*1)
    if prediction == 0:
        decision = "granted"
    else :
        decision = "not granted"
    # return json string
    return json.dumps({'decision' : decision, 'base_value': shap_values.base_values[data_idx], 'shap_values1_idx': shap_values1[data_idx, :].tolist(), \
    "ID_to_predict": ID_to_predict.to_json(orient='columns')})

@app.route("/load_top_10/", methods=['GET'])
def load_top_10():
    return json.dumps({"top_10" : top_10})

@app.route("/load_data/", methods=['GET'])
def load_data():
    return {"data" : pd.DataFrame(data[0:5]).to_json(orient='columns')} 

@app.route("/load_best_thresh/", methods=['GET'])
def load_best_thresh():
    return {"best_thresh" : best_thresh} 



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5600)