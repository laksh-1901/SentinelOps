import requests
import time


def check_website(url):
    try:
        start = time.perf_counter()

        response = requests.get(url, timeout=5)

        response_time = round((time.perf_counter() - start) * 1000, 2)

        return {
            "url": url,
            "status": "Healthy",
            "status_code": response.status_code,
            "response_time": response_time
        }

    except requests.exceptions.RequestException:

        return {
            "url": url,
            "status": "Down",
            "status_code": "-",
            "response_time": "-"
        }
