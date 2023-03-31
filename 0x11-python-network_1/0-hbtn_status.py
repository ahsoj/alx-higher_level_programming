#!/usr/bin/python3
"""
    Resource Fetching function
"""
import urllib.request


def main():
    """
        fetches https://alx-intranet.hbtn.io/status
        rtype: str
    """
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as read_url:
        url = read_url.read()
        utf = str(url).rsplit("'")[1]
        print(f"Body response:")
        print(f"\t- type: {type(url)}")
        print(f"\t- content: {url}")
        print(f"\t- utf8 content: {utf}")


if __name__ == "__main__":
    main()
