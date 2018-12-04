from flask import Flask, render_template,url_for,request
from flask_bootstrap import Bootstrap
import os,pickle
from pprint import pprint

plomb=cooper=zinc="Empty"

"""f=open("model4.sav", 'rb')  
loaded_model = pickle.load(f)"""

app = Flask(__name__)
Bootstrap(app)

def predict(values):
    X=[]
    for value in values.items():
        X.append(value)
    X=[X]
    y_predict=loaded_model.predict(X)
    return y_predict[0][0],y_predict[0][1],y_predict[0][2]

@app.route("/",methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = "empty","empty","empty"#predict(request.form)
      return render_template("result.html",result = result)

if __name__ == "__main__":
    app.run(debug=True)