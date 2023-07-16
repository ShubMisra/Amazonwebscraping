import requests
from bs4 import BeautifulSoup as bs

response = requests.get(
    "http://ipv4.webshare.io/",
    proxies={
        "http": "http://dcngnpve-rotate:0cs2obi8ncin@p.webshare.io:80/"
    }
)

proxies = [response.text.strip()]

url = "https://www.amazon.in/s?k=iphone&crid=2YTWUI4N4NN9N&sprefix=iphon%2Caps%2C327&ref=nb_sb_ss_ts-doa-p_4_5"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

r = requests.get(url, headers=headers)

soup = bs(r.text, 'html.parser')

# Find all span elements
span_elements = soup.find_all('span')

# Iterate over the span elements and print the class attribute
for element in span_elements:
    class_list = element.get('class')
    if class_list:
        for class_name in class_list:
            print(class_name)
