from json import loads, dump
from datetime import datetime
import matplotlib.pyplot as plt
import logging
from urllib import request

logging.basicConfig(level=logging.INFO)

logging.info('start')


try:
    link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    f = request.urlopen(link)
    text = f.read()
    data = loads(text)
except:
    logging.error("link trubles")
    data = {"features": {"properties": {"amg": 0, "time": 0, "place": ''}}}


data = [el["properties"] for el in data["features"]]
data = [(el["mag"], el["place"],
         datetime.fromtimestamp(el["time"] // 1000).time().isoformat()) for el in data]

logging.info(data)

plt.figure(figsize=(15, 5))
plt.stem([el[2] for el in data], [el[0] for el in data])
plt.title("Землетрясения за последний час")
plt.xlabel("Время")
plt.ylabel("Магнитуда")

text_return = '\n' + ''.join([f"{el[2]},\t{el[0]},\t{el[1]}\n" for el in  data])
logging.info(text_return)
logging.info("Pres enter to see plot")
input()


plt.show()

logging.info(text_return)

logging.info('end')