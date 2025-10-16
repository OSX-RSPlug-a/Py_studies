import redis
import ssl
import os
import sys

host = '127.0.0.1'
port = 6379
pas = '098765'
# if you are using certificate to connect
#ca_cert = 'ssl/ca.crt' 

#ssl_context = ssl.create_default_context(cafile=ca_cert)


r = redis.Redis(
    host=host,
    port=port,
    password=pas,
    #ssl=True,
    #ssl_ca_cert=ssl_context,
    db=0
)

try:
    r.flushdb()
    print("FLUSHDB successufully ran")
except redis.RedisError as e:
    print(f"Redis error: {e}")