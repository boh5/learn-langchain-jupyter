import requests


def main():
    url = "https://waimai.meituan.com/help/faq"

    page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"})

    t = page.text
    print(1)


if __name__ == "__main__":
    main()