# -*- coding:utf8 -*-
import jwt

from flask import current_app
from massage.models import Member

def encode_token(member):
    if not isinstance(member, Member):
        raise ValueError('arg1 is not instance of Member')

    return jwt.encode({'id': member.id, 'mb_id': member.mb_id,\
        'mb_pwd': member.mb_pwd}, current_app.config['JWT_SECRET'], algorithm=current_app.config['JWT_ALGORITHM']).decode("utf-8")

def decode_token(token):
    if token:
        decoded = jwt.decode(token, current_app.config['JWT_SECRET'],\
            algorithms=[current_app.config['JWT_ALGORITHM']])

        member = Member.query.filter_by(id=decoded['id'], mb_id=decoded['mb_id'],\
            mb_pwd=decoded['mb_pwd']).first()
        if member is None:
            raise ValueError('token is not valid')

        return member

    raise ValueError('token is not valid')