"""
Send a request to flask application
"""
import requests
import urllib3  
# or if this does not work with the previous import:
# from requests.packages import urllib3  

# Suppress only the single warning from urllib3.
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)
url = "https://flaskapp-cr-v2-1079705010275.us-east1.run.app"

# Method 1
resp = requests.get(f"{url}/hello", verify=False)
print(resp.content.decode())

# Method 2
resp = requests.get(f"{url}/hello/Foo bar", verify=False)
print(resp.content.decode())

# Method 3
resp = requests.post(f"{url}/hello_body", data={"my_name": "Foo bar"}, verify=False)
print(resp.content.decode())