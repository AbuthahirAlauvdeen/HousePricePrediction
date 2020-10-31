from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("HousePredictPickle.pkl")

@app.route("/")
def Hello():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
       BHK_No = request.form["BHK_No"]
       BHK_NO = int(BHK_No)
       BHK_OR_RK = request.form["BHK_OR_RK"]
       BHK_OR_RK = int(BHK_OR_RK)
       Ready_To_Move = request.form["Ready_To_Move"]
       READY_TO_MOVE = int(Ready_To_Move)
       RERA_Approved = request.form["RERA_Approved"]
       RERA = int(RERA_Approved)
       Resale = request.form["Resale"]
       RESALE = int(Resale)
       Square_Feet = request.form["Square_Feet"]
       SQUARE_FT = float(Square_Feet)
       Under_Construction = request.form["Under_Construction"]
       UNDER_CONSTRUCTION = int(Under_Construction)
       Ad_Posted_By = request.form["Ad_Posted_By"]
       Posted_by_enc = int(Ad_Posted_By)
       price = model.predict([[BHK_NO,BHK_OR_RK,READY_TO_MOVE,RERA,RESALE,SQUARE_FT,UNDER_CONSTRUCTION,Posted_by_enc]])

       return render_template('index.html',
                               prediction_text="Price = {}".format(price))

if __name__ == "__main__":
   app.run()