# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


def format_date(date):
    return date[6:] + '/' + date[4:6] + '/' + date[:4]

@app.route('/')
def hello():
    result = '<H1>US - Azralon</H1><br>'
    arq = open('us/Azralon.csv', 'r')
    items = arq.readlines()[::-1]
    arq.close()

    date = None
    for item in items:
        item_id, item_name, item_date = item.split(',')
        item_date = item_date.replace('\n', "")
        if item_date != date:
            date = item_date
            result += '<br>' + format_date(date) + '<br>'
        result += "<a href='https://www.wowhead.com/item=%s'>%s</a><br>" %(item_id, item_name)
    """Return a friendly HTTP greeting."""
    return result


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
