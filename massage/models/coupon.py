# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class Coupon(db.Model):
    """ 쿠폰 테이블 """
    __tablename__ = 'coupon'

    cu_idx = db.Column(db.Integer, nullable=False, primary_key=True)
    mb_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    cu_num = db.Column(db.String(20)) #쿠폰번호
    cu_used = db.Column(db.String(1), nullable=False, default='0') #사용여부 0:미사용, 1:사용
    cu_edate = db.Column(db.String(20), nullable=False) #사용만기날짜
    cu_usedate = db.Column(db.String(20)) #사용날짜