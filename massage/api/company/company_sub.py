# -*- coding:utf8 -*-
#pylint: disable=E1101,C0103
import datetime

from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import swagger

from massage import db
from massage.swagger import ResponseModel
from massage.models import Company, AreaSub

post_parser = reqparse.RequestParser()
post_parser.add_argument('as_idx', type=str, location='form', required=True)

class CompanysSub(Resource):

    @swagger.doc({
        'tags': ['company'],
        'description': '2차 지역별 제휴업체 조회',
        'parameters': [
            {
                'name': 'as_idx',
                'description': '2차 지역 as_idx',
                'in': 'formData',
                'type': 'string',
                'required': True
            }
        ],
        'responses': {
            '200': {
                'description': '2차 지역별 제휴업체 조회',
                'schema': ResponseModel,
                'examples': {
                    'application/json': {
                        'code': 200,
                        'message': '2차 지역별 제휴업체 조회 성공',
                        'data': {
                            "area_sub": [
                                {
                                    "as_idx": 1,
                                    "am_idx": 1,
                                    "as_area": "강남/역삼/서초",
                                    "as_step": 'null',
                                    "as_regdate": "",
                                    "as_edtdate": 'null',
                                    "as_ip": 'null',
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
        """ 2차 지역별 제휴업체 조회 """
        args = post_parser.parse_args()

        company_sub = AreaSub.query\
            .filter(AreaSub.as_idx == args['as_idx'])\
            .filter(Company.as_idx == AreaSub.as_idx)\
            .all()            
        print(company_sub)

        if args['as_idx']:
            if company_sub:
                return {
                    'code': 200,
                    'message': '2차 지역별 제휴업체 조회 성공',
                    'data': {
                        'area_sub': [
                            x.get_area_sub_object(company_object=True) for x in company_sub
                        ]
                    } 
                }, 200

            return {
                'code': 400,
                'message': '데이터가 존재하지 않습니다.'
            }, 400