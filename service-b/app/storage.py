import os
import redis
from dotenv import load_dotenv
load_dotenv()

class RedisDb:
    def __init__(self) -> None:
        self.host = str(os.getenv("REDIS_HOST"))
        self.port = int(os.getenv("REDIS_PORT", 6379))

    def get_connection(self):
        self.conn = redis.Redis(host=self.host, port=self.port , decode_responses=True)
        
    def closdb(self):
        self.conn.close()

    def set_cordinat_to_db(self, key, value):
        self.conn.set(key, value)

    def get_item(self, name):
        self.conn.get(name)

    def get_all(self):
        pass

   

