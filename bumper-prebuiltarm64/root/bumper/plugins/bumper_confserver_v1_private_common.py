#!/usr/bin/env python3
import logging

from aiohttp import web

from bumper import plugins
from bumper.models import *


class v1_private_common(plugins.ConfServerApp):

    def __init__(self):
        self.name = "v1_private_common"
        self.plugin_type = "sub_api"
        self.sub_api = "api_v1"

        self.routes = [
            web.route("*", "/private/{country}/{language}/{devid}/{apptype}/{appversion}/{devtype}/{aid}/common/checkAPPVersion", self.handle_checkAPPVersion, name="v1_common_checkAppVersion"),
            web.route("*", "/private/{country}/{language}/{devid}/{apptype}/{appversion}/{devtype}/{aid}/common/checkVersion", self.handle_checkVersion, name="v1_common_checkVersion"),
            web.route("*", "/private/{country}/{language}/{devid}/{apptype}/{appversion}/{devtype}/{aid}/common/uploadDeviceInfo", self.handle_uploadDeviceInfo, name="v1_common_uploadDeviceInfo"),
            web.route("*", "/private/{country}/{language}/{devid}/{apptype}/{appversion}/{devtype}/{aid}/common/getSystemReminder", self.handle_getSystemReminder, name="v1_common_getSystemReminder"),
            web.route("*", "/private/{country}/{language}/{devid}/{apptype}/{appversion}/{devtype}/{aid}/common/getConfig",self.handle_getConfig, name="v1_common_getConfig"),
            web.route("*", "/private/{country}/{language}/{devid}/{apptype}/{appversion}/{devtype}/{aid}/common/getAreas",self.handle_getAreas, name="v1_common_getAreas"),
            web.route("*", "/private/{country}/{language}/{devid}/{apptype}/{appversion}/{devtype}/{aid}/common/getAgreementURLBatch", self.handle_getAgreementURLBatch, name="v1_common_getAgreementURLBatch"),
            web.route("*", "/private/{country}/{language}/{devid}/{apptype}/{appversion}/{devtype}/{aid}/common/getTimestamp", self.handle_getTimestamp, name="v1_common_getTimestamp"),

        ]

        self.get_milli_time = bumper.ConfServer.ConfServer_GeneralFunctions().get_milli_time

    async def handle_checkVersion(self, request):
        try:
            body = {
                "code": bumper.RETURN_API_SUCCESS,
                "data": {
                    "c": None,
                    "img": None,
                    "r": 0,
                    "t": None,
                    "u": None,
                    "ut": 0,
                    "v": None,
                },
                "msg": "????????????",
                "time": self.get_milli_time(datetime.utcnow().timestamp()),
            }

            return web.json_response(body)

        except Exception as e:
            logging.exception("{}".format(e))

    async def handle_checkAPPVersion(self, request):  # EcoVacs Home
        try:
            body = {
                "code": bumper.RETURN_API_SUCCESS,
                "data": {
                    "c": None,
                    "downPageUrl": None,
                    "img": None,
                    "nextAlertTime": None,
                    "r": 0,
                    "t": None,
                    "u": None,
                    "ut": 0,
                    "v": None,
                },
                "msg": "????????????",
                "success": True,
                "time": self.get_milli_time(datetime.utcnow().timestamp()),
            }

            return web.json_response(body)

        except Exception as e:
            logging.exception("{}".format(e))

    async def handle_uploadDeviceInfo(self, request):  # EcoVacs Home
        try:
            body = {
                "code": bumper.RETURN_API_SUCCESS,
                "data": None,
                "msg": "????????????",
                "success": True,
                "time": self.get_milli_time(datetime.utcnow().timestamp()),
            }

            return web.json_response(body)

        except Exception as e:
            logging.exception("{}".format(e))

    async def handle_getSystemReminder(self, request):  # EcoVacs Home
        try:
            body = {
                "code": bumper.RETURN_API_SUCCESS,
                "data": {
                    "iosGradeTime": {"iodGradeFlag": "N"},
                    "openNotification": {
                        "openNotificationContent": None,
                        "openNotificationFlag": "N",
                        "openNotificationTitle": None,
                    },
                },
                "msg": "????????????",
                "success": True,
                "time": self.get_milli_time(datetime.utcnow().timestamp()),
            }

            return web.json_response(body)

        except Exception as e:
            logging.exception("{}".format(e))

    async def handle_getConfig(self, request):
        try:
            data = []
            for key in request.query["keys"].split(','):
                data.append({
                    "key": key,
                    "value": "Y"
                })

            body = {
                "code": bumper.RETURN_API_SUCCESS,
                "data": data,
                "msg": "????????????",
                "success": True,
                "time": self.get_milli_time(datetime.utcnow().timestamp()),
            }

            return web.json_response(body)

        except Exception as e:
            logging.exception("{}".format(e))

    async def handle_getAreas(self, request):
        try:
            body = {
                "code": bumper.RETURN_API_SUCCESS,
                "data": AREA_LIST,
                "msg": "????????????",
                "success": True,
                "time": self.get_milli_time(datetime.utcnow().timestamp()),
            }

            return web.json_response(body)

        except Exception as e:
            logging.exception("{}".format(e))

    async def handle_getAgreementURLBatch(self, request):  # EcoVacs Home
        try:
            body = {
                "code": bumper.RETURN_API_SUCCESS,
                "data": [
                    {
                        "acceptTime": None,
                        "force": None,
                        "id": "20180804040641_7d746faf18b8cb22a50d145598fe4c90",
                        "type": "USER",
                        "url": "https://gl-eu-wap.ecovacs.com/content/agreement?id=20180804040641_7d746faf18b8cb22a50d145598fe4c90&language=EN",
                        "version": "1.03"
                    },
                    {
                        "acceptTime": None,
                        "force": None,
                        "id": "20180804040245_4e7c56dfb7ebd3b81b1f2747d0859fac",
                        "type": "PRIVACY",
                        "url": "https://gl-eu-wap.ecovacs.com/content/agreement?id=20180804040245_4e7c56dfb7ebd3b81b1f2747d0859fac&language=EN",
                        "version": "1.03"
                    }
                ],
                "msg": "????????????",
                "success": True,
                "time": self.get_milli_time(datetime.utcnow().timestamp()),
            }

            return web.json_response(body)

        except Exception as e:
            logging.exception("{}".format(e))

    async def handle_getTimestamp(self, request):  # EcoVacs Home
        try:
            time = self.get_milli_time(datetime.utcnow().timestamp())
            body = {
                "code": bumper.RETURN_API_SUCCESS,
                "data": {
                    "timestamp": time
                },
                "msg": "????????????",
                "success": True,
                "time": time,
            }

            return web.json_response(body)

        except Exception as e:
            logging.exception("{}".format(e))


