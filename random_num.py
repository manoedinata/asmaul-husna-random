import random
import json

with open("Asmaul_Husna.json", "r") as f:
    data = json.load(f)
    lowest_num = data[0]["nomor"] # Elemen pertama
    highest_num = data[-1]["nomor"] # Elemen terakhir

randomChoice = random.randrange(lowest_num, highest_num+1)

print(f"{data[randomChoice - 1]['arab']} - {data[randomChoice - 1]['latin']} ({randomChoice})")
