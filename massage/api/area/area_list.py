# -*- coding:utf8 -*-
#pylint: disable=E1101,C0103
import datetime

from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import swagger

from massage import db
from massage.swagger import ResponseModel
from massage.models import AreaMain, AreaSub

class AreaList(Resource):
    @swagger.doc({
        'tags': ['area'],
        'description': '지역 전체 조회',
        'parameters': [
            
        ],
        'responses': {
            '200': {
                'description': '지역 전체 조회',
                'schema': ResponseModel,
                'examples': {
                    'application/json': {
                        'code': 200,
                        'message': '지역 전체조회 성공',
                        'data': {
                            "area_main": [
                                {
                                    "am_idx": 1,
                                    "am_area": "서울",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": [
                                        {
                                            "as_idx": 1,
                                            "am_idx": 1,
                                            "as_area": "강남/역삼/서초",
                                            "as_step": 'null',
                                            "as_regdate": "",
                                            "as_edtdate": 'null',
                                            "as_ip": 'null'
                                        },
                                        {
                                            "as_idx": 2,
                                            "am_idx": 1,
                                            "as_area": "송파/잠실/신천",
                                            "as_step": 'null',
                                            "as_regdate": "",
                                            "as_edtdate": 'null',
                                            "as_ip": 'null'
                                        },
                                        {
                                            "as_idx": 3,
                                            "am_idx": 1,
                                            "as_area": "영등포/구로/금천",
                                            "as_step": 'null',
                                            "as_regdate": "",
                                            "as_edtdate": 'null',
                                            "as_ip": 'null'
                                        }
                                    ]
                                },
                                {
                                    "am_idx": 2,
                                    "am_area": "경기",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": [
                                        {
                                            "as_idx": 4,
                                            "am_idx": 2,
                                            "as_area": "수원/인계/권선/영통",
                                            "as_step": 'null',
                                            "as_regdate": "",
                                            "as_edtdate": 'null',
                                            "as_ip": 'null'
                                        },
                                        {
                                            "as_idx": 5,
                                            "am_idx": 2,
                                            "as_area": "수원역/세류/팔달구/구운/장안",
                                            "as_step": 'null',
                                            "as_regdate": "",
                                            "as_edtdate": 'null',
                                            "as_ip": 'null'
                                        },
                                        {
                                            "as_idx": 6,
                                            "am_idx": 2,
                                            "as_area": "안성/평택/송탄",
                                            "as_step": 'null',
                                            "as_regdate": "",
                                            "as_edtdate": 'null',
                                            "as_ip": 'null'
                                        }
                                    ]
                                },
                                {
                                    "am_idx": 3,
                                    "am_area": "부산",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": [
                                        {
                                            "as_idx": 7,
                                            "am_idx": 3,
                                            "as_area": "해운대/재송",
                                            "as_step": 'null',
                                            "as_regdate": "",
                                            "as_edtdate": 'null',
                                            "as_ip": 'null'
                                        },
                                        {
                                            "as_idx": 8,
                                            "am_idx": 3,
                                            "as_area": "송정/기장",
                                            "as_step": 'null',
                                            "as_regdate": "",
                                            "as_edtdate": 'null',
                                            "as_ip": 'null'
                                        },
                                        {
                                            "as_idx": 9,
                                            "am_idx": 3,
                                            "as_area": "서면/초읍/양정",
                                            "as_step": 'null',
                                            "as_regdate": "",
                                            "as_edtdate": 'null',
                                            "as_ip": 'null'
                                        }
                                    ]
                                },
                                {
                                    "am_idx": 4,
                                    "am_area": "대구",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 5,
                                    "am_area": "인천",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 6,
                                    "am_area": "광주",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 7,
                                    "am_area": "대전",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 8,
                                    "am_area": "울산",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 9,
                                    "am_area": "강원",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 10,
                                    "am_area": "경남",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 11,
                                    "am_area": "경북",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 12,
                                    "am_area": "전남",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 13,
                                    "am_area": "전북",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 14,
                                    "am_area": "제주",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 15,
                                    "am_area": "충남",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                },
                                {
                                    "am_idx": 16,
                                    "am_area": "충북",
                                    "am_step": 'null',
                                    "am_regdate": "",
                                    "am_edtdate": 'null',
                                    "am_ip": 'null',
                                    "area_sub": []
                                }
                            ]
                        }
                    }
                }
            }
        }
    })
    def get(self):
        """ 지역 전체 조회 """

        main = AreaMain.query.all()
        print(main)

        if main:
        

            return {
                'code': 200,
                'message': '지역 전체조회 성공',
                'data': {
                    'area_main': [
                        x.get_area_main_object(sub_object=True) for x in main
                    ]
                }
            }, 200