import serial
import time
import requests
import json

firebase_url = 'https://sensit-8bd76.firebaseio.com'
#Connect to Serial Port for communication
ser = serial.Serial('dev/ttyacm0', 9600, timeout=0)
#Setup a loop to send Temperature values at fixed intervals
#in seconds
#print ser
print firebase_url
fixed_interval = 3
while 1:
	try:          
		sensor_thermal = ser.readline()
    	#sensor_moisture = ser.readline()
    	#sensor_soil = ser.readline()

    	#current time and date
  		time_hhmmss = time.strftime('%H:%M:%S')
		date_mmddyyyy = time.strftime('%d/%m/%Y')
    
		#print sensor_thermal + ',' + time_hhmmss + ',' + date_mmddyyyy
		print time_hhmmss
		print date_mmddyyyy
    	#insert record
    	#data = {'date':date_mmddyyyy,'time':time_hhmmss,'value':sensor_thermal}
		#result = requests.post(firebase_url + '/'+ '/temperature.json', data=json.dumps(data))
    
		#print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
		time.sleep(fixed_interval)
	except IOError:
		print('Error! Something went wrong.')
		time.sleep(fixed_interval)
