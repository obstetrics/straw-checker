import cloudscraper
import random
import string
from colorama import Fore, init

init(autoreset=True)

API_URL = "https://straw.page/power/exists?site={}"

def random_username(length=3):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def check_username(scraper, username):
    try:
        r = scraper.get(API_URL.format(username), timeout=10)
        r.raise_for_status()
        data = r.json()
        if data.get("valid") is True:
            print(f"{Fore.GREEN}[+] {username}")
            with open("valid.txt", "a") as f:
                f.write(username + "\n")
        elif data.get("valid") is False:
            print(f"{Fore.RED}[-] {username}")
        else:
            print(f"{Fore.YELLOW}[!] Unknown response for {username}: {data}")
    except Exception as e:
        print(f"{Fore.YELLOW}[!] Error checking {username}: {e}")

def main():
    scraper = cloudscraper.create_scraper()
    while True:
        username = random_username()
        check_username(scraper, username)

if __name__ == "__main__":
    main()
