import requests
import smtplib
from bs4 import BeautifulSoup
import lxml

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

MY_EMAIL = "yeshacodes@gmail.com"
MY_PASSWORD = "yujjfkqvdfwdtnrr"
URL_PRODUCT = "https://www.amazon.in/RE-EQUIL-Murumuru-Silicon-free-Conditioner/dp" \
              "/B07GKKFG1H/ref=sr_1_14?crid=3UBOFDHMS6A5R&keywords=hair+conditioner&qid=1671438678&sprefix" \
              "=hair+cond%2Caps%2C260&sr=8-14"

def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="yeshavyas27@gmail.com",
                            msg=f"Subject:Price Drop Alert \n There is Price drop in {URL_PRODUCT} \n Thank you!")


response = requests.get(URL_PRODUCT, headers=header)
html_data = response.text
soup = BeautifulSoup(html_data, "lxml")
print(soup.prettify())

price_tag = soup.select_one(".a-span12 a-price span.a-offscreen")
try:
    price = int(price_tag.string[1:])

    if price < 400:
        send_email()
    else:
        print("No price drop")

except AttributeError:
    print("None is returned")