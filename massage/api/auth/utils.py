# -*- coding:utf8 -*-
from functools import wraps
import jwt

from flask import current_app, g
from flask_restful import reqparse

from massage.models import Member

token_parser = reqparse.RequestParser()
token_parser.add_argument('X-Http-Token', type=str, location='headers', dest='token', required=True)

def encode_token(member):
    if not isinstance(member, Member):
        raise ValueError('arg1 is not instance of Member')

    return jwt.encode({'id': member.id, 'mb_id': member.mb_id,\
        'mb_pwd': member.mb_pwd}, current_app.config['JWT_SECRET'], algorithm=current_app.config['JWT_ALGORITHM']).decode("utf-8")

def decode_token(token):
    if token:
        try:
            decoded = jwt.decode(token, current_app.config['JWT_SECRET'],\
                algorithms=[current_app.config['JWT_ALGORITHM']])

            member = Member.query.filter_by(id=decoded['id'], mb_id=decoded['mb_id'],\
                mb_pwd=decoded['mb_pwd']).first()
            return member
        except jwt.exceptions.DecodeError:
            pass

    return None

def token_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        args = token_parser.parse_args()
        member = decode_token(args['token'])

        if member:

            g.member = member
            return func(*args, **kwargs)

        return {
            'code': 404,
            'message': '올바르지 않은 토큰입니다.'
        }, 404

    return decorator