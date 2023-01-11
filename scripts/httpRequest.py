# req: pip install requests
import requests

r = requests.get("https://www.youtube.com", stream=True)
# print(r.headers)
print("headers['Alt-Svc']: %s" % r.headers["Alt-Svc"])
