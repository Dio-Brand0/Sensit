import serial
import time
import requests
import json

firebase_url = 'https://sensit-8bd76.firebaseio.com'
#Connect to Serial Port for communication
ser = serial.Serial('COM5', 9600, timeout=0)
#Setup a loop to send Temperature values at fixed intervals
#in seconds
#print ser
print firebase_url
fixed_interval = 3
while 1:
	try:          
		string = ser.readline()
		#sensor_thermal = ser.readline()
    	#sensor_moisture = ser.readline()
    	#sensor_soil = ser.readline()
    		sensor_thermal = string[0:2]
    		sensor_moisture = string[3:5]
    		sensor_soil = string[6:8]

    	#current time and date
  		time_hhmmss = time.strftime('%H:%M:%S')
		date_mmddyyyy = time.strftime('%d/%m/%Y')
    
		print sensor_thermal + ',' + time_hhmmss + ',' + date_mmddyyyy
		#print time_hhmmss
		#print date_mmddyyyy
    	#insert record
    	#data = {'date':date_mmddyyyy,'time':time_hhmmss,'value':sensor_thermal}
		result = requests.post(firebase_url + '/'+ '/temperature.json', data=json.dumps({'date':date_mmddyyyy,'time':time_hhmmss,'value':sensor_thermal}))
		print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
		result = requests.post(firebase_url + '/'+ '/moisture.json', data=json.dumps({'date':date_mmddyyyy,'time':time_hhmmss,'value':sensor_moisture}))
		print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
		result = requests.post(firebase_url + '/'+ '/soil.json', data=json.dumps({'date':date_mmddyyyy,'time':time_hhmmss,'value':sensor_soil}))
		print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
		time.sleep(fixed_interval)
	except IOError:
		print('Error! Something went wrong.')
		time.sleep(fixed_interval)