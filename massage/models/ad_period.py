# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class AdPeriod(db.Model):
    """ 광고기한 테이블 """
    __tablename__ = 'ad_period'

    ap_idx = db.Column(db.Integer, nullable=False, primary_key=True)
    cp_idx = db.Column(db.Integer, db.ForeignKey('company.cp_idx'), nullable=False)
    mb_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    ap_type = db.Column(db.String(1), nullable=False, default='N') #광고타입 M:메인, N:일반
    ap_showdate = db.Column(db.String(20), nullable=False) #노출기한
    ap_regdate = db.Column(db.String(20), nullable=False) #등록일자
    ap_editdate = db.Column(db.String(20), nullable=False) #수정일자

