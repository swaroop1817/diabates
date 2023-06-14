from flask import Flask,jsonify,request,render_template
import sqlite3
import pickle

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        pregnancies = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        blood_pressure = int(request.form['blood-pressure'])
        skin_thickness = int(request.form['skin-thickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree = float(request.form['diabetes-pedigree'])
        age = int(request.form['age'])
        data = [pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree,age]
        print(data)
        with open('model.pickel','rb') as file:
            model = pickle.load(file)
        result = model.predict([data])
        print(result) 
        if result[0]==0:
            outcome='No Diabatic'
        else:
            outcome = 'Diabatic'
        print('data has been iserted')
        return jsonify({'message':outcome})        



    else:
        return render_template('predict.html')
    

@app.route('/patient', methods=['GET','POST'])    
def showpatient():
    conn=sqlite3.connect('patient.db')
    cur = conn.execute("select * from patientinfo")
    data = []
    for i in cur.fetchall():
        patient = {}
        patient['name']= i[0]
        patient['result'] = i[1]
        data.append(patient)
    return render_template('showpatient.html',data=data)

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)                     
