# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class Review(db.Model):
    """ 리뷰 테이블 """
    __tablename__ = 'review'

    rv_idx = db.Column(db.Integer, nullable=False, primary_key=True) #일렬번호
    rv_pidx = db.Column(db.Integer) #부모일렬번호 - 답변일 때 부모일렬번호가 들어감
    mb_id = db.Column(db.Integer,  db.ForeignKey('member.id'), nullable=False) #회원아이디
    cp_idx = db.Column(db.Integer, db.ForeignKey('company.cp_idx'), nullable=False) #업체번호
    rv_star = db.Column(db.Integer) #별점
    rv_content = db.Column(db.Text, nullable=False) #글내용
    rv_regdate = db.Column(db.String(20), nullable=False) #등록일자
    rv_edtdate = db.Column(db.String(20)) #수정일자
    rv_ip = db.Column(db.String(20)) #아이피