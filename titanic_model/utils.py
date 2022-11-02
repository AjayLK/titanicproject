import pickle
import json
import pandas as pd
import numpy as np
import config


class TitanicData():
    def __init__(self,Pclass,Gender,Age,SibSp,Parch,Fare,Embarked):
        self.Pclass = Pclass
        self.Gender = Gender
        self.Age = Age
        self.SibSp = SibSp
        self.Parch = Parch
        self.Fare = Fare
        self.Embarked = Embarked

    def load_file(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.titanic_model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)


    def get_predicted_survived(self):
        self.load_file()  # calling load_file method to get

        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.json_data['pclass_dict'][self.Pclass]
        array[1] = self.json_data['gender_dict'][self.Gender]
        array[2] = self.Age
        array[3] = self.SibSp
        array[4] = self.Parch
        array[5] = self.Fare
        array[6] = self.json_data['embarked_dict'][self.Embarked]

        print("Test Array -->\n",array)
        predicted_survived = self.titanic_model.predict([array])[0]
        return predicted_survived

if __name__ == "__main__":

    Pclass = 'pclass_1'
    Gender = 'male'
    Age = 50
    SibSp = 1
    Parch = 2
    Fare = 5
    Embarked = 'S'

    td = TitanicData(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)
    survived = td.get_predicted_survived()
    print()
    print(f"predicted diabetes disease patients {survived}")
    

