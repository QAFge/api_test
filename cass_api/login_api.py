#login_api.py
from base.http_client import HttpClient
# 继承HttpClient
class Auth(HttpClient):
    def login(self, **kwargs):
        return self.post('https://h5.qhkyfund.com/fi-mall-fundcustomer-server-v3/userLogin/login','',{"login_type":2,"login_value":"13480620409","password":"TeMnp90Z73qCDinCsH0gTWIWCzGcuyOioPRUTc2CZg31l1Pp/L6CKQrDMaFtWAzPz/H2AkIz8nxyo/uITToXeA==","id_type":0,"ip":" ","user_type":1,"device_mac":" ","device_name":" ","funcNo":3057712},headers={'tk-token-authorization':''})
# 实例化Auth类
auth_1 =Auth()