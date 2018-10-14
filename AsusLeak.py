import argparse
import requests
import re

def ExtractDHCP(ip):
	url='http://{}/Main_Login.asp'.format(ip)
	r = requests.get(url)
	html = str(r.content)
	result = re.search('var dhcpLeaseInfo = (.*)var hostName = "";', html)
	devices = result.group(1)
	lenght = len(devices.split("],"))
	for x in range(lenght):	
		device = devices.split("],")[x]
		device = device.replace("[","")
		device = device.replace('\\',"")
		device = device.replace('\'',"")
		device = device.replace(',',"")
		device = device.replace(']',"")
		device = device.replace(';n',"")
		print(device)
def ExtractTime(ip):
	url='http://{}/update_clients.asp'.format(ip)
	r = requests.get(url)
	html = str(r.content)
	result = re.search("current_time:(.*)',", html)
	time = result.group(1)
	time = time.replace("\\","")
	time = time.replace("'","")
	print(time)
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='AsusWRT DHCP extract')
	parser.add_argument('-ip', action ='store', dest='ip', help="IP of router",default=max)
	results = parser.parse_args()
	ExtractDHCP(results.ip)
	ExtractTime(results.ip)