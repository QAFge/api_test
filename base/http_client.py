import json as _json
import requests
from  utils.logger import  logger


class HttpClient():
    # 接口做post一般都是采用json格式进行提交
    __headers =  {'Accept':'application/json,text/plain,*/*',
                  'Accept-Encoding':'gzip,deflate,br',
                  'Accept-Language':'zh-CN,zh;q=0.9',
                  'Cache-Control':'no-cache',
                  'Connection':'keep-alive',
                  'Content-Length': '53',
                  'Content-Type': 'application/json',
                  'Host': 'h5.qhkyfund.com',
                  'Origin': 'https://h5.qhkyfund.com',
                  'Pragma': 'no-cache',
                  'Referer': 'https://h5.qhkyfund.com/lcsm/mall/index',
                  'Sec-Fetch-Dest': 'empty',
                  'Sec-Fetch-Mode': 'cors',
                  'Sec-Fetch-Site': 'same-origin',
                  'timestamp': '1660455380794',
                  'tk-token-authorization': 'MALLTRADE 7d68723f624a451a9d2d188baf8bd755',
                  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

    def __init__(self):
        self.__session = requests.session()

    def get(self, path, **kwargs):
        return self.__request(path, 'GET', **kwargs)

    def post(self, path, data=None, json=None, **kwargs):
        return self.__request(path, 'POST', data, json, **kwargs)

    def __request(self, url, method, data=None, json=None, **kwargs):
        headers = kwargs.get("headers")
        params = kwargs.get("params")
        # 如果传入header不为空，那么更新header
        if headers:
            self.__headers.update(headers)
        self.__request_log(url, method, data, json, params, self.__headers)
        resp = None
        if method == "GET":
            resp = self.__session.get(url, **kwargs)
        elif method == "POST":
            resp = requests.post(url, data, json, **kwargs)
        self.__response_log(resp)
        return resp

    def __request_log(self, url, method, data=None, json=None, params=None, headers=None):
        logger.info("接口请求地址: {}".format(url))
        logger.info("接口请求方式: {}".format(method))
        logger.info("接口请求头: {}".format(_json.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("接口请求 params 参数: {}".format(_json.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 : {}".format(_json.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 json 参数: {}".format(_json.dumps(json, indent=4, ensure_ascii=False)))

    def __response_log(self, resp):
        try:
            logger.info("返回信息 : {}".format(resp.text, ensure_ascii=False))
        except Exception as e:
            logger.error('系统错误：{}'.format(e))
