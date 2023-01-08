from flask import Flask, jsonify
import json
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config["JSON_AS_ASCII"] = False

def get_data():
    with open("Asmaul_Husna.json", "r") as f:
        data = json.load(f)
    return data

@app.route("/")
def home():
    data = get_data()

    return jsonify(data)

@app.route("/random")
def random_choice():
    data = get_data()

    lowest_num = data[0]["nomor"] # Elemen pertama
    highest_num = data[-1]["nomor"] # Elemen terakhir
    randomChoice = random.randrange(lowest_num, highest_num+1)

    return jsonify(data[randomChoice - 1])

if __name__ == "__main__":
    app.run()
