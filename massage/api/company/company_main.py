# -*- coding:utf8 -*-
#pylint: disable=E1101,C0103
import datetime

from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import swagger

from massage import db
from massage.swagger import ResponseModel
from massage.models import Company, AreaMain

post_parser = reqparse.RequestParser()
post_parser.add_argument('am_idx', type=str, location='form', required=True)

class CompanyMain(Resource):

    @swagger.doc({
        'tags': ['company'],
        'description': '1차 지역별 제휴업체 조회',
        'parameters': [
            {
                'name': 'am_idx',
                'description': '1차 지역 (am_idx 값을 넣어주세요.)',
                'in': 'formData',
                'type': 'string',
                'required': True
            }
        ],
        'responses': {
            '200': {
                'description': '1차 지역별 제휴업체 조회',
                'schema': ResponseModel,
                'examples': {
                    'application/json': {
                        'code': 200,
                        'message': '1차 지역별 제휴업체 조회 성공',
                        'data': {
                            "area_main": [
                                {
                                    "am_idx": 1,
                                    "am_area": "서울",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "company": [
                                        {
                                            "cp_idx": 1,
                                            "mb_id": 1,
                                            "cp_sangho": "건강테라피 (아차산)",
                                            "cp_always_time": "1",
                                            "cp_always_day": "1",
                                            "cp_otime": "9",
                                            "cp_ctime": "24",
                                            "cp_h_0": "1",
                                            "cp_h_1": "1",
                                            "cp_h_2": "1",
                                            "cp_h_3": "1",
                                            "cp_h_4": "1",
                                            "cp_h_5": "1",
                                            "cp_h_6": "1",
                                            "cp_price": "60000",
                                            "cp_sale_price": "30000",
                                            "cp_phone": "010-1234-5678",
                                            "cp_vphone": "0507-462-5313",
                                            "cp_zipcode": "12321",
                                            "cp_addr1": "서울특별시 광진구 구의동",
                                            "cp_addr2": "바보빌딩 101호",
                                            "cp_lat": "0E-10",
                                            "cp_long": "0E-10",
                                            "am_idx": 1,
                                            "as_idx": 1,
                                            "cp_star": "9",
                                            "cp_fav": 5,
                                            "cp_content": "60분에 30000원",
                                            "cp_open": "1",
                                            "cp_regdate": "2018-09-01 00:00:00",
                                            "cp_edtdate": 'null',
                                            "cp_ip": 'null'
                                        },
                                        {
                                            "cp_idx": 2,
                                            "mb_id": 1,
                                            "cp_sangho": "나나롯아로마 (마곡)",
                                            "cp_always_time": "1",
                                            "cp_always_day": "1",
                                            "cp_otime": "9",
                                            "cp_ctime": "24",
                                            "cp_h_0": "1",
                                            "cp_h_1": "1",
                                            "cp_h_2": "1",
                                            "cp_h_3": "1",
                                            "cp_h_4": "1",
                                            "cp_h_5": "1",
                                            "cp_h_6": "1",
                                            "cp_price": "60000",
                                            "cp_sale_price": "25000",
                                            "cp_phone": "010-4892-1982",
                                            "cp_vphone": "0507-462-5629",
                                            "cp_zipcode": "98494",
                                            "cp_addr1": "서울특별시 강서구 마곡동",
                                            "cp_addr2": "멍충빌빙 202호",
                                            "cp_lat": "0E-10",
                                            "cp_long": "0E-10",
                                            "am_idx": 1,
                                            "as_idx": 1,
                                            "cp_star": "4",
                                            "cp_fav": 9,
                                            "cp_content": "60분에 25000원",
                                            "cp_open": "1",
                                            "cp_regdate": "2018-09-01 00:00:00",
                                            "cp_edtdate": 'null',
                                            "cp_ip": 'null'
                                        },
                                        {
                                            "cp_idx": 3,
                                            "mb_id": 1,
                                            "cp_sangho": "그린타이 (잠실)",
                                            "cp_always_time": "1",
                                            "cp_always_day": "1",
                                            "cp_otime": "9",
                                            "cp_ctime": "24",
                                            "cp_h_0": "1",
                                            "cp_h_1": "1",
                                            "cp_h_2": "1",
                                            "cp_h_3": "1",
                                            "cp_h_4": "1",
                                            "cp_h_5": "1",
                                            "cp_h_6": "1",
                                            "cp_price": "60000",
                                            "cp_sale_price": "25000",
                                            "cp_phone": "010-4892-1982",
                                            "cp_vphone": "0507-462-5629",
                                            "cp_zipcode": "98494",
                                            "cp_addr1": "서울특별시 송파구 삼전동",
                                            "cp_addr2": "왈왈왈왈 303호",
                                            "cp_lat": "0E-10",
                                            "cp_long": "0E-10",
                                            "am_idx": 1,
                                            "as_idx": 2,
                                            "cp_star": "10",
                                            "cp_fav": 12,
                                            "cp_content": "60분에 10000원",
                                            "cp_open": "1",
                                            "cp_regdate": "2018-09-01 00:00:00",
                                            "cp_edtdate": 'null',
                                            "cp_ip": 'null'
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                }
            }
        }
    })
    def post(self):
        """ 1차 지역별 제휴업체 조회 """
        args = post_parser.parse_args()

        company_main = AreaMain.query\
            .filter(AreaMain.am_idx == args['am_idx'])\
            .filter(Company.am_idx == AreaMain.am_idx)\
            .all()            
        print(company_main)

        if args['am_idx']:
            if company_main:
                return {
                    'code': 200,
                    'message': '1차 지역별 제휴업체 조회 성공',
                    'data': {
                        'area_main': [
                            x.get_area_main_object(company_object=True) for x in company_main
                        ]
                    } 
                }, 200

            return {
                'code': 400,
                'message': '데이터가 존재하지 않습니다.'
            }, 400