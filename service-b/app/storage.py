import os
import redis
from dotenv import load_dotenv
load_dotenv()

class RedisDb:
    def __init__(self) -> None:
        self.host = str(os.getenv("REDIS_HOST"))
        self.port = int(os.getenv("REDIS_PORT", 6379))
        self._conn = None
        self._pool = redis.ConnectionPool(
            host=self.host,
            port=self.port,
            decode_responses=True
        )
        self._conn = None

    def connect(self):
        if self._conn is None:
            self._conn = redis.Redis(connection_pool=self._pool)
        return self._conn

    def clos(self):
        if self._conn:
            self._conn.close()
            self._conn = None
            

    def set_data_to_db(self, key, value):
        self.connect()
        if self._conn:
            return self._conn.set(key, value)
        else:
            print({"yehuda error":"RedisDb.conn Not enabled"})
            return False
        
    def get_item(self, name):
        self.connect()
        if self._conn:
            return self._conn.get(name)
        else:
            print({"yehuda error":"RedisDb.conn Not enabled"})
            return False
        
    def get_all(self):
        self.connect()
        if self._conn:
            all_data = {}
            for key in self._conn.scan_iter():
                all_data[key] = self._conn.get(key)
            return all_data
        else:
            return {"yehuda error":"RedisDb._conn Not enabled"}