plugin = v1_private_common()

AREA_LIST = {"currentVersion": 231,
             "areaList": [{"areaKey": "JP", "chsName": "??????", "enName": "Japan", "pyFirst": "R"},
                          {"areaKey": "MY", "chsName": "????????????", "enName": "Malaysia", "pyFirst": "M"},
                          {"areaKey": "DE", "chsName": "??????", "enName": "Germany", "pyFirst": "D"},
                          {"areaKey": "LI", "chsName": "???????????????", "enName": "Liechtenstein", "pyFirst": "L"},
                          {"areaKey": "AT", "chsName": "?????????", "enName": "Austria", "pyFirst": "A"},
                          {"areaKey": "TW", "chsName": "??????", "enName": "Taiwan", "pyFirst": "T"},
                          {"areaKey": "FR", "chsName": "??????", "enName": "France", "pyFirst": "F"},
                          {"areaKey": "CN", "chsName": "????????????", "enName": "China Mainland", "pyFirst": "Z"},
                          {"areaKey": "SG", "chsName": "?????????", "enName": "Singapore", "pyFirst": "X"},
                          {"areaKey": "RE", "chsName": "????????????", "enName": "Reunion Island", "pyFirst": "L"},
                          {"areaKey": "EH", "chsName": "????????????", "enName": "Western Sahara", "pyFirst": "X"},
                          {"areaKey": "WF", "chsName": "?????????????????????????????????", "enName": "Wallis and Futuna Islands",
                           "pyFirst": "W"},
                          {"areaKey": "KP", "chsName": "??????", "enName": "North Korea", "pyFirst": "C"},
                          {"areaKey": "ZW", "chsName": "????????????", "enName": "Zimbabwe", "pyFirst": "J"},
                          {"areaKey": "VI", "chsName": "?????????????????????", "enName": "United States Virgin Islands",
                           "pyFirst": "M"},
                          {"areaKey": "PF", "chsName": "?????????????????????", "enName": "French Polynesia",
                           "pyFirst": "F"},
                          {"areaKey": "DJ", "chsName": "?????????", "enName": "Djibouti", "pyFirst": "J"},
                          {"areaKey": "KZ", "chsName": "???????????????", "enName": "Kazakhstan", "pyFirst": "H"},
                          {"areaKey": "TV", "chsName": "?????????", "enName": "Tuvalu", "pyFirst": "T"},
                          {"areaKey": "VU", "chsName": "????????????", "enName": "Vanuatu", "pyFirst": "W"},
                          {"areaKey": "IN", "chsName": "??????", "enName": "India", "pyFirst": "Y"},
                          {"areaKey": "CM", "chsName": "?????????", "enName": "Cameroon", "pyFirst": "K"},
                          {"areaKey": "LK", "chsName": "????????????", "enName": "Sri Lanka", "pyFirst": "S"},
                          {"areaKey": "CC", "chsName": "???????????????", "enName": "Cocos Islands", "pyFirst": "K"},
                          {"areaKey": "KY", "chsName": "????????????", "enName": "Cayman Islands", "pyFirst": "K"},
                          {"areaKey": "QA", "chsName": "?????????", "enName": "Qatar", "pyFirst": "K"},
                          {"areaKey": "AZ", "chsName": "????????????", "enName": "Azerbaijan", "pyFirst": "A"},
                          {"areaKey": "HN", "chsName": "????????????", "enName": "Honduras", "pyFirst": "H"},
                          {"areaKey": "AW", "chsName": "????????????", "enName": "Aruba", "pyFirst": "A"},
                          {"areaKey": "KH", "chsName": "?????????", "enName": "Cambodia", "pyFirst": "J"},
                          {"areaKey": "CO", "chsName": "????????????", "enName": "Colombia", "pyFirst": "G"},
                          {"areaKey": "IR", "chsName": "??????", "enName": "Iran", "pyFirst": "Y"},
                          {"areaKey": "ZA", "chsName": "??????", "enName": "South Africa", "pyFirst": "N"},
                          {"areaKey": "UY", "chsName": "?????????", "enName": "Uruguay", "pyFirst": "W"},
                          {"areaKey": "GU", "chsName": "??????", "enName": "Guam", "pyFirst": "G"},
                          {"areaKey": "GH", "chsName": "??????", "enName": "Ghana", "pyFirst": "J"},
                          {"areaKey": "GN", "chsName": "?????????", "enName": "Guynea", "pyFirst": "J"},
                          {"areaKey": "MH", "chsName": "???????????????", "enName": "Marshall Islands",
                           "pyFirst": "M"},
                          {"areaKey": "SE", "chsName": "??????", "enName": "Sweden", "pyFirst": "R"},
                          {"areaKey": "SB", "chsName": "???????????????", "enName": "Solomon Islands",
                           "pyFirst": "S"},
                          {"areaKey": "NE", "chsName": "?????????", "enName": "Niger", "pyFirst": "N"},
                          {"areaKey": "HT", "chsName": "??????", "enName": "Haiti", "pyFirst": "H"},
                          {"areaKey": "PL", "chsName": "??????", "enName": "Poland", "pyFirst": "B"},
                          {"areaKey": "DO", "chsName": "?????????????????????", "enName": "Dominican Republic",
                           "pyFirst": "D"},
                          {"areaKey": "PS", "chsName": "????????????", "enName": "Palestine", "pyFirst": "B"},
                          {"areaKey": "KW", "chsName": "?????????", "enName": "Kuwait", "pyFirst": "K"},
                          {"areaKey": "UZ", "chsName": "??????????????????", "enName": "Republic of Uzbekistan",
                           "pyFirst": "W"},
                          {"areaKey": "GD", "chsName": "????????????", "enName": "Grenada", "pyFirst": "G"},
                          {"areaKey": "KG", "chsName": "??????????????????", "enName": "Kyrgyzstan", "pyFirst": "J"},
                          {"areaKey": "JO", "chsName": "??????", "enName": "Jordan", "pyFirst": "Y"},
                          {"areaKey": "IL", "chsName": "?????????", "enName": "Israel", "pyFirst": "Y"},
                          {"areaKey": "UK", "chsName": "??????", "enName": "United Kingdom", "pyFirst": "Y"},
                          {"areaKey": "MW", "chsName": "?????????", "enName": "Malawi", "pyFirst": "M"},
                          {"areaKey": "MC", "chsName": "?????????", "enName": "Monaco", "pyFirst": "M"},
                          {"areaKey": "IC", "chsName": "???????????????", "enName": "Canary Islands", "pyFirst": "J"},
                          {"areaKey": "JM", "chsName": "?????????", "enName": "Jamaica", "pyFirst": "Y"},
                          {"areaKey": "MP", "chsName": "?????????????????????", "enName": "The Northern Mariana Islands",
                           "pyFirst": "B"},
                          {"areaKey": "BH", "chsName": "?????????", "enName": "Bahrain", "pyFirst": "B"},
                          {"areaKey": "MK", "chsName": "?????????", "enName": "Macedonia", "pyFirst": "M"},
                          {"areaKey": "ET", "chsName": "???????????????", "enName": "Ethiopia", "pyFirst": "A"},
                          {"areaKey": "CL", "chsName": "??????", "enName": "Chile", "pyFirst": "Z"},
                          {"areaKey": "GP", "chsName": "???????????????", "enName": "Guadeloupe", "pyFirst": "G"},
                          {"areaKey": "FK", "chsName": "???????????????", "enName": "Falkland Islands",
                           "pyFirst": "F"},
                          {"areaKey": "GL", "chsName": "?????????", "enName": "Greenland", "pyFirst": "G"},
                          {"areaKey": "BF", "chsName": "???????????????", "enName": "Burkina Faso", "pyFirst": "B"},
                          {"areaKey": "GI", "chsName": "????????????", "enName": "Gibraltar", "pyFirst": "Z"},
                          {"areaKey": "MV", "chsName": "????????????", "enName": "Maldives", "pyFirst": "M"},
                          {"areaKey": "CU", "chsName": "??????", "enName": "Cuba", "pyFirst": "G"},
                          {"areaKey": "LS", "chsName": "?????????", "enName": "Lesotho", "pyFirst": "L"},
                          {"areaKey": "MA", "chsName": "?????????", "enName": "Morocco", "pyFirst": "M"},
                          {"areaKey": "AL", "chsName": "???????????????", "enName": "Albania", "pyFirst": "A"},
                          {"areaKey": "AF", "chsName": "?????????", "enName": "Afghanistan", "pyFirst": "A"},
                          {"areaKey": "CA", "chsName": "?????????", "enName": "Canada", "pyFirst": "J"},
                          {"areaKey": "BB", "chsName": "????????????", "enName": "Barbados", "pyFirst": "B"},
                          {"areaKey": "LC", "chsName": "???????????????", "enName": "Saint Lucia", "pyFirst": "S"},
                          {"areaKey": "PN", "chsName": "???????????????", "enName": "Pitcairn Island",
                           "pyFirst": "P"},
                          {"areaKey": "LV", "chsName": "????????????", "enName": "Latvia", "pyFirst": "L"},
                          {"areaKey": "NO", "chsName": "??????", "enName": "Norway", "pyFirst": "N"},
                          {"areaKey": "BE", "chsName": "?????????", "enName": "Belgium", "pyFirst": "B"},
                          {"areaKey": "VE", "chsName": "????????????", "enName": "Venezuela", "pyFirst": "W"},
                          {"areaKey": "MQ", "chsName": "????????????", "enName": "Martinique", "pyFirst": "M"},
                          {"areaKey": "GY", "chsName": "?????????", "enName": "Guyana", "pyFirst": "G"},
                          {"areaKey": "AM", "chsName": "????????????", "enName": "Armenia", "pyFirst": "Y"},
                          {"areaKey": "EC", "chsName": "????????????", "enName": "Ecuador", "pyFirst": "E"},
                          {"areaKey": "CV", "chsName": "?????????", "enName": "Cape Verde", "pyFirst": "F"},
                          {"areaKey": "NZ", "chsName": "?????????", "enName": "New Zealand", "pyFirst": "X"},
                          {"areaKey": "RO", "chsName": "????????????", "enName": "Romania", "pyFirst": "L"},
                          {"areaKey": "DM", "chsName": "????????????", "enName": "Dominica", "pyFirst": "D"},
                          {"areaKey": "TZ", "chsName": "????????????", "enName": "Tanzania", "pyFirst": "T"},
                          {"areaKey": "BD", "chsName": "????????????", "enName": "Bangladesh", "pyFirst": "M"},
                          {"areaKey": "TD", "chsName": "??????", "enName": "Chad", "pyFirst": "Z"},
                          {"areaKey": "LT", "chsName": "?????????", "enName": "Lithuania", "pyFirst": "L"},
                          {"areaKey": "TJ", "chsName": "???????????????", "enName": "Tajikistan", "pyFirst": "T"},
                          {"areaKey": "TK", "chsName": "?????????", "enName": "Tokelau", "pyFirst": "T"},
                          {"areaKey": "BS", "chsName": "???????????????", "enName": "Bahamas", "pyFirst": "B"},
                          {"areaKey": "MM", "chsName": "??????", "enName": "Myanmar", "pyFirst": "M"},
                          {"areaKey": "BI", "chsName": "?????????", "enName": "Burundi", "pyFirst": "B"},
                          {"areaKey": "PY", "chsName": "?????????", "enName": "Paraguay", "pyFirst": "B"},
                          {"areaKey": "SK", "chsName": "????????????", "enName": "Slovakia", "pyFirst": "S"},
                          {"areaKey": "FI", "chsName": "??????", "enName": "Finland", "pyFirst": "F"},
                          {"areaKey": "GA", "chsName": "??????", "enName": "Gabon", "pyFirst": "J"},
                          {"areaKey": "DZ", "chsName": "???????????????", "enName": "Algeria", "pyFirst": "A"},
                          {"areaKey": "FO", "chsName": "????????????", "enName": "Faroe Islands", "pyFirst": "F"},
                          {"areaKey": "ZM", "chsName": "?????????", "enName": "Zambia", "pyFirst": "Z"},
                          {"areaKey": "NU", "chsName": "??????", "enName": "Niue", "pyFirst": "N"},
                          {"areaKey": "ER", "chsName": "??????????????????", "enName": "Eritrea", "pyFirst": "E"},
                          {"areaKey": "HK", "chsName": "??????", "enName": "Hong Kong", "pyFirst": "X"},
                          {"areaKey": "IT", "chsName": "?????????", "enName": "Italy", "pyFirst": "Y"},
                          {"areaKey": "MS", "chsName": "??????????????????", "enName": "Montserrat", "pyFirst": "M"},
                          {"areaKey": "EE", "chsName": "????????????", "enName": "Estonia", "pyFirst": "A"},
                          {"areaKey": "WS", "chsName": "?????????", "enName": "Samoa", "pyFirst": "S"},
                          {"areaKey": "TG", "chsName": "??????", "enName": "Togo", "pyFirst": "D"},
                          {"areaKey": "ML", "chsName": "??????", "enName": "Mali", "pyFirst": "M"},
                          {"areaKey": "GF", "chsName": "???????????????", "enName": "French Guyana", "pyFirst": "F"},
                          {"areaKey": "KM", "chsName": "?????????", "enName": "Comoros", "pyFirst": "K"},
                          {"areaKey": "ID", "chsName": "???????????????", "enName": "Indonesia", "pyFirst": "Y"},
                          {"areaKey": "KE", "chsName": "?????????", "enName": "Kenya", "pyFirst": "K"},
                          {"areaKey": "EG", "chsName": "??????", "enName": "Egypt", "pyFirst": "A"},
                          {"areaKey": "NF", "chsName": "????????????", "enName": "Norfolk Island", "pyFirst": "N"},
                          {"areaKey": "RS", "chsName": "????????????", "enName": "Serbia", "pyFirst": "S"},
                          {"areaKey": "TR", "chsName": "?????????", "enName": "Turkey", "pyFirst": "T"},
                          {"areaKey": "DK", "chsName": "??????", "enName": "Denmark", "pyFirst": "D"},
                          {"areaKey": "AD", "chsName": "?????????", "enName": "Andorra", "pyFirst": "A"},
                          {"areaKey": "LR", "chsName": "????????????", "enName": "Liberia", "pyFirst": "L"},
                          {"areaKey": "AE", "chsName": "????????????????????????", "enName": "United Arab Emirates",
                           "pyFirst": "A"},
                          {"areaKey": "CH", "chsName": "??????", "enName": "Switzerland", "pyFirst": "R"},
                          {"areaKey": "AU", "chsName": "????????????", "enName": "Australia", "pyFirst": "A"},
                          {"areaKey": "TP", "chsName": "?????????", "enName": "East Timor", "pyFirst": "D"},
                          {"areaKey": "LY", "chsName": "?????????", "enName": "Libya", "pyFirst": "L"},
                          {"areaKey": "RW", "chsName": "?????????", "enName": "Rwanda", "pyFirst": "L"},
                          {"areaKey": "SA", "chsName": "???????????????", "enName": "Saudi Arabia", "pyFirst": "S"},
                          {"areaKey": "AR", "chsName": "?????????", "enName": "Argentina", "pyFirst": "A"},
                          {"areaKey": "GM", "chsName": "?????????", "enName": "Gambia", "pyFirst": "G"},
                          {"areaKey": "BY", "chsName": "????????????", "enName": "Belarus", "pyFirst": "B"},
                          {"areaKey": "SL", "chsName": "????????????", "enName": "Sierra Leone", "pyFirst": "S"},
                          {"areaKey": "TM", "chsName": "???????????????", "enName": "Turkmenistan", "pyFirst": "T"},
                          {"areaKey": "AG", "chsName": "?????????????????????", "enName": "Antigua and Barbuda",
                           "pyFirst": "A"},
                          {"areaKey": "MR", "chsName": "???????????????", "enName": "Mauritania", "pyFirst": "M"},
                          {"areaKey": "PT", "chsName": "?????????", "enName": "Portugal", "pyFirst": "P"},
                          {"areaKey": "BW", "chsName": "????????????", "enName": "Botswana", "pyFirst": "B"},
                          {"areaKey": "GT", "chsName": "????????????", "enName": "Guatemala", "pyFirst": "W"},
                          {"areaKey": "BT", "chsName": "??????", "enName": "Bhutan", "pyFirst": "B"},
                          {"areaKey": "AI", "chsName": "????????????", "enName": "Anguilla", "pyFirst": "A"},
                          {"areaKey": "OM", "chsName": "??????", "enName": "Oman", "pyFirst": "A"},
                          {"areaKey": "KI", "chsName": "????????????", "enName": "Kiribati", "pyFirst": "J"},
                          {"areaKey": "UA", "chsName": "?????????", "enName": "Ukraine", "pyFirst": "W"},
                          {"areaKey": "YE", "chsName": "??????", "enName": "Yemen", "pyFirst": "Y"},
                          {"areaKey": "DR", "chsName": "?????????????????????",
                           "enName": "Democratic Republic of the Congo", "pyFirst": "G"},
                          {"areaKey": "MD", "chsName": "????????????", "enName": "Moldova", "pyFirst": "M"},
                          {"areaKey": "GW", "chsName": "???????????????", "enName": "Guinea-Bissau", "pyFirst": "J"},
                          {"areaKey": "CG", "chsName": "??????????????????", "enName": "Congo Brazzaville",
                           "pyFirst": "G"},
                          {"areaKey": "SN", "chsName": "????????????", "enName": "Senegal", "pyFirst": "S"},
                          {"areaKey": "BA", "chsName": "??????", "enName": "Bosnia Hercegovina",
                           "pyFirst": "B"},
                          {"areaKey": "MO", "chsName": "??????", "enName": "Macao", "pyFirst": "A"},
                          {"areaKey": "KN", "chsName": "?????????????????????", "enName": "Saint Kitts and Nevis",
                           "pyFirst": "S"},
                          {"areaKey": "TO", "chsName": "??????", "enName": "Tonga", "pyFirst": "T"},
                          {"areaKey": "NG", "chsName": "????????????", "enName": "Nigeria", "pyFirst": "N"},
                          {"areaKey": "TT", "chsName": "????????????????????????", "enName": "Trinidad and Tobago",
                           "pyFirst": "T"},
                          {"areaKey": "CF", "chsName": "???????????????", "enName": "Central African Republic",
                           "pyFirst": "Z"},
                          {"areaKey": "PE", "chsName": "??????", "enName": "Peru", "pyFirst": "M"},
                          {"areaKey": "PG", "chsName": "?????????????????????", "enName": "Papua New Guinea",
                           "pyFirst": "B"},
                          {"areaKey": "CX", "chsName": "?????????", "enName": "Christmas Island", "pyFirst": "S"},
                          {"areaKey": "AN", "chsName": "????????????", "enName": "Netherlands Antilles",
                           "pyFirst": "A"},
                          {"areaKey": "BO", "chsName": "????????????", "enName": "Bolivia", "pyFirst": "B"},
                          {"areaKey": "IQ", "chsName": "?????????", "enName": "Iraq", "pyFirst": "Y"},
                          {"areaKey": "NP", "chsName": "?????????", "enName": "Nepal", "pyFirst": "N"},
                          {"areaKey": "BJ", "chsName": "??????", "enName": "Benin", "pyFirst": "B"},
                          {"areaKey": "VN", "chsName": "??????", "enName": "Vietnam", "pyFirst": "Y"},
                          {"areaKey": "NI", "chsName": "????????????", "enName": "Nicaragua", "pyFirst": "N"},
                          {"areaKey": "PW", "chsName": "????????????", "enName": "Palau", "pyFirst": "P"},
                          {"areaKey": "SO", "chsName": "?????????", "enName": "Somalia", "pyFirst": "S"},
                          {"areaKey": "SM", "chsName": "????????????", "enName": "San Marino", "pyFirst": "S"},
                          {"areaKey": "NR", "chsName": "??????", "enName": "Nauru", "pyFirst": "N"},
                          {"areaKey": "BN", "chsName": "??????", "enName": "Brunei Darussalam", "pyFirst": "W"},
                          {"areaKey": "MZ", "chsName": "????????????", "enName": "Mozambique", "pyFirst": "M"},
                          {"areaKey": "GR", "chsName": "??????", "enName": "Greece", "pyFirst": "X"},
                          {"areaKey": "TN", "chsName": "?????????", "enName": "Tunisia", "pyFirst": "T"},
                          {"areaKey": "RU", "chsName": "?????????", "enName": "Russian Federation",
                           "pyFirst": "E"},
                          {"areaKey": "MG", "chsName": "??????????????????", "enName": "Madagascar", "pyFirst": "M"},
                          {"areaKey": "NA", "chsName": "????????????", "enName": "Namibia", "pyFirst": "N"},
                          {"areaKey": "CQ", "chsName": "???????????????", "enName": "Equatorial Guinea",
                           "pyFirst": "C"},
                          {"areaKey": "SR", "chsName": "?????????", "enName": "Suriname", "pyFirst": "S"},
                          {"areaKey": "MU", "chsName": "????????????", "enName": "Mauritius", "pyFirst": "M"},
                          {"areaKey": "LA", "chsName": "??????", "enName": "Laos", "pyFirst": "L"},
                          {"areaKey": "US", "chsName": "??????", "enName": "United States", "pyFirst": "M"},
                          {"areaKey": "ST", "chsName": "?????????????????????????????????", "enName": "Sao Tome and Principe",
                           "pyFirst": "S"},
                          {"areaKey": "BM", "chsName": "???????????????", "enName": "Bermuda", "pyFirst": "B"},
                          {"areaKey": "LU", "chsName": "?????????", "enName": "Luxembourg", "pyFirst": "L"},
                          {"areaKey": "CR", "chsName": "???????????????", "enName": "Costa Rica", "pyFirst": "G"},
                          {"areaKey": "KR", "chsName": "??????", "enName": "South Korea", "pyFirst": "H"},
                          {"areaKey": "CZ", "chsName": "??????", "enName": "Czech Republic", "pyFirst": "J"},
                          {"areaKey": "MX", "chsName": "?????????", "enName": "Mexico", "pyFirst": "M"},
                          {"areaKey": "SH", "chsName": "???????????????", "enName": "St Helena", "pyFirst": "S"},
                          {"areaKey": "AO", "chsName": "?????????", "enName": "Angola", "pyFirst": "A"},
                          {"areaKey": "MN", "chsName": "??????", "enName": "Mongolia", "pyFirst": "M"},
                          {"areaKey": "VC", "chsName": "??????????????????????????????",
                           "enName": "Saint Vincent and the Grenadines", "pyFirst": "S"},
                          {"areaKey": "PH", "chsName": "?????????", "enName": "Philippines", "pyFirst": "F"},
                          {"areaKey": "SC", "chsName": "?????????", "enName": "Seychelles", "pyFirst": "S"},
                          {"areaKey": "CK", "chsName": "????????????", "enName": "Cook Islands", "pyFirst": "K"},
                          {"areaKey": "PK", "chsName": "????????????", "enName": "Pakistan", "pyFirst": "B"},
                          {"areaKey": "HR", "chsName": "????????????", "enName": "Croatia", "pyFirst": "K"},
                          {"areaKey": "TH", "chsName": "??????", "enName": "Thailand", "pyFirst": "T"},
                          {"areaKey": "SI", "chsName": "???????????????", "enName": "Slovenia", "pyFirst": "S"},
                          {"areaKey": "VG", "chsName": "?????????????????????", "enName": "British Virgin Islands",
                           "pyFirst": "Y"},
                          {"areaKey": "SY", "chsName": "???????????????????????????", "enName": "Syrian Arab Republic",
                           "pyFirst": "A"},
                          {"areaKey": "CY", "chsName": "????????????", "enName": "Cyprus", "pyFirst": "S"},
                          {"areaKey": "BR", "chsName": "??????", "enName": "Brazil", "pyFirst": "B"},
                          {"areaKey": "LB", "chsName": "?????????", "enName": "Lebanon", "pyFirst": "L"},
                          {"areaKey": "IS", "chsName": "??????", "enName": "Iceland", "pyFirst": "B"},
                          {"areaKey": "PA", "chsName": "?????????", "enName": "Panama", "pyFirst": "B"},
                          {"areaKey": "FM", "chsName": "??????????????????", "enName": "Micronesia", "pyFirst": "M"},
                          {"areaKey": "VA", "chsName": "?????????", "enName": "Vatican City State",
                           "pyFirst": "F"},
                          {"areaKey": "NC", "chsName": "??????????????????", "enName": "New Caledonia", "pyFirst": "X"},
                          {"areaKey": "MT", "chsName": "?????????", "enName": "Malta", "pyFirst": "M"},
                          {"areaKey": "BG", "chsName": "????????????", "enName": "Bulgaria", "pyFirst": "B"},
                          {"areaKey": "ES", "chsName": "?????????", "enName": "Spain", "pyFirst": "X"},
                          {"areaKey": "CI", "chsName": "????????????", "enName": "Ivory Coast", "pyFirst": "X"},
                          {"areaKey": "IE", "chsName": "?????????", "enName": "Ireland", "pyFirst": "A"},
                          {"areaKey": "BZ", "chsName": "????????????", "enName": "Belize", "pyFirst": "B"},
                          {"areaKey": "SZ", "chsName": "????????????", "enName": "Swaziland", "pyFirst": "S"},
                          {"areaKey": "SV", "chsName": "????????????", "enName": "EI Salvador", "pyFirst": "S"},
                          {"areaKey": "GE", "chsName": "????????????", "enName": "Georgia", "pyFirst": "G"},
                          {"areaKey": "SD", "chsName": "??????", "enName": "Sudan", "pyFirst": "S"},
                          {"areaKey": "PR", "chsName": "????????????", "enName": "Puerto Rico", "pyFirst": "B"},
                          {"areaKey": "FJ", "chsName": "??????", "enName": "Fiji", "pyFirst": "F"},
                          {"areaKey": "NL", "chsName": "??????", "enName": "Netherlands", "pyFirst": "H"},
                          {"areaKey": "UG", "chsName": "?????????", "enName": "Uganda", "pyFirst": "W"},
                          {"areaKey": "HU", "chsName": "?????????", "enName": "Hungary", "pyFirst": "X"},
                          {"areaKey": "TC", "chsName": "???????????????????????????", "enName": "Turks and Caicos Islands",
                           "pyFirst": "T"}]}
