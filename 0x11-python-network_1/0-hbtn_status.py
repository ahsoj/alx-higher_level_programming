#!/usr/bin/python3
"""Resource Fetching function"""
import urllib.request


def main():
    """ fetches https://alx-intranet.hbtn.io/status """
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as read_url:
        url = read_url.read() 
        utf = str(url).rsplit("'")[1]
        print(
        f"Body response:\n\t- type: {type(url)} \n\t- content: {url}\n\t- utf8 content: {utf}")


if __name__ == "__main__":
    main()
