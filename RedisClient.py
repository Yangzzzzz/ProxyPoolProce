import redis
from setting import HOST, PORT, PASSWORD, PROXY_NAME


class RedisClient:
    def __init__(self):
        self.connt = redis.Redis(host=HOST, port=PORT, password=PASSWORD)

    def get(self):
        result = self.connt.lpop(PROXY_NAME)
        return result

    def add(self, prostr):
        self.connt.rpush(PROXY_NAME, prostr)

    def pop(self, cnt=1):
        length = self.connt.llen(PROXY_NAME)
        if cnt >= length:
            cnt = length
        result = self.connt.lrange(PROXY_NAME, 0, cnt - 1)
        self.connt.ltrim(PROXY_NAME, cnt, -1)
        return result


if __name__ == '__main__':
    client = RedisClient()
    client.add('yyyy')
    s = client.get()
    client.add(1)
    client.add(2)
    client.add(3)
    s = client.pop()
    print(s)
