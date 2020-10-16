import os
import subprocess
import time


while 1:
    with open('log.txt', 'a+') as log:
        host = "8.8.8.8"
        result = subprocess.run(f"ping {host} -n 1 | findstr /I ttl", capture_output=True, shell=True, text=True)
        if result.returncode != 0:
            res = 'offline <=='
        if result.returncode == 0:
            res = 'online'
        log.write(time.strftime('%Y-%m-%d %H:%M.%S ') + res + '\n')
        time.sleep(1)