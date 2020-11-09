from datetime import datetime, date
from time import time, sleep

import asyncio
from pymongo import collection
from api_controller import ApiRequest
from mongo_controller import MongoController

class LoggicModel(ApiRequest, MongoController):
    """docstring"""

    def __init__(self) -> None:
        """[summary]"""
        ApiRequest.__init__(self)
        MongoController.__init__(self)

    def __get_date(self) -> list:
        """Get date of system

        Returns:
            list: [0]today aaaa-mm-dd, [1]time h:m:s:ms, [2]today_str dd-mm-aaaa
        """
        date = datetime.now()
        today_str = date.strftime('%d-%m-%Y')
        today = date.date()
        time = date.time()

        return [today, time, today_str]

    def get_data_by_date(self) -> dict:
        """Connect to mongo atlas and find data by date

        Returns:
            dict: {'data': data if exit else None }
        """
        date = self.__get_date()[0].isoformat()
        try:
            response = self.mongo['collection'].find_one({'date': date})
        except Exception as err:
            self.mogo['client'].close()
            return {'data': False}

        return {'data': response}

    def prepare_response(self) -> dict:
        """Get data from api's and save data in mongo atlas

        Returns:
            dict: indicators from three api, trm,, uf, utm
        """
        try:
            res = self.__get_api_data()
            response = {
                'date': self.__get_date()[0].isoformat(),
                'indicators': {
                    'dolar': res['convert']['vl'],
                    'uf': res['uf']['serie'][0]['valor'],
                    'utm': res['utm']['serie'][0]['valor']
                }
            }
            # save an copy for not add _id to origin object
            self.db_save(response.copy())
        except Exception as err:
            response = {'data': False}

        return {'data': response}

    def __get_api_data(self) -> dict:
        #start_time = time()
        utm = self.indicator_utm()
        convert = self.converter()
        uf = self.indicator_uf()
        return {
            'convert': convert,
            'utm': utm,
            'uf': uf
        }
        #stop_time = time()
        #print(stop_time - start_time)
