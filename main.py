import collections
import os
import sys
import requests
import re
import time
from linkify_it import LinkifyIt

def search_urls(text: str) -> list[str]:
    linkify = LinkifyIt(options={"fuzzy_link":False})
    matches = linkify.match(text)

    if not matches:
        return []

    return [m.url for m in matches]


def search_urls_directory(dir_name: str) -> set:
    result = set()
    Q = collections.deque()

    Q.append(dir_name)
    while Q:
        fname = Q.pop()
        if os.path.isdir(fname):
            for e in os.listdir(fname):
                Q.append(os.path.join(fname, e))
        else:
            try:
                with open(fname, encoding="utf-8") as f:
                    text = f.read()
                    urls = search_urls(text)
                    for e in urls:
                        result.add(e)
            except:
                pass

    return result


def Get_status_by_url(url: str) -> int:
    try:
        request = requests.get(url)
        result = request.status_code
        request.close()
        return result
    except:
        return -1

def search_and_filter_urls_directory(working_directory: str, filter_mode: str, status_code: str,detect_URLs_that_cannot_connect_to_the_server:bool,wait_time:int)->list:
    filter_modes = set(["allow", "deny"])

    if filter_mode not in filter_modes:
        raise ValueError("filter_mode is not in {}".format(filter_modes))

    urls = search_urls_directory(working_directory)

    detected_urls_with_status = []
    for url in urls:
        detected_urls_with_status.append(
            {"url": url, "status_code": Get_status_by_url(url)}
        )
        time.sleep(wait_time)
    
    filter_func=lambda a,b:not re.match(b,a) if filter_mode == "allow" else lambda a,b:re.match(b,a)

    detected_urls_with_status = [
        e for e in detected_urls_with_status 
        if (
            filter_func(str(e["status_code"]) ,status_code)
            if e["status_code"]!=-1
            else
            detect_URLs_that_cannot_connect_to_the_server==True
        )
    ]

    return detected_urls_with_status

def main(working_directory: str, filter_mode: str, status_code:str,detect_URLs_that_cannot_connect_to_the_server:bool,wait_time:int):
    detected_urls_with_status=search_and_filter_urls_directory(
        working_directory,
        filter_mode, 
        status_code,
        detect_URLs_that_cannot_connect_to_the_server,
        wait_time
    )
    
    if len(detected_urls_with_status) > 0:
        print("Did not pass. There are detected URLs.")
        for e in detected_urls_with_status:
            print("{},{}".format(e["url"], e["status_code"]))
        sys.exit(-1)
    else:
        print("Passed. No URLs detected.")
        sys.exit(0)


if __name__ == "__main__":
    main(
        os.getenv("working_directory"),
        os.getenv("filter_mode"),
        os.getenv("filter_status_code"),
        os.getenv("detect_URLs_that_cannot_connect_to_the_server"),
        os.getenv("wait_time"),
    )
