import pickle
import numpy as np
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

model = pickle.load(open('logistic.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.json
        print(data)
        new_data = [list(data.values())]
        output = model.predict(new_data)[0]
        return jsonify(output)
    except KeyError as e:
        error_message = f"KeyError: Missing key '{e.args[0]}' in JSON data."
        return jsonify(error=error_message), 400
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return jsonify(error=error_message), 500


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        Women_Occupation = request.form['Women Occupation']
        Occupation = ['Farming / Semi-Skilled / Unskilled', 'White Collar', 'Teacher / Nurse / Writer / Technician / Skilled', 'Managerial / Business', 'Professional with Advanced Degree']
        Women_Occupation_temp = [0, 0, 0, 0, 0]
        
        for i in range(len(Occupation)):
            if Women_Occupation == Occupation[i]:
                Women_Occupation_temp[i] = 1

        Husband_Occupation = request.form['Husband Occupation']
        Husband_Occupation_temp = [0, 0, 0, 0, 0]
        
        for i in range(len(Occupation)):
            if Husband_Occupation == Occupation[i]:
                Husband_Occupation_temp[i] = 1

        Rate_Marriage = request.form['Rate Marriage']
        Rate = ['Very Poor', 'Poor', 'Fair', 'Good', 'Very Good']
        Rate_temp = []

        for i in range(len(Rate)):
            if Rate_Marriage == Rate[i]:
                Rate_temp.append(i + 1)

        Women_Age = float(request.form['Women Age'])
        Number_of_years = float(request.form['Number of years Marride'])
        Number_of_Children = int(request.form['Number of Children'])

        Religious = request.form['Religious']  
        religious_values = ['Not Religious', 'Somewhat Religious', 'Moderately Religious', 'Strongly Religious']
        religious_temp = []

        for i in range(len(religious_values)):
            if Religious == religious_values[i]:
                religious_temp.append(i + 1)

        Education = request.form['Education']
        Education_values = {"Grade School": 9, "High School": 12, 'Some College': 14, "College Graduate": 16, "Some Graduate School": 17, "Advanced Degree": 20}
        Education_temp = []
        
        if Education in Education_values:
            Education_temp.append(Education_values[Education])

        f = Women_Occupation_temp + Husband_Occupation_temp + Rate_temp + [Women_Age, Number_of_years, Number_of_Children] + religious_temp + Education_temp
        data = np.array([f])
        output = int(model.predict(data)[0])

        if output == 1:        
            return render_template('home.html', prediction_text="Women have Affair.")
        else:
            return render_template('home.html', prediction_text="Women don't have Affair.")
         
if __name__ == '__main__':
    app.run(debug=True)