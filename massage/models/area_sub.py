# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class AreaSub(db.Model):
    """ 지역 테이블 """
    __tablename__ = 'area_sub'

    as_idx = db.Column(db.Integer, nullable=False, primary_key=True)
    am_idx = db.Column(db.Integer, db.ForeignKey('area_main.am_idx'), nullable=False)
    as_area = db.Column(db.String(4), nullable=False) #지역 - 서울,경기,부산,대구 ...
    as_title = db.Column(db.String(60), nullable=False) #상세지역명 - 경포대,강릉,정동진 ...
    as_step = db.Column(db.Integer) #노출순서
    as_regdate = db.Column(db.String(20), nullable=False) #등록일자
    as_edtdate = db.Column(db.String(20)) #수정일자
    as_ip = db.Column(db.String(20)) #아이피

    company = db.relationship('Company', backref='area_sub', lazy=True)