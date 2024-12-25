"""
Send a request to flask application
"""
import requests

url = "https://flaskapp-cr-v1-yerjarnciq-ue.a.run.app"

# Method 1
resp = requests.get(f"{url}/hello", verify=False)
print(resp.content.decode())

# Method 2
resp = requests.get(f"{url}/hello/Foo bar", verify=False)
print(resp.content.decode())

# Method 3
resp = requests.post(f"{url}/hello_body", data={"my_name": "Foo bar"}, verify=False)
print(resp.content.decode())