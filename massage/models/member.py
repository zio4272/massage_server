# -*- coding:utf8 -*-
# pylint: disable=E1101
import hashlib
import re
import datetime

from massage import db

class Member(db.Model):
    """ 사용자 테이블 """
    __tablename__ = 'member'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    mb_id = db.Column(db.String(40), nullable=False, unique=True)
    mb_pwd = db.Column(db.String(255), nullable=False)
    mb_level = db.Column(db.Integer, nullable=False, default=1) #1:일반회원, 2:업체회원, 9:슈퍼관리자
    mb_regtype = db.Column(db.String(2), nullable=False, default='NM') #NM:일반, KT:카톡, NV:네이버
    mb_name = db.Column(db.String(20), nullable=False)
    mb_email = db.Column(db.String(60), nullable=False)
    mb_phone = db.Column(db.String(20), nullable=False)
    mb_autologin = db.Column(db.String(1), nullable=False, default='0') #0사용안함 , 1사용
    mb_use_push = db.Column(db.String(1), nullable=False, default='1') #0사용안함 , 1사용
    mb_state = db.Column(db.String(1), nullable=False, default='N') #N일반 , B차단 , O탈퇴
    mb_ip = db.Column(db.String(20))
    mb_bandate = db.Column(db.String(20))
    mb_regdate = db.Column(db.String(20))
    mb_edtdate = db.Column(db.String(20))
    mb_outdate = db.Column(db.String(20))

    company = db.relationship('Company', backref='member', lazy=True)
    ad_period = db.relationship('AdPeriod', backref='member', lazy=True)
    coupon = db.relationship('Coupon', backref='member', lazy=True)
    event_pub = db.relationship('EventPub', backref='member', lazy=True)
    favorite = db.relationship('Favorite', backref='member', lazy=True)
    review = db.relationship('Review', backref='member', lazy=True)
    files = db.relationship('Files', backref='member', lazy=True)
    
    @staticmethod
    def generate_password_hash(password):
        pre_hashed = hashlib.sha512(('x3FpknhFyR' + password + 'a6E8kInyyW')\
            .encode('utf8')).hexdigest()
        return hashlib.md5(pre_hashed.encode('utf8')).hexdigest()

    @staticmethod
    def check_password_hash(mb_pwd, password):
        return mb_pwd == Member.generate_password_hash(password)

    @property
    def password(self):
        raise AttributeError('`password` is not a readable attribute')

    @password.setter
    def password(self, password):
        self.mb_pwd = self.generate_password_hash(password)

    def verify_password(self, password):
        return self.check_password_hash(self.mb_pwd, password)
    
    @staticmethod
    def verify_phone_number(mb_phone):
        phone_pattern = re.compile(r'^[\d]{3}-[\d]{3,4}-[\d]{4}$')
        return phone_pattern.match(mb_phone)

    @staticmethod
    def verify_email(mb_email):
        email_pattern = re.compile(r'^[A-Z0-9a-z._%+-]{1,64}@[A-Za-z0-9.-]{2,}\.[A-Za-z0-9.-]{2,}$')
        return email_pattern.match(mb_email)

    @staticmethod
    def verify_name(mb_name):
        name_pattern = re.compile(r'^[가-힣]{2,5}$')
        return name_pattern.match(mb_name)