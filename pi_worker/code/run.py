import gpiozero
import requests
import os, time

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
        time.sleep(10000000)
    else:
        print('Connection unavailable.')


if __name__ == "__main__":
    host = os.environ.get('DJANGO_HOST')
    port = os.environ.get('DJANGO_PORT')
    post_url = os.environ.get('POST_URL')
    wait_for_django_server(url='http://'+host+':'+port+post_url, timeout=20)
