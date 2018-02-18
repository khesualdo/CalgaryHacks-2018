#!/<path-to>/python
# Get date from MQTT server

import cymysql
import paho.mqtt.client as mqtt
import json
import base64
import datetime
import TweetBot
import subprocess

def writeToDB(dateTime=None, loudness=None, geo_lat=None, geo_long=None):

	if dateTime is None:
		raise Exception('No date/time provided!')

	if loudness is None:
		raise Exception('No loudness provided!')

	if geo_lat is None:
		raise Exception('No lat provided!')

	if geo_long is None:
		raise Exception('No long provided!')

	# Accept lat as float or int
	if not isinstance(geo_lat, float):
		if not isinstance(geo_lat, int):
			raise Exception('Latitude should be a float or int')

	# Accept long as float or int
	if not isinstance(geo_long, float):
		if not isinstance(geo_long, int):
			raise Exception('Longitude should be a float or int')

	try:
		conn = cymysql.connect(
			host='108.167.140.23', 
		user='nicolas_CeroBuks', 
		passwd='5LO$3c_73=]B', 
		db='nicolas_CeroBuks', 
		charset='utf8')
		cur = conn.cursor()
	except:
		print("Connection to DB failed.")
		return
	
	query = "INSERT INTO GUNSHOT VALUES ( NULL, \'" +\
	 str(dateTime) + "\', " + str(loudness) + ", " +\
	  str(geo_lat) + ", " + str(geo_long) + ");"

	try:
		cur.execute(query)
	except:
		print("Insert query execution failed.")

APPEUI = "70B3D57EF00065F5"
APPID  = "app_733"
PSW    = 'ttn-account-v2.mt4eewK-lOs5bQyncG3Sx68ghj7WaH2-qF4eqjKC6nw'

#Call back functions 

# gives connection message
def on_connect(mqttc, mosq, obj,rc):
	print("Connected with result code: "+str(rc))
	# subscribe for all devices of user
	print("Subscribing")
	mqttc.subscribe('app_733/devices/arduino_uno_grove_shield/up/soundLevel')
	print("Done")

# gives message from device
def on_message(mqttc,obj,msg):
	x = json.loads(msg.payload)
	timestamp = datetime.datetime.now()
	loudness = str(x)
	print(str(timestamp) + " Sound Level: " + loudness)
	geo_lat = 51.08019000
	geo_long = -114.13051000
	writeToDB(timestamp, loudness, geo_lat, geo_long)
	tweetMessage = "LMFAO"
	subprocess.Popen('java -jar sms.jar',shell=True,stdout=subprocess.PIPE)
	# TweetBot.tweet(tweetMessage, geo_lat, geo_long)
	
def on_publish(mosq, obj, mid):
	print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
	print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc,obj,level,buf):
	print("message:" + str(buf))
	print("userdata:" + str(obj))
		
mqttc= mqtt.Client()

# Assign event callbacks
mqttc.on_connect=on_connect
mqttc.on_message=on_message

mqttc.username_pw_set(APPID, PSW)
mqttc.connect("us-west.thethings.network",1883,60)

# and listen to server
run = True
while run:
	mqttc.loop()