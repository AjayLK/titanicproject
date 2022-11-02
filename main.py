

from flask import Flask, jsonify, render_template, request
from titanic_model.utils import TitanicData
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome")
    return render_template('index.html')

@app.route('/predict_survived',methods = ['GET','POST'])
def get_heart_disease():
    if request.method == 'GET':
        print('we are using get method')
    
        data = request.form
        print("Data-->",data)

        Pclass = request.args.get('Pclass')
        Gender = request.args.get('Gender')
        Age = eval(request.args.get('Age'))
        SibSp = eval(request.args.get('SibSp'))
        Parch = eval(request.args.get('Parch'))
        Fare = eval(request.args.get('Fare'))
        Embarked = request.args.get('Embarked')

        print('Pclass,Gender,Age,SibSp,Parch,Fare,Embarked',Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)

        td = TitanicData(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)
        survived = td.get_predicted_survived()
        if survived == 0:
            return render_template('index.html',prediction = 'The passenger did not survived.')
        else:
            return render_template('index.html',prediction = 'The passenger has survived and happily making his onward journey.')

    else: 
        print('we are using post method')
    
        data = request.form
        print("Data-->",data)

        Pclass = request.form.get('Pclass')
        Gender = request.form.get('Gender')
        Age = eval(request.form.get('Age'))
        SibSp = eval(request.form.get('SibSp'))
        Parch = eval(request.form.get('Parch'))
        Fare = eval(request.form.get('Fare'))
        Embarked = request.form.get('Embarked')

        print('Pclass,Gender,Age,SibSp,Parch,Fare,Embarked',Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)

        td = TitanicData(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)
        survived = td.get_predicted_survived()
        if survived == 0:
            return render_template('index.html',prediction = 'The passenger did not survived.')
        else:
            return render_template('index.html',prediction = 'The passenger has survived and happily making his onward journey.')

  

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug = True)