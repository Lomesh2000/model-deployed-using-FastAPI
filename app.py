from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class ModelInput(BaseModel):
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int

# model load
model = pickle.load(open('model.sav', 'rb'))

@app.post('/result')
def diabetes_pred(parameters: ModelInput):
    input_data = parameters.model_dump_json()
    input_dictionary = json.loads(input_data)
    
    pregnancies = input_dictionary['Pregnancies']
    glucose = input_dictionary['Glucose']
    blood_pressure = input_dictionary['BloodPressure']
    skin_thickness = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    diabetespedigreefunction = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    input_list = [pregnancies, glucose, blood_pressure, skin_thickness, 
                  insulin, bmi, diabetespedigreefunction, age]
    
    prediction = model.predict([input_list])

    if prediction[0] == 0:
        return 'Not Infected'
    else:
        return 'Infected'
