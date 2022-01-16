#!/usr/bin/env python3

"""Gets details of air quality from OpenWeather API"""

from datetime import datetime
from zoneinfo import ZoneInfo
import logging
import requests

import database
from wconf import API_key, coords


# set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s: %(levelname)s:\t%(funcName)s:\t%(message)s',
							  datefmt='%d/%m/%Y %H:%M:%S')
# logging to console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

# logging to file
fh = logging.FileHandler('air.log')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)


def fetch_data(coords=coords):
	"fetches air quality data for a given pair of lat and long coordinates"
	lat, lon = coords
	try:
		r = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_key}')
		logger.debug(f'http response: {r.status_code}')
	except Exception as e:
		logger.error(e)
		raise
	else:
		pass
	finally:
		return r.json()

def check_aq(aqi):
	"returns descriptor for given aqi value"
	aqdict = {1: 'Good', 2: 'Fair', 3: 'Moderate', 4: 'Poor', 5: 'Very Poor'}
	return aqdict.get(aqi)

def parse_timestamp(dt):
	"returns UTC timestamp as formatted date"
	tz = ZoneInfo('Europe/London')
	d = datetime.fromtimestamp(dt, tz=tz)
	date = d.strftime('%A %d %b %Y')
	time = d.strftime('%I.%M %p')
	return date, time

def save(dt, aqi, components):
	"saves the data to the local database"
	db = database.connect()
	database.create_table(db)
	database.add_record(db,
		(aqi,
		components["co"],
		components["no"],
		components["no2"],
		components["o3"],
		components["so2"],
		components["pm10"],
		components["pm2_5"],
		components["nh3"],
		dt))

def main():
	"fetches the latest air quality reading from openweather"
	logger.info("running")
	data = fetch_data()
	# logger.debug(f"{data=}")
	aqi = data['list'][0]['main']['aqi']
	dt = data['list'][0]['dt']
	aq = check_aq(aqi)
	components = data['list'][0]['components']
	date, time = parse_timestamp(dt)
	print(f'air quality at {time} on {date} is {aq.lower()}')
	save(dt, aqi, components)

if __name__ == '__main__':
	main()
