import requests
from bs4 import BeautifulSoup
import json

URL = "https://islam.nu.or.id/ubudiyah/99-asmaul-husna-dan-artinya-1T8jl"

req = requests.get(URL)
parse = BeautifulSoup(req.text, "html.parser")

table = parse.find("table")
data = []
for col in table.find_all("tr")[1:]:
    data.append({
        "nomor": int(col.select_one("td:nth-of-type(1)").text),
        "latin": col.select_one("td:nth-of-type(2)").text,
        "arab": col.select_one("td:nth-of-type(3)").text,
        "arti": col.select_one("td:nth-of-type(4)").text,
    })

with open("Asmaul_Husna.json", "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# print(json.dumps(data, indent=4, ensure_ascii=False))
