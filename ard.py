from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_data():
    with open("RTDA\energy_data.json", "r") as f:
        return json.load(f)

@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", energy_data=data)

@app.route("/data")
def get_data():
    return jsonify(load_data())

if __name__ == "__main__":
    app.run(debug=True)
