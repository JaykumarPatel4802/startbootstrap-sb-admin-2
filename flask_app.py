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

@app.route('/simulation', methods=['GET','POST'])
def simulation():
    # found in ../templates/
    if(request.method == "POST"):
        data = str(request.get_data())

        temp = data[data.find('totalStudents') + 15:]
        totalStudents = temp[:temp.find(',')]

        temp = data[data.find('studentsPerRoom') + 17:]
        studentsPerRoom = temp[:temp.find(',')]

        temp = data[data.find('numberOfRooms') + 15:]
        numberOfRooms = temp[:temp.find(',')]

        temp = data[data.find('averageTime') + 13:]
        averageTime = temp[:temp.find(',')]

        temp = data[data.find('maxTime') + 9:]
        maxTime = temp[:temp.find(',')]

        temp = data[data.find('minTime') + 9:]
        minTime = temp[:temp.find('}')]

        mydb = mysql.connector.connect(
        host = "JaykumarPatel4802.mysql.pythonanywhere-services.com",
        user = "JaykumarPatel480",
        passwd = "MySQLDataBase",
        database = "JaykumarPatel480$Simulation",
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO simulation_data (totalStudents, studentsPerRoom, numberOfRooms, averageTime, maxTime, minTime) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, (totalStudents, studentsPerRoom, numberOfRooms, averageTime, maxTime, minTime))
        mydb.commit()

        return str(totalStudents) + " " + str(studentsPerRoom) + " " + str(numberOfRooms) + " " + str(averageTime) + " " + str(maxTime) + " " + str(minTime)

    return render_template("simulation.html")




