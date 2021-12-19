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

from flask import Flask, request, abort, jsonify
import json
from datetime import datetime
import time
from hashlib import blake2b
from google.cloud import bigquery
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file(
    'credentials/ecomm-app-123-bc2c03fdc940.json',
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

app = Flask(__name__)


@app.route('/store', methods=['GET'])
def getStoreInfo():
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    query_job = client.query(
    """
        SELECT
            store_id,
            store_name,
            address
        FROM `ecomm-app-123.store.info`
        WHERE created_date > '2021-12-13'
        ORDER BY created_date DESC
        LIMIT 10"""
    )

    results = query_job.result()

    for latest_store_info in results:
        store_id = str(latest_store_info['store_id'])
        store_name = str(latest_store_info['store_name'])
        address = str(latest_store_info['address'])
        return jsonify({
            'store_id': store_id,
            'store_name': store_name,
            'address': address
        }), 200



@app.route('/store', methods=['POST'])
def addStoreInfo():
    if not request.json or not 'store_name' in request.json or not 'address' in request.json:
        abort(405)

    store_name = request.json['store_name']
    address = request.json['address']
    created_date = datetime.today().strftime('%Y-%m-%d')

    # Hash store_id based on current time
    k = str(time.time()).encode('utf-8')
    h = blake2b(key=k, digest_size=16)
    store_id = h.hexdigest()

    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    query_job = client.query(
    """
        INSERT INTO `ecomm-app-123.store.info` (store_id, store_name, address, created_date)
        VALUES (%(store_id)s, %(store_name)s, %(address)s, %(created_date)s)
    """ % {
            'store_id': store_id,
            'store_name': store_name,
            'address': address,
            'created_date': created_date
        }
    )

    results = query_job.result()
    return 200


if __name__ == '__main__':
    app.run(debug=True)
else:
    application = app
