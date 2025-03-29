from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# API Route to Read Data from File
@app.route("/api", methods=["GET"])
def get_data():
    file_path = "data.json"
    
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return jsonify(data)
    
    return jsonify({"error": "File not found"}), 404

@app.route("/")
def home():
    return "Hello! This is the flask tutorial assignment\nGo to '/api' to view the result"


if __name__ == "__main__":
    app.run(debug=True)

