import requests

print requests.get("http://localhost:5000/api/test").text
