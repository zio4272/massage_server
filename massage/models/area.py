# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class Area(db.Model):
    """ 지역 테이블 """
    __tablename__ = 'area'

    ar_idx = db.Column(db.Integer, nullable=False, primary_key=True)
    ar_area = db.Column(db.String(4), nullable=False) #지역 - 서울,경기,부산,대구 ...
    ar_title = db.Column(db.String(60), nullable=False) #상세지역명 - 경포대,강릉,정동진 ...
    ar_step = db.Column(db.Integer) #노출순서
    ar_regdate = db.Column(db.String(20), nullable=False) #등록일자
    ar_edtdate = db.Column(db.String(20), nullable=False) #수정일자
    ar_ip = db.Column(db.String(20), nullable=False) #아이피

    company = db.relationship('Company', backref='area', lazy=True)