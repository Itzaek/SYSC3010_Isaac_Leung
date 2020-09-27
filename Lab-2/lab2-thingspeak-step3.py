import urllib.request
import requests
import threading
import json

import random


# Define a function that will post on server every 15 Seconds

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    val=random.randint(1,30)
    URl='https://api.thingspeak.com/update?api_key='
    KEY='BP28Z5P0BRGKHV8J'
    HEADER='&field1={}&field2={}'.format(val,val)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)

def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/1159992/fields/1.json?api_key='
    KEY='6VR4RPWV6ECDXXZP'
    HEADER='&results=2'
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)

    get_data=requests.get(NEW_URL).json()
    #print(get_data)
    channel_id=get_data['channel']['id']

    field_1=get_data['feeds']
    #print(field_1)

    t=[]
    for x in field_1:
        #print(x['field1'])
        t.append(x['field1'])

    print(t)

if __name__ == '__main__':
    #thingspeak_post()
    read_data_thingspeak()
