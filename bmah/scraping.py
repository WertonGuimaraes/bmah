# The configuration use "cloud scheduler".
# run every day (at 4 a.m. gmt) make a post on https://wow-black-market.appspot.com/getinfoday/

import requests
import lxml.html as lh
import datetime
import time

from bmah import get_model
from flask import Blueprint, render_template, request

from constants import SERVERS


def get_info(server_name, date):
    url = "https://www.tradeskillmaster.com/black-market?realm=" + server_name
    tries = 0
    items = []
    while True:
        if tries >= 50:
            print("waiting 1 mim...")
            time.sleep(60)
            tries = 0
        page = requests.get(url)
        tries += 1
        doc = lh.fromstring(page.content)
        items_xpath = doc.xpath('//tr/td/a')
        if len(doc.xpath('//div[@class="empty"]')) == 1:
            break
        if len(items_xpath) > 0:
            break

    for item in items_xpath:
        item_id = item.get("data-item")
        item_name = item.get("title")
        items.append({"item_id": item_id, "item_name": item_name, "date": date})

    return items


date = datetime.datetime.now().strftime("%Y%m%d")
get_info_day = Blueprint('getinfoday', __name__)


def save_on_database():
    for server_name in SERVERS:
        items = get_info(server_name, date)
        print(items)
        for item in items:
            print(server_name)
            get_model().create(server_name, item)


@get_info_day.route('/', methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        save_on_database()
    return render_template("post.html", action="Add", book={})
