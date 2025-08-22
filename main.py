import requests

response = requests.get(
    'https://timeapi.io/api/TimeZone/zone?timeZone=Europe/Oslo')

data = response.json()

print("Timezone is: ", data["timeZone"])
