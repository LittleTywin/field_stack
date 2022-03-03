import gpiozero
import requests
import os, time
from datetime import datetime
import random, pytz

def wait_for_django_server(url,timeout):
    tic = time.perf_counter()
    connection_established = False
    time.sleep(2)
    print(url)
    tries=0
    while time.perf_counter()-tic < timeout and not connection_established :
        time.sleep(0.5)
        tries+=1
        try:
            r = requests.get(url)
            
            if r.status_code == 200:
                connection_established = True
        except:
            pass
    if connection_established:
        print('Connection established!')
        print(f'tries={tries}')
    else:
        print('Connection unavailable.')

def get_data_point():
    timestamp = datetime.now(tz=pytz.timezone('Europe/Athens'))
    tamper = bool(random.getrandbits(1))
    burner = bool(random.getrandbits(1))
    tamperco=random.randint(24,71)
    burnerco=random.randint(24,71)
    temperature=random.randrange(24,71)
    humidity=random.randrange(24,71)
    data = {
        'timestamp':timestamp, 
        'tamper':tamper, 
        'burner':burner,
        'tamperco':tamperco,
        'burnerco':burnerco, 
        'temperature':temperature,
        'humidity':humidity,
    }
    return data    


def main():
    host = os.environ.get('DJANGO_HOST')
    port = os.environ.get('DJANGO_PORT')
    post_url = os.environ.get('POST_URL')
    wait_for_django_server(url='http://'+host+':'+port+post_url, timeout=20)
    url = 'http://20.20.0.101:8002/core/api/'
    while True:
        time.sleep(5)
        print('posting data')
        r = requests.post(url, get_data_point())
        


if __name__ == "__main__":
    main()
