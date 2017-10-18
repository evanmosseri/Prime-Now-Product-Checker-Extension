import requests
from pyquery import PyQuery as pq
import re

zip = "78705"
amazon_url = "https://www.amazon.com/" \
             "AmazonBasics-6-Outlet-Surge-Protector-2-Pack/dp/B014EKQ5AA/" \
             "ref=sr_1_1_sspa?ie=UTF8&qid=1507868474&sr=8-1-spons&keywords=AmazonBasics+6-Outlet&psc=1"

# amazon_page = pq(amazon_url, headers={"User Agent": "Test for Chrome Extension"})
# asin = amazon_page("#ASIN").val()
asin = amazon_url.split("/")[5]

now_url = "https://primenow.amazon.com/gp/product/{}".format(asin)

print(pq(now_url, headers={
    # "User Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive",
    "DNT": "1",
    "Referer": "https://primenow.amazon.com/onboard?ie=UTF8&sourceUrl=%2Fgp%2Fproduct%2FB014EKQ5AA",
    "User Agent": "Test for My Chrome Extension",
    "Cookie": 'x-wl-uid=1GAxMwb7R5EyYNhddaZsZQr6ml/9l/ufnqcFzfRR2Ws2/wl5g9FOV7ZaJLEm9tmxn2t0EA3ceO6U=; session-token="G/q9KKFbFt7QMMoE5BjcsutDlsdv+UPncK4lzbM+khHFRpUseLO85JWZUI8UDRarXAG2VHyCBefOQEY7Tr0wEVizltPkCO0hPvae35Se1ey+bDwHVMFD57+kDyTahZWe34PViBaFj34ocowNKlPQIbKomIWCV/fq/QoVtbFkeMGkqxBSt/ODHY5b5gGfvI2wTuYvkfz5a8HtzIJ3Vh2Nhw=="; csm-hit=s-V84G0Q9279C2JVXPBRZA|1507869674570; ubid-main=131-6082162-4644366; session-id-time=2082758401l; session-id=130-1946093-7801858',
    "Host": "primenow.amazon.com"
}).text())
# print(requests.get("").text())