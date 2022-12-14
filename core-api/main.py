#!/usr/bin/env python
import healthpy
import os
import re

from jose import jwt
from flask import Flask, jsonify, current_app, request
from flask_rq2 import RQ

app = Flask(__name__)
rq = RQ()

redis_url: str = os.getenv('REDIS_URL')
try:  
    jwt_secret: str = os.environ['JWT_SECRET']
except KeyError: 
    print('[error]: `JWT_SECRET` environment variable required')
    sys.exit(1)

# Had to change RQ_DEFAULT_URL to RQ_REDIS_URL following the proper docs from the flask_rq2 page 
# https://flask-rq2.readthedocs.io/en/latest/#rq-redis-url
app.config['RQ_REDIS_URL'] = redis_url
app.config['JWT_SECRET'] = jwt_secret

rq.init_app(app)

@app.route('/transaction', methods=['POST'])
def create_transaction():
    data = request.get_json()
    token: str = data.get('token')
    amount: int = int(data.get('amount'))
    currency: str = data.get('currency')

    if not token:
        return jsonify(error='Token is blank'), 422
    if not amount:
        return jsonify(error='Amount is blank'), 422
    if not currency:
        return jsonify(error='Currency is blank'), 422
    if not re.match(r'^[A-Z]{3}$', currency):
        return jsonify(error='Invalid currency code'), 422

    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET'], algorithms=['HS256'])
        print(payload)
    except jwt.JWTError as exc:
        return jsonify(error=str(exc)), 422
    else:
        if payload['enabled']:
            rq.get_queue().enqueue(
                '__main__.make_transaction',
                user_id=payload['user_id'],
                amount=amount,
                currency=currency,
            )
            return jsonify(
                user_id=payload['user_id'],
                amount=amount,
                currency=currency,
            )
        else:
            return jsonify(error='User not enabled for transactions'), 403


@app.route('/health')
def health():
    status = healthpy.pass_status  # replace with the aggregated status
    checks = {}  # replace with the computed checks
    return healthpy.response_body(status, checks=checks)
