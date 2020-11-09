from decouple import config
from pymongo import MongoClient
from pymongo import collection
from urllib3 import response


# Import environ var from conect to Mongo Atlas
CLUSTER = config('CLUSTER')
DBNAME = config('DBNAME')
PASWORD = config('PASWORD')
USER = config('USER')
URL = f'mongodb+srv://{USER}:{PASWORD}@{CLUSTER}/{DBNAME}?retryWrites=true&w=majority'


class MongoController(object):
    """
    docstring
    """

    def __init__(self) -> None:
        self.mongo = self.__db_conect('indicadores')

    def __db_conect(self, _collection=None, db_name=DBNAME,) -> dict:
        """Connet to mongo atlas cluster

        Args:
            _collection (str): name of collection to find. Defaults to None.
            db_name (str): db name. Defaults to DBNAME.

        Returns:
            dict: {connet: bool, collection: mongo collection, client: mongo client}
        """
        if (db_name and _collection):
            # Connet to mongo atlas
            client = MongoClient(URL)
            # Connet to bd specific
            db = client[db_name]
            # Return especific collection and the client
            response = {
                'collection': db[_collection],
                'client': client
            }
            return response

    def db_save(self, data=None):
        """Save one data in mongo db

        Args:
            data (dict): dato to record in db. Defaults to None.
        """
        if (data):
            self.mongo['collection'].insert_one(data)
            self.mongo['client'].close()