import os
import requests
from bs4 import BeautifulSoup

url = "https://www.reg.uci.edu/perl/WebSoc?YearTerm=2025-92&ShowFinals=1&ShowComments=1&Dept=MATH&CourseNum=2B"
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

def count_open_sections():
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    rows = soup.select("tr")
    open_count = 0
    for row in rows:
        if row.find("td"):
            cells = row.select("td")
            if cells:
                status = cells[-1].get_text(strip=True)
                if status == "OPEN":
                    open_count += 1
    return open_count

def send_discord_message(message):
    if DISCORD_WEBHOOK_URL:
        data = {"content": message}
        requests.post(DISCORD_WEBHOOK_URL, json=data)
    print(message)

def main():
    open_count = count_open_sections()
    send_discord_message(f"🔍 Current OPEN Math 2B classes: {open_count}")

if __name__ == "__main__":
    main()
