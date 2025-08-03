import time
import requests

def calc_time(func):
    def wrapper():
        times_init = time.time()
        func()
        times_fin = time.time()
        print(f"Time request duration: {times_fin - times_init}")
    return wrapper

@calc_time
def extchang_mon():
    link = "https://economia.awesomeapi.com.br/last/USD-BRL"
    req = requests.get(link)
    req = req.json()
    print(req['USDBRL']['bid'])
    

extchang_mon()