import requests
import time

for i in range(5):
    try:
        response = requests.get(
            "https://api.themoviedb.org/3/movie/278",
            params={
                "api_key": "f0fae71cba04d7904d15347e4eb6d9d5"
            },
            timeout=15
        )

        print("Request", i + 1, "→", response.status_code)

    except Exception as e:
        print("Request", i + 1, "→ FAILED:", type(e).__name__, e)

    time.sleep(3)