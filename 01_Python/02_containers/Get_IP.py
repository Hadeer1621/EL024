
# task Get your public IP   Get your location
import requests

#===============================================================================
ip_address = requests.get('https://api64.ipify.org?format=json').json()
# print(ip_address)
response = requests.get(f'http://ip-api.com/json/').json()
# print(response)
location_data = {
        "ip": ip_address,
        "city": response.get("city"),
         "region": response.get("region"),
        "country": response.get("country"),
       "countryCode":response.get("countryCode"),
        "regionName":response.get("regionName"),
        "timezone":response.get("timezone"),
        "org":response.get("org"),
       "isp":response.get("isp"),
 }
for key,value in location_data.items():
    print(key,':',value)

#======anther_soluation====================================================
'''
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
    
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data
print(get_location())

'''