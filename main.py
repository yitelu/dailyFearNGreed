from bs4 import BeautifulSoup
import requests
from datetime import datetime
import smtplib

#the reason for the fake header so that website won't think it's a bot that try to scrap the data.
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

#the request for the target URL and don't forget  to add the "header" in the end
response = requests.get("https://money.cnn.com/data/fear-and-greed/", headers=header)

#getting the response in text and turn it into html.parser/lxml.parser to be a "SOUP"
data = response.text
soup = BeautifulSoup(data, "html.parser")
#print(soup.prettify())

#soup select the class "feargreed" and "a" href the link that put everything in the list
all_index_elements = soup.select(".feargreed li")

current_index = ""

#split the get text and split text and test the last item
all_index = [index.get_text().split(" ") for index in all_index_elements]

for i in range(3, len(all_index[0]), 1):
    current_index += all_index[0][i]
    current_index += " "

#print(current_index)

#type in your own email and password, if you're using gmail make sure the security setting is updated
MY_EMAIL = "xxxx"
MY_PASSWORD = "xxxx"

today = datetime.now()

#put multiple email in a list
recipients = ["xxxxx@gmail.com", "xxxxx@gmail.com"]

#smtplib.SMTP_SSL("smtp.gmail.com", 465)
with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr= MY_EMAIL,
        to_addrs= recipients,
        msg=f"Subject:Today's Fear & Greed Index is {current_index}\n\n Today {today.now()} Based on the website https://money.cnn.com/data/fear-and-greed/ the Fear&Greed index is now {current_index}"
    )