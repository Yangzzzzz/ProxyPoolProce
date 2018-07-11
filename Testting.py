import requests
from setting import TEST_OUT

testpath = 'http://www.baidu.com/'


class Testting:
    def __init__(self):
        pass

    def check(self, proxypath):
        proxy = {
            'http': 'http://' + proxypath
        }
        try:
            print('test ：'+proxypath)
            res = requests.get(testpath, proxies=proxy, timeout=TEST_OUT)
        except Exception as e:
            print('ip：' + proxypath + ' is bad')
            return False
        if res.status_code != 200:
            return False
        print('ip：' + proxypath + ' sucess!')
        return True


if __name__ == '__main__':
    testting = Testting()
    testting.check('115.218.122.11:9000')
