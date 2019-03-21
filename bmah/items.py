from bmah import get_model
from flask import Blueprint, redirect, render_template, request, url_for


items = Blueprint('items', __name__)


# [START list]
@items.route("/")
def list():
    token = request.args.get('page_token', None)
    if token:
        token = token.encode('utf-8')

    books, next_page_token = get_model().list(cursor=token)

    print(books)

    return render_template(
        "list.html",
        books=books,
        next_page_token=next_page_token)
# [END list]