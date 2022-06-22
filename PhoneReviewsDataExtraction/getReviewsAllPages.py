import json
import os
import time
import requests
import pandas as pd

headers = {
    "cookie": "EMAGVISITOR=a%3A1%3A%7Bs%3A7%3A%22user_id%22%3Bi%3A2122868777249922555%3B%7D; ltuid=1629216378.434-944b10beef358af092bd65d38d16d9dbbfe130d6; EMAGUUID=1629216378-31406412-89800.817; _pdr_internal=GA1.2.1319308104.1629216378; eab449=c; loginTooltipShown=1; sr=1536x824; vp=1536x664; delivery_locality_id=14385; site_version_11=not_mobile; web4_ga=GA1.1.1319308104.1629216378; gdpr_consent_type=1; token1=%225606a576d3034d6db7852fe34389def8a945b6324b97e52fd6b86f4e34fe510f%22; cart_summary=%7B%22t%22%3A1%2C%22b%22%3A0%2C%22p%22%3A0%2C%22bfc%22%3A0%2C%22line%22%3A%5B%5D%7D; eab510=b; _ga=GA1.1.1319308104.1629216378; _scid=0bac757a-0e94-4c2d-bd0a-b91e0dbdce3d; FPID=FPID2.2.pnnFyEYsG4A2qm5vei23uyQxn6vfyQCT7MVm5nFw%2BV4%3D.1629216378; _pin_unauth=dWlkPU5qYzBZV05tWW1RdE56aGpNUzAwTVRSaExXSmxNV0V0T1RFMk1EZGhOekprWldZNA; _hjid=970921cf-7ef9-4281-a0cd-b193f6f7ce97; listingDisplayId=2; eab527=b; _ga_JJCSV4C7C3=GS1.1.1636881937.2.0.1636881937.0; campaign_notifications={'283':1,'10968':1,'11039':1}; sr=1536x824; G_ENABLED_IDPS=google; sk_c_undefined=2; sk_t_undefined=on; sk_t_skin_crazy_sale_after_bf_2021=1; vp=1536x722; _gcl_au=1.1.1565555289.1636997344; listingPerPage=60; _hjSessionUser_278704=eyJpZCI6IjZkNDQxODRhLTExMWUtNWUzNC05OTk0LTY3NGRmYmIzMmY5NyIsImNyZWF0ZWQiOjE2MzcyMzQ1NjE2MzQsImV4aXN0aW5nIjp0cnVlfQ==; EMAGROSESSID=24e4dbf25185da827e079f861fe8054c; FPLC=sss5zzRwiEzX0GRWjvxX7hudV%2F%2FXDtewSJijNT29O6IwaMABwZ8pzR0l6cVXtkYSQAHEWSz8o%2FZyHXvdqw50V%2FTEM82Yl6x8Jly4rO3uEfsBRpRN6NB5rI60qADPAQ%3D%3D; _uetsid=efe258204abd11ec90db6b49f1267a3a; _uetvid=7f4c2ce0445811ecb1303969fefcaaf5; _pdr_view_id=1637575710-98464.443-872397916; web4_ga_JJCSV4C7C3=GS1.1.1637575903.36.0.1637576249.0",
    "authority": "www.emag.ro",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "dnt": "1",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "content-type": "application/x-www-form-urlencoded",
    "accept": "application/json, text/javascript",
    "x-request-source": "www",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "accept-language": "en-US,en;q=0.9,ro-RO;q=0.8,ro;q=0.7,ko;q=0.6"
}

def parse_url(url, p, pages):
    # p = nr pagini de review din querystring
    if pages < 0:
        return
    list = [] #creaza o noua lista pentru a aduna recenziile
    querystring = {'source_id': '7', 'token': '', 'page[offset]': f'{p}', 'page[limit]': '10', 'sort[created]': 'desc'}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    for item in data['reviews']['items']:
        phone_id = item['product']['part_number_key']
        phone_name = item['product']['name']
        review_score = item['rating']
        review_title = item['title']
        review_content = item['content']
        review = {
            "phone_id": phone_id,
            "phone_name": phone_name,
            "review_score": review_score,
            "review_title": review_title,
            "review_content": review_content,
        }
        list.append(review)
    df = pd.json_normalize(list)
    if os.path.exists('Reviews_13_01.csv'): #daca exista fisierul adauga datele noi
        df.to_csv('Reviews_13_01.csv', mode='a', header=False, index_label=False)
    else:
        df.to_csv('Reviews_13_01.csv')
    time.sleep(3)
    p += 10 #treci la urmatoarea pagina
    pages -= 10
    print('parse next review page-----')
    parse_url(url, p, pages)
    return

def get_pages(url):
    querystring = {'source_id': '7', 'token': '', 'page[offset]': '0',
                   'page[limit]': '10', 'sort[created]': 'desc'}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    pages = int((data['reviews']['count'] / 10)) * 10
    return pages

def parse_file():
    with open('Links.json') as f:
        urls = json.load(f)
        for url_row in urls:
            print('----- inside url: ', url_row['path'])
            url = url_row['path']
            pages = get_pages(url)
            p = 0
            print('reviews pages: ', pages)
            parse_url(url, p, pages)
            time.sleep(3)

parse_file()
