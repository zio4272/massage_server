# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class EventPub(db.Model):
    """ 이벤트당첨자 테이블 """
    __tablename__ = 'event_pub'

    ep_idx = db.Column(db.Integer,nullable=False, primary_key=True) #일렬번호
    cp_idx = db.Column(db.Integer, db.ForeignKey('company.cp_idx'), nullable=False) #업체번호
    ev_idx = db.Column(db.Integer, db.ForeignKey('event.ev_idx'), nullable=False) #이벤트번호
    mb_id = db.Column(db.Integer,  db.ForeignKey('member.id'), nullable=False) #회원아이디
    ep_regdate = db.Column(db.String(40), nullable=False,) #날짜

    company = db.relationship('Company', back_populates='event_pub')
    event = db.relationship('Event', back_populates='event_pub')