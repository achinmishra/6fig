from pymongo import MongoClient
from pprint import pprint


class MongoDBHandler:
    def __init__(self):

        self._client = MongoClient('localhost', 27017)
        self._db = None

    def _get_db_handle(self):
        self._db = self._client.admin

    def check_server_status(self):
        self._get_db_handle()
        if self._db is not None:
            serverstatusresult = self._db.command("serverStatus")
        else:
            print("Log DB Get handle error")
            return
        pprint(serverstatusresult)