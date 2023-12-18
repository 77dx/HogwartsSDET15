import pytest
name = "conftest"

@pytest.fixture(autouse=False, scope='module',params=['tom','jane'])     # 可获取yield返回值, autouse=True默认所有都执行
def login(request):
    print('调用登陆，获取token')
    username = request.param
    yield {'username':username}    # 相当于return
    print('登出')



def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')