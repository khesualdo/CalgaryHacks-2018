import cymysql

dateTime = "hi"
loudness = 345
lat = 45
long = 34

def writeToDB(dateTime = None, loudness = None, lat = None, long = None):
	try:
		conn = cymysql.connect(host='108.167.140.23', user='nicolas_CeroBuks', passwd='5LO$3c_73=]B', db='nicolas_CeroBuks', charset='utf8')
		cur = conn.cursor()
	except:
		print("Connection to DB failed.")
		return;
	
	query = "INSERT INTO GUNSHOT VALUES ( NULL, \'" + str(dateTime) + "\', " + str(loudness) + ", " + str(lat) + ", " + str(long) + ");"
	try:
		cur.execute(query)
	except:
		print("Insert query execution failed.")
	 
writeToDB(dateTime, loudness, lat, long)