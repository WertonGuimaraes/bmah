from  datetime import datetime

from bmah import get_model
from flask import Blueprint, render_template, request, redirect, url_for

from bmah.model_datastore import get_client
from constants import SERVERS

items = Blueprint('items', __name__)
menu = Blueprint('menu', __name__)


@items.route("/<server_name>")
def list(server_name):
    token = request.args.get('page_token', None)
    if token:
        token = token.encode('utf-8')

    items_data, next_page_token = get_model().list(server_name, cursor=token)

    return render_template(
        "list.html",
        server_name=server_name,
        items=items_data,
        next_page_token=next_page_token)


@items.route("/", methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        return redirect(url_for('.list', server_name=request.form['serverlist']))
    return render_template("menu.html", servers=SERVERS)



