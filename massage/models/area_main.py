# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class AreaMain(db.Model):
    """ 지역 테이블 """
    __tablename__ = 'area_main'

    am_idx = db.Column(db.Integer, nullable=False, primary_key=True)
    am_area = db.Column(db.String(4), nullable=False) #지역 - 서울,경기,부산,대구 ...
    am_step = db.Column(db.Integer) #노출순서
    am_regdate = db.Column(db.String(20), nullable=False) #등록일자
    am_edtdate = db.Column(db.String(20)) #수정일자
    am_ip = db.Column(db.String(20)) #아이피

    company = db.relationship('Company', backref='area_main', lazy=True)
    company = db.relationship('AreaSub', back_populates='area_main')