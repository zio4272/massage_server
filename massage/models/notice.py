# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class Notice(db.Model):
    """ 공지사항 테이블 """
    __tablename__ = 'notice'

    bo_idx = db.Column(db.Integer,nullable=False, primary_key=True)
    vl_num = db.Column(db.Integer) #역인덱스용 최초 -1부터 추가시 감산한다.
    bo_title = db.Column(db.String(255), nullable=False) #제목
    bo_content = db.Column(db.Text, nullable=False) #내용
    bo_notice = db.Column(db.String(1), nullable=False, default='0') #상단공지여부 기본값0, 0:일반, 1:상단
    bo_regdate = db.Column(db.String(20), nullable=False) #등록일자
    bo_edtdate = db.Column(db.String(20)) #수정일자
    bo_ip = db.Column(db.String(20))

    company = db.relationship('Company', backref='area', lazy=True)