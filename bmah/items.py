from  datetime import datetime

from bmah import get_model
from flask import Blueprint, render_template, request


items = Blueprint('items', __name__)


@items.route("/")
def list():
    print("abc")
    token = request.args.get('page_token', None)
    if token:
        token = token.encode('utf-8')

    items_data, next_page_token = get_model().list(cursor=token)

    return render_template(
        "list.html",
        items=items_data,
        next_page_token=next_page_token)
