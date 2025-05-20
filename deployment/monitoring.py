"""Deployment monitoring placeholder."""

import requests

def check_health(url):
    try:
        r = requests.get(url)
        return r.status_code == 200
    except Exception:
        return False
