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

    mycursor.execute("SELECT * FROM simulation_data")

    data = mycursor.fetchall()
    last_data = data[len(data) - 1]

    return render_template("index.html", full_data=data, last_data=last_data)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    # found in ../templates/

    mydb = mysql.connector.connect(
    host = "JaykumarPatel4802.mysql.pythonanywhere-services.com",
    user = "JaykumarPatel480",
    passwd = "MySQLDataBase",
    database = "JaykumarPatel480$Simulation",
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM simulation_data")

    data = mycursor.fetchall()
    last_data = data[len(data) - 1]

    return render_template("dashboard.html", full_data=data, last_data=last_data)

@app.route('/simulation', methods=['GET'])
def simulation():
    # found in ../templates/
    return render_template("simulation.html")




