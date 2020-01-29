from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import numpy as np

app = Flask(__name__)


app.static_folder = 'static'
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    # found in ../templates/

    mydb = mysql.connector.connect(
    host = "JaykumarPatel4802.mysql.pythonanywhere-services.com",
    user = "JaykumarPatel480",
    passwd = "MySQLDataBase",
    database = "JaykumarPatel480$Simulation",
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT numStudents, avgTime FROM simulation_data")

    # label_data_series = mycursor.fetchall()
    # label_data_array = np.transpose(label_data_series, axis = 0);
    data = mycursor.fetchall()
    print(data)
    # mycursor.execute("SELECT numStudents FROM simulation_data")
    # value_data_series = mycursor.fetchall()
    # value_data_array = np.transpose(value_data_series, axis = 0);

    return render_template("index.html", data=data)
    # return render_template("index.html", label_data=label_data_array, value_data=value_data_array)
    # return render_template("index.html")

@app.route('/simulation', methods=['GET'])
def simulation():
    # found in ../templates/
    return render_template("simulation.html")