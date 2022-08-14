#login_api.py
from base.http_client import HttpClient
# 继承HttpClient
class advisor(HttpClient):

    def advisor_get(self, **kwargs):
        return self.post('https://h5.qhkyfund.com/fi-mall-fundcustomer-server-v3/advisor/get','',{"user_id": "0000161815", "funcNo": 6857902})
# 实例化Auth类
advisor =advisor()