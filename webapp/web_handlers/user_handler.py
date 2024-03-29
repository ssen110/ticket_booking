from flask import jsonify
from webapp.web_handlers import base_handler
from common_package.vo import json_result_vo
from common_web_api.helpers import user_helper


class UserHandler(base_handler.BaseHandler):
    def get_user_details(self):
        data = dict()
        message = None
        try:
            user_id = self.get_request("user_id")
            result = user_helper.UserHelper().get_user_details(int(user_id))
            data["data"] = result.serialize()
            message = "Success"
        except Exception as e:
            message = self.get_log_message('Got exception on UserHandler: get_user_details')
        finally:
            json_result = json_result_vo.JsonresultVo(data, message)
            return jsonify(json_result.serialize())

    def save_user_details(self):
        data = dict()
        message = None
        try:
            email_id = self.get_request("email_id")
            name =  self.get_request("user_name")
            user_helper.UserHelper().save_user_details(email_id, name)
        except Exception as e:
            message = self.get_log_message('Got exception on UserHandler: save_user_details')
        finally:
            json_result = json_result_vo.JsonresultVo(data, message)
            return jsonify(json_result.serialize())
