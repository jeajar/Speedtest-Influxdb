#!/usr/bin/env python3
import speedtest
from influxdb import InfluxDBClient

host = "192.168.1.23"
database = "speedtest"
threads = None
client = InfluxDBClient(host=host, database=database)

s = speedtest.Speedtest()
s = speedtest.Speedtest()

s.get_best_server()
s.download(threads=threads)

s.upload(threads=threads)
s.results.share()

results_dict = s.results.dict()


download = results_dict['download']
upload = results_dict['upload']
ping = results_dict['ping']



data = f'speedtest,download={download} speedtest,upload={upload} speedtest,ping={ping} '

json_body = [
    {
        "measurement": "Speedtest",
        "fields": {
            "download": download
        }
    },
    {
        "measurement": "Speedtest",
        "fields": {
            "upload": upload
        }
    },
        {
        "measurement": "Speedtest",
        "fields": {
            "ping": ping
        }
    }
]
client.write_points(json_body)