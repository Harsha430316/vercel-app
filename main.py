from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load marks data from JSON file
with open("q-vercel-python.json", "r") as file:
    marks_data = json.load(file)

# Convert list into a dictionary for faster lookup
marks_dict = {student["name"]: student["marks"] for student in marks_data}

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")  # Get names from query params
    print(names)
    marks = [marks_dict.get(name, None) for name in names]  # Get marks, return None if not found
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)