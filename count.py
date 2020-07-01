import requests
import re
import datetime
import time

endpoint = "https://portal.rockgympro.com/portal/public/74083a89f418928244e5479ea18be366/occupancy"


def get_count():
    html = requests.get(endpoint).text
    regex = ",'ARC'.*'count' : (\d+),"

    found = re.search(regex, html, flags=re.DOTALL)

    if found:
        match = found.group(1)
        return match
    else:
        return "Not found"


def append_data(time, count):
    output_file = open("output.txt", "a")
    output_file.write(f"{time},{count}\n")
    output_file.close()


while(True):
    now = datetime.datetime.now()
    count = get_count()

    append_data(now, count)

    time.sleep(5 * 60)
