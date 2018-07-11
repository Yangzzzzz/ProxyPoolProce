import re
from Testting import Testting
import requests


class Getter:
    def __init__(self):
        pass

    def getByNiMing(self):
        result = []
        for i in range(1, 4):
            res = requests.get('https://www.kuaidaili.com/free/inha/{}/'.format(i))
            pat = re.compile('<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(.*)</td>')
            array = pat.findall(res.text)
            for path, port in array:
                testting = Testting()
                proPath = path + ':' + port
                proPath = proPath.replace(' ', '')
                rsp = testting.check(proPath)
                if rsp == True:
                    result.append(proPath)


if __name__ == '__main__':
    getting = Getter()
    result = getting.getByNiMing()
    print(result)
