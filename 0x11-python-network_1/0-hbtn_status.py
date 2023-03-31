#!/usr/bin/python3
"""Resource Fetching function"""
import urllib.request


def main():
    """ fetches https://alx-intranet.hbtn.io/status """
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as read_url:
        url = read_url.read()
        sp = ' '
        utf = str(url).rsplit("'")[1]
        print(f"Body response:")
        print(f"{sp*4}- type: {type(url)}")
        print(f"{sp*4}- content: {url}")
        print(f"{sp*4}- utf8 content: {utf}")


if __name__ == "__main__":
    main()
