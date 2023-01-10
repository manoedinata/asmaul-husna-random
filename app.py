from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config["JSON_AS_ASCII"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

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
    result_num = request.args.get("result_num")

    lowest_num = data[0]["nomor"] # Elemen pertama
    highest_num = data[-1]["nomor"] # Elemen terakhir
    randomChoice = []
    if result_num:
        randomNumbers = random.sample(range(lowest_num, highest_num+1), int(result_num))
        randomChoice = [data[x - 1] for x in randomNumbers]
    else:
        randomNumbers = random.randrange(lowest_num, highest_num+1)
        randomChoice.append(data[randomNumbers - 1])

    return jsonify(randomChoice)

if __name__ == "__main__":
    app.run()
