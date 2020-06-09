import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/gp/product/B079QYYGF1?pf_rd_r=WYHYS2Z921JYBYWNVVV9&pf_rd_p=edaba0ee-c2fe-4124-9f5d-b31d6b1bfbee'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    soup2 = BeautifulSoup(soup.prettify(), 'html.parser')

    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:4])


    print(title.strip())
    print(converted_price)

    if converted_price < 199.0:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('<youremail>', '<yourpassword>')

    subject = 'Price went down!'
    body = 'Check the amazon link https://www.amazon.com/gp/product/B079QYYGF1?pf_rd_r=WYHYS2Z921JYBYWNVVV9&pf_rd_p=edaba0ee-c2fe-4124-9f5d-b31d6b1bfbee'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '<youremail>',
        '<youremail>',
        msg
    )

    print('Email has been sent')
    server.quit()


while(True):
    check_price()
    time.sleep(60)