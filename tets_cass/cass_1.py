# cass_1.py

import pytest
import allure
import ddt
from cass_api.login_api import auth_1
from cass_api.advisor_get_api import advisor

@allure.feature('登录')
def test_01():
    response = auth_1.login()
    #print(response)
    assert response.json().get('code') == 0
    tonken= response.headers.get('tk-token-authorization') #获取响应有token
    response_advisor = advisor.advisor_get(headers={'tk-token-authorization':tonken})
    assert response_advisor.json().get('code') == 0
if __name__ == '__main__':
    pytest.main()
