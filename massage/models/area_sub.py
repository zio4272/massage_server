# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class AreaSub(db.Model):
    """ 지역 테이블 """
    __tablename__ = 'area_sub'

    as_idx = db.Column(db.Integer, nullable=False, primary_key=True)
    am_idx = db.Column(db.Integer, db.ForeignKey('area_main.am_idx'), nullable=False)
    as_area = db.Column(db.String(20), nullable=False) # 강남/역삼/서초
    as_step = db.Column(db.Integer) #노출순서
    as_regdate = db.Column(db.String(20), nullable=False) #등록일자
    as_edtdate = db.Column(db.String(20)) #수정일자
    as_ip = db.Column(db.String(20)) #아이피

    company = db.relationship('Company', backref='area_sub', lazy=True)

    def get_area_sub_object(self):
        area_sub = {
            'as_idx': self.as_idx,
            'am_idx': self.am_idx,
            'as_area': self.as_area,
            'as_step': self.as_step,
            'as_regdate': self.as_regdate,
            'as_edtdate': self.as_edtdate,
            'as_ip': self.as_ip
        }

        return area_sub