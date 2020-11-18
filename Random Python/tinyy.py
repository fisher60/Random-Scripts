import requests

api_url = "https://tinyy.io"


def get_short_url(url, vanity_code=None):
    payload = {"url": url}

    if vanity_code:
        payload["code"] = vanity_code

    resp = requests.post(api_url, json=payload, headers={"Content-Type": "application/json"}).json()

    return f"{api_url}/{resp['code']}"


# print(get_short_url("https://www.youtube.com/watch?v=A1UhABiAfVk&ab_channel=SilasLaspada"))
print(get_short_url("https://www.google.com/search?q=2020&oq=2020&aqs=chrome..69i57j35i39l2j0i131i433i457j0i131i433j69i60l3.580j1j4&sourceid=chrome&ie=UTF-8", vanity_code="Dumpster_Fire"))
