# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class Event(db.Model):
    """ 이벤트 테이블 """
    __tablename__ = 'event'

    ev_idx = db.Column(db.Integer,nullable=False, primary_key=True) #일렬번호
    ev_type = db.Column(db.String(1), nullable=False) #이벤트타입 C:쿠폰, E:이벤트
    cp_idx = db.Column(db.Integer, db.ForeignKey('company.cp_idx'), nullable=False) #업체번호
    ev_title = db.Column(db.String(255), nullable=False) #이벤트제목
    ev_sdate = db.Column(db.String(20), nullable=False,) #시작일자
    ev_edate = db.Column(db.String(20), nullable=False,) #마감일자
    ev_pubdate = db.Column(db.String(20), nullable=False,) #당첨자발표날짜
    ev_summary = db.Column(db.Text, nullable=False,) #이벤트설명
    ev_regdate = db.Column(db.String(20), nullable=False) #등록일자
    ev_edtdate = db.Column(db.String(20)) #수정일자
    ev_ip = db.Column(db.String(20)) #아이피

    event_pub = db.relationship('EventPub', back_populates='event')