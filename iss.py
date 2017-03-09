import urllib.request
from urllib.request import urlopen
import json
import datetime


dict = {}

def load_info():
    dictf = {}
    try:
        response = urlopen("http://api.open-notify.org/iss-now.json").read().decode('utf8')
    except urllib.error.HTTPError:
        print("error!!")
    else:
        obj = json.loads(response)
        if obj['message'] == "success":
            dictf['timestamp'] = obj['timestamp']
            dictf['iss_position_lo'] = obj['iss_position']['longitude']
            dictf['iss_position_la'] = obj['iss_position']['latitude']
        return dictf

dict = load_info()
if dict:
    str_loca = dict['iss_position_la'] + "," + dict['iss_position_lo']
    datedata = datetime.datetime.fromtimestamp(int(dict['timestamp'])).strftime('%H:%M:%S-%d-%m-%Y')

    f = open("img/" + datedata + '.png','wb')
    f.write(urlopen("https://maps.googleapis.com/maps/api/staticmap?center=" + str_loca + "&zoom=3&size=640x640&maptype=satellite&markers=color:red|" + str_loca + "&key=AIzaSyCplk-b4aNxj3uK2kTv3dEP4DkbRoV_ZRM").read())
    f.close()
