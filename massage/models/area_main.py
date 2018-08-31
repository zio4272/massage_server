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
    area_sub = db.relationship('AreaSub', backref='area_main', lazy=True)

    def get_area_main_object(self, sub_object=False, company_object=False):
        area_main = {
            'am_idx': self.am_idx,
            'am_area': self.am_area,
            'am_step': self.am_step,
            'am_regdate': self.am_regdate,
            'am_edtdate': self.am_edtdate,
            'am_ip': self.am_ip
        }

        if sub_object:
            area_main['area_sub'] = []
            for sub in self.area_sub:
                area_main['area_sub'].append(sub.get_area_sub_object())
        
        if company_object:
            area_main['company'] = []
            for companys in self.company:
                area_main['company'].append(companys.get_company_object())

        return area_main