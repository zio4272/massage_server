# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class Viewlog(db.Model):
    """ 업체열람로그 테이블 """
    __tablename__ = 'viewlog'

    vl_idx = db.Column(db.Integer, nullable=False, primary_key=True)
    vl_num = db.Column(db.Integer) #역인덱스용 최초 -1부터 추가시 감산한다.
    cp_idx = db.Column(db.Integer, db.ForeignKey('company.cp_idx'), nullable=False) #업체번호
    mb_id = db.Column(db.String(40), nullable=False) #회원아이디
    vl_regdate = db.Column(db.String(20), nullable=False) #등록일자
    vl_ip = db.Column(db.String(20)) #아이피