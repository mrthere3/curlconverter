import requests

headers = {
    'x-msisdn': 'XXXXXXXXXXXXX',
    'user-agent': 'Mozilla Android6.1',
}

params = {
    'p': '5',
    'pub': 'testmovie',
    'tkn': '817263812',
}

response = requests.get('http://localhost:28139/vc/moviesmagic', params=params, headers=headers)
