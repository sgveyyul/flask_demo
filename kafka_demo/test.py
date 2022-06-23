import requests
import json
from threading import Thread

from faker import Faker


NUM_THREADS=5

def send_message():
    for i in range(10000):
        print(i)
        fake = Faker()

        url = "http://localhost:8080/users"
        payload = {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "middlename": "Camins",
            "birthday": "1994-11-05",
            "address": "Iligan City"
        }
        headers = {
            "Content-Type" : "application/json",
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers)

if __name__=='__main__':
    for t in range(20):
        worker = Thread(target=send_message)
        worker.start()