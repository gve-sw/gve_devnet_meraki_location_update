#!/usr/bin/env python3
""" Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import meraki
from flask import Flask, request, json
from pprint import pprint
from dotenv import load_dotenv
import os
import csv

# load all environment variables
load_dotenv()
API_KEY = os.getenv('API_KEY')

switch_locations = {} # this dictionary will include the switch serials as keys and their lat and lng coordinates as the value

# get the switches and their locations from the csv file
with open('locations.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        location = {
            "lat": row["lat"],
            "lng": row["lng"]
        }

        switch_locations[row["serial"]] = location

pprint(switch_locations)

app = Flask(__name__)

# define how web server will receive the webhook
@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        data = request.json
        pprint(data)

        if data["alertType"] == "switches came up":
            dashboard = meraki.DashboardAPI(API_KEY)

            serial = data["deviceSerial"]
            location = switch_locations[serial]
            lat = location["lat"]
            lng = location["lng"]

            dashboard.devices.updateDevice(serial, lat=lat, lng=lng)


    return 'This server is for receiving webhooks'




if __name__ == '__main__':
    app.run(debug=True)
