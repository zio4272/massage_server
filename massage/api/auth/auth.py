# -*- coding:utf8 -*-
#pylint: disable=E1101,C0103
import datetime

from flask_restful import Resource, reqparse
from flask_restful_swagger_2 import swagger

from massage import db
from massage.swagger import ResponseModel
from massage.utils import RestfulType
from massage.models import Member

from .utils import encode_token, decode_token

signup_parser = reqparse.RequestParser()
signup_parser.add_argument('mb_id', type=RestfulType.alphanumeric,\
    required=True, location='form')
signup_parser.add_argument('mb_pwd', type=RestfulType.alphanumeric,\
    required=True, location='form')
signup_parser.add_argument('mb_name', type=str, required=True, location='form')
signup_parser.add_argument('mb_email', type=str, required=True, location='form')
signup_parser.add_argument('mb_phone', type=str, required=True, location='form')

class Auth(Resource):
    @swagger.doc({
        'tags': ['member'],
        'description': '회원가입',
        'parameters': [
            {
                'name': 'mb_id',
                'description': '유저 아이디',
                'in': 'formData',
                'type': 'string',
                'required': True
            }, {
                'name': 'mb_pwd',
                'description': '유저 비밀번호',
                'in': 'formData',
                'type': 'string',
                'required': True
            }, {
                'name': 'mb_name',
                'description': '유저 이름',
                'in': 'formData',
                'type': 'string',
                'required': True
            }, {
                'name': 'mb_email',
                'description': '유저 이메일',
                'in': 'formData',
                'type': 'string',
                'required': True
            }, {
                'name': 'mb_phone',
                'description': '유저 휴대폰 번호. 정규식은 `^[\d]{3}-[\d]{3,4}-[\d]{4}$` 사용',
                'in': 'formData',
                'type': 'string',
                'required': True
            }
        ],
        'responses': {
            '201': {
                'description': '회원가입 성공',
                'schema': ResponseModel,
                'examples': {
                    'application/json': {
                        'code': 201,
                        'message': '회원가입 성공',
                        "data": {
                            "member": {
                                "id": 19,
                                "mb_id": "qkrqhdud1004",
                                "mb_regtype": "NM",
                                "mb_name": "박보영",
                                "mb_email": "qkrqhdud@1004.com",
                                "mb_phone": "010-1234-5678",
                                "mb_regdate": "2018-08-31 09:14:55",
                                "member_token": "some value"
                            }
                        }
                    }
                }
            },
            '400': {
                'description': '파라미터 값 이상',
                'schema': ResponseModel,
                'examples': {
                    'application/json': {
                        'code': 400,
                        'message': '특정 파라미터 값이 올바르지 않습니다.'
                    }
                }
            }
        }
    })
    def put(self):
        """ 회원가입 """
        args = signup_parser.parse_args()

        if not (len(args['mb_id']) >= 8 and len(args['mb_id']) <= 16):
            return {
                'code': 400,
                'message': '유저 아이디 값이 올바르지 않습니다.'
            }, 400
        elif not (len(args['mb_pwd']) >= 8 and len(args['mb_pwd']) <= 16):
            return {
                'code': 400,
                'message': '유저 비밀번호 값이 올바르지 않습니다.'
            }, 400
        elif not Member.verify_name(args['mb_name']):
            return {
                'code': 400,
                'message': '사용자 이름 값이 올바르지 않습니다.'
            }, 400
        elif not Member.verify_email(args['mb_email']):
            return {
                'code': 400,
                'message': '이메일 값이 올바르지 않습니다.'
            }, 400
        elif not Member.verify_phone_number(args['mb_phone']):
            return {
                'code': 400,
                'message': '휴대전화 값이 올바르지 않습니다.'
            }, 400

        member = Member.query.filter_by(mb_id=args['mb_id']).first()
        if member is not None:
            return {
                'code': 400,
                'message': '중복된 유저 아이디가 존재합니다.'
            }, 400

        member = Member.query.filter_by(mb_email=args['mb_email']).first()
        if member is not None:
            return {
                'code': 400,
                'message': '중복된 유저 이메일이 존재합니다.'
            }, 400

        user = Member.query.filter_by(mb_phone=args['mb_phone']).first()
        if user is not None:
            return {
                'code': 400,
                'message': '중복된 유저 전화번호가 존재합니다.'
            }, 400

        reg_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_member = Member()
        new_member.mb_id = args['mb_id']
        new_member.mb_pwd = args['mb_pwd']
        new_member.mb_name = args['mb_name']
        new_member.mb_email = args['mb_email']
        new_member.mb_phone = args['mb_phone']
        new_member.mb_regdate = reg_date
        new_member.user_token = encode_token(new_member)

        # if args['address']:
        #     new_member.address = args['address']

        db.session.add(new_member)
        db.session.commit()

        return {
            'code': 201,
            'message': '회원가입 성공입니다.',
            'data': {
                'member': {
                    'id': new_member.id,
                    'mb_id': new_member.mb_id,
                    'mb_regtype': new_member.mb_regtype,
                    'mb_name': new_member.mb_name,
                    'mb_email': new_member.mb_email,
                    'mb_phone': new_member.mb_phone,
                    'mb_regdate': new_member.mb_regdate,
                    'member_token': encode_token(new_member)
                }
            }
        }, 201