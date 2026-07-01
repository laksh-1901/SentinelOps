import requests
import time


def check_website(url):
    try:
        start = time.time()

        response = requests.get(url, timeout=5)

        end = time.time()

        response_time = round((end - start) * 1000, 2)

        return {
            "status": "Healthy",
            "status_code": response.status_code,
            "response_time": response_time
        }

    except requests.exceptions.RequestException:
        return {
            "status": "Down",
            "status_code": "N/A",
            "response_time": "N/A"
        }
