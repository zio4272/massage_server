# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class Faq(db.Model):
    """ 자주 묻는 질문 테이블 """
    __tablename__ = 'faq'

    bo_idx = db.Column(db.Integer, nullable=False, primary_key=True)
    vl_num = db.Column(db.Integer) #역인덱스용 최초 -1부터 추가시 감산한다.
    bo_title = db.Column(db.String(255), nullable=False) #제목
    bo_content = db.Column(db.Text, nullable=False) #내용
    bo_step = db.Column(db.Integer) #노출순서 등록시 max+1이 되고 수정이 가능해야함
    bo_regdate = db.Column(db.String(20), nullable=False) #등록일자
    bo_edtdate = db.Column(db.String(20), nullable=False) #수정일자
    bo_ip = db.Column(db.String(20)) #아이피