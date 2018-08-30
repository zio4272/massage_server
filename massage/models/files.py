# -*- coding:utf8 -*-
# pylint: disable=E1101
import datetime

from massage import db

class Files(db.Model):
    """ 파일 테이블 """
    __tablename__ = 'files'

    fi_idx = db.Column(db.Integer, nullable=False, primary_key=True)
    mb_id = db.Column(db.Integer, db.ForeignKey('member.id')) #회원아이디
    fi_gubun1 = db.Column(db.String(20)) #구분1
    fi_gubun2 = db.Column(db.String(20)) #구분2
    fi_gubun3 = db.Column(db.String(20)) #구분3
    fi_rname = db.Column(db.String(255), nullable=False) #실제파일이름
    fi_vname = db.Column(db.String(255), nullable=False) #가상파일이름
    fi_is_img = db.Column(db.String(1), nullable=False) #이미지인지 아닌지
    fi_mime_type = db.Column(db.String(20), nullable=False) #마임타입(파일종류)
    fi_size = db.Column(db.String(20)) #파일사이즈
    fi_width = db.Column(db.String(6)) #이미지가로사이즈
    fi_height = db.Column(db.String(6)) #이미지세로사이즈
    fi_regdate = db.Column(db.String(20)) #아이피