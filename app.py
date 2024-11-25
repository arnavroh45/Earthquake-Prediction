# Import 
from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
from geopy.geocoders import Nominatim
loc = Nominatim(user_agent="Geopy Library")

# Flask app
app = Flask(__name__, template_folder='templates')

# Load model
model=pickle.load(open('modell.pkl','rb'))

# To str
def to_str(var):
     return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

@app.route('/')
def home():
    return render_template('/homepage.html')

@app.route('/error',methods=['POST','GET'])
def error():
    data4 = request.form['e']
    if(data4.startswith('sk-')):
        return render_template('/insert.html')
    else:
        return render_template('/error.html')


@app.route('/home', methods=['GET', 'POST'])
def homee():
    return render_template('/homepage.html')

@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('/success.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('/login.html')
    

@app.route('/prediction' , methods=['POST','GET'])
def prediction():
    data4 = request.form['d']
    getloc = loc.geocode(data4)
    if(getloc == None):
        return render_template('/error1.html')
    data1 = int(float(getloc.latitude))
    data2 = int(float(getloc.longitude))
    if(data1<8 or data1>38):
        print("invalid location")
    # data1 = int(float(request.form['a']))
    # data2 = int(float(request.form['b']))
    # data3 = int(float(request.form['c']))
    arr = np.array([[data1, data2]])
    output= int(float(model.predict(arr)[0][0]))

    if output<4:
        return render_template('/prediction.html',p=to_str(output), q=' No ')
    elif output>=4 & output<6:
        return render_template('/prediction.html',p=to_str(output), q= ' Low ')
    elif output>=6 & output<8:
        return render_template('/prediction.html',p=to_str(output), q=' Moderate ')
    elif output>=8 & output<9:
        return render_template('/prediction.html',p=to_str(output), q=' High ')
    elif output>=9:
        return render_template('/prediction.html',p=to_str(output), q=' Very High ')
    else :
        return render_template('/prediction.html',p=' N.A.', q= ' Undefined ')



if __name__ == "__main__":
    app.run(debug=True)