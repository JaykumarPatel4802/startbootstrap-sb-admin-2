from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # found in ../templates/
    return render_template("index.html")

@app.route('/simulation', methods=['GET'])
def simulation():
    # found in ../templates/
    return render_template("simulation.html")