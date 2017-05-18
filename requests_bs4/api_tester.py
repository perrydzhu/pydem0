import time
import requests
from requests_toolbelt import MultipartEncoder


m = MultipartEncoder(
    fields={
        "pic1": ('jennifer.jpg', open('jennifer.jpg', 'rb'), 'image/jpeg'),
        "pic2": ('emma.jpeg', open('emma.jpeg', 'rb'), 'image/jpeg')
    }
)


for i in range(30):
    print("No. {0}".format(i))
    # r = requests.post("http://localhost:8000/match", data=m, headers={'Content-Type': m.content_type})
    r = requests.get("http://localhost:8000/list")
    print(r.text)
    time.sleep(1)
