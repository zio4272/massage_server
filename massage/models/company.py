# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class Company(db.Model):
    """ 업체정보 테이블 """
    __tablename__ = 'company'

    cp_idx = db.Column(db.Integer, nullable=False, primary_key=True)
    mb_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    cp_sangho = db.Column(db.String(60), nullable=False)
    cp_always_time = db.Column(db.String(1), nullable=False, default=0) #24시간 0:NO , 1:YES
    cp_always_day = db.Column(db.String(1), nullable=False, default=0) #연중무휴 0:NO , 1:YES
    cp_otime = db.Column(db.String(20), nullable=False) #오픈시간
    cp_ctime = db.Column(db.String(20), nullable=False) #마감시간
    cp_h_0 = db.Column(db.String(1), nullable=False) #휴일(일)
    cp_h_1 = db.Column(db.String(1), nullable=False) #휴일(월)
    cp_h_2 = db.Column(db.String(1), nullable=False) #휴일(화)
    cp_h_3 = db.Column(db.String(1), nullable=False) #휴일(수)
    cp_h_4 = db.Column(db.String(1), nullable=False) #휴일(목)
    cp_h_5 = db.Column(db.String(1), nullable=False) #휴일(금)
    cp_h_6 = db.Column(db.String(1), nullable=False) #휴일(토)
    cp_price = db.Column(db.String(10), nullable=False) #가격
    cp_sale_price = db.Column(db.String(10)) #할인가격
    cp_phone = db.Column(db.String(20), nullable=False) #전화번호
    cp_vphone = db.Column(db.String(20), nullable=False) #가상번호
    cp_zipcode = db.Column(db.String(6), nullable=False) #우편번호
    cp_addr1 = db.Column(db.String(255), nullable=False) #주소
    cp_addr2 = db.Column(db.String(255), nullable=False) #상세주소
    cp_lat = db.Column(db.Numeric(15, 10), nullable=False, default=0)
    cp_long = db.Column(db.Numeric(15, 10), nullable=False, default=0)
    ar_idx = db.Column(db.Integer, db.ForeignKey('area.ar_idx'), nullable=False) #지역구분
    cp_star = db.Column(db.String(20)) #별점
    cp_fav = db.Column(db.Integer) #찜갯수
    cp_content = db.Column(db.Text, nullable=False) #가격/코스안내
    cp_open = db.Column(db.String(1), nullable=False, default=0) #노출여부 0:NO , 1:YES
    cp_regdate = db.Column(db.String(20), nullable=False) #등록일자
    cp_edtdate = db.Column(db.String(20)) #수정일자
    cp_ip = db.Column(db.String(20)) #아이피

    ad_period = db.relationship('AdPeriod', backref='company', lazy=True)
    viewlog = db.relationship('Viewlog', backref='company', lazy=True)
    event_pub = db.relationship('EventPub', back_populates='company')
    event = db.relationship('Event', backref='company', lazy=True)
    favorite = db.relationship('Favorite', backref='company', lazy=True)
    review = db.relationship('Review', backref='company', lazy=True)