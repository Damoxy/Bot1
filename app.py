from flask import Flask, render_template, request, jsonify
from retrieve_tweet import download_user
import joblib
import pandas as pd
from analisis_data_profil import preprocess
app = Flask(__name__)

model = joblib.load('finalized_model_without.sav')

def prediction(df):
    skrip = preprocess(df)
    pred_proba=model.predict_proba(skrip)
    y_pred=model.predict(skrip)
    percentage=pred_proba[:,1]
    joins=' '.join(map(str, percentage))
    perc=float(joins)*100
    percent=(str(perc)+"%")
    print(y_pred)
    return percent

@app.route("/")
def index():
    return render_template('index.html')
 
@app.route("/check", methods=['POST','GET'])
def check():
    dl_user = request.form.get('chat_in')
    download = download_user(dl_user)
    df=pd.read_csv('result.csv')
    prediksi=prediction(df)
    return render_template('index.html',prediction=prediksi)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
    
