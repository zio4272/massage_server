# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class Favorite(db.Model):
    """ 찜 테이블 """
    __tablename__ = 'favorite'

    fv_idx = db.Column(db.Integer,nullable=False, primary_key=True) #일렬번호
    mb_id = db.Column(db.Integer,  db.ForeignKey('member.id'), nullable=False) #회원아이디
    cp_idx = db.Column(db.Integer, db.ForeignKey('company.cp_idx'), nullable=False) #업체번호
    fv_regdate = db.Column(db.String(20), nullable=False,) #등록일자
    fv_ip = db.Column(db.String(20)) #아이피