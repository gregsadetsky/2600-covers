import re
from pathlib import Path

IMGS_DIR = Path("/Users/g/Desktop/recurse-2600-covers/1.imgs")
HTML_FILE_PATH = Path("/Users/g/Desktop/recurse-2600-covers/2.covers.html")

with open(HTML_FILE_PATH) as f:
    lines = f.readlines()


def slugify(st):
    return re.sub(r"\W+", "-", st).strip("-").lower()


PERIOD_TO_MONTH_IDX = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
    "spring": 3,
    "summer": 6,
    "autumn": 9,
    "winter": 12,
}

for line in lines:
    img_file_name = re.search(r"/([^/]+\?)", line).groups(0)[0]
    img_file_name = img_file_name[:-1]
    file_extension = Path(img_file_name).suffix
    res = re.search(r">([^<]+)</a></span>", line)
    cover_period_slug = slugify(res.groups(0)[0])

    res = re.match(r"([^-]+)-(\d{4}).*", cover_period_slug)
    period, year = res.groups()
    destination_name = f"{year}-{PERIOD_TO_MONTH_IDX[period]}{file_extension}"
    print(destination_name)

    IMGS_DIR.joinpath(img_file_name).rename(destination_name)
