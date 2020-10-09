import httplib
import urllib
import time
#Written for python 2.7 
key = "7481QW0APO2BO2BU"  #API Key
def labexam():
        #Requested Data
        projectgroup = "L1-F-8"
        member = "A"
        email = "isaacleung@cmail.carleton.ca"
        params = urllib.urlencode({'field1': projectgroup,'field2': member, 'field3': email, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            #print requested data
            print(projectgroup)
            print(member)
            print(email)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
if __name__ == "__main__":
     labexam()
