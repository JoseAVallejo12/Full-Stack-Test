import json
from datetime import datetime
from urllib3 import PoolManager, Retry, Timeout



class ApiRequest (object):
    """
    docstring
    """

    def __init__(self):
        pass

    def converter(self, _from='USD', _to='CLP', valor=1):
        """Convert divices _from _to

        Args:
            _from (str, optional): device origin. Defaults to 'USD'.
            _to (str, optional): device equivalent. Defaults to 'CLPPP'.
            valor (int, optional): value to conver. Defaults to 1.

        Returns:
            [dict]: [equivalent values]
        """
        # validate type of var input, and make req to api usin private method
        if isinstance(_from, str) and isinstance(_to, str) and isinstance(valor, int):
            if valor <= 0:
                valor = 1
            opt = {
                'url': f'https://currency26.p.rapidapi.com/convert/{_from}/{_to}/{valor}',
                'method': 'GET',
                'headers': {
                    'x-rapidapi-key': "3d672ba603mshca2232c62c367d0p141c76jsna233dacaa78f",
                    'x-rapidapi-host': "currency26.p.rapidapi.com"
                }
            }
            return self.__request_api(opt)
        else:
            return {'Fail': 'Type of var incorrect'}

    def indicator_utm(self, _date='15-10-2020') -> dict:
        """Get UTM indicators form api goberment chile

        Args:
            _data (str, DD-MM-AAAA): data format. Defaults to '15-10-2020'.

        Returns:
            dict: response from api
        """
        # Validate date before to sent req
        validate_date = self.__validate_data(_date)
        if validate_date.get('state'):
            opt = {
                'url': f'https://mindicador.cl/api/utm/{_date}',
                'method': 'GET',
                'headers': {}
            }
            return self.__request_api(opt)
        else:
            return validate_date.get('fail')

    def indicator_uf(self, _date='15-10-2020') -> dict:
        """Get Indicators form api goberment chile

        Args:
            _data (str, DD-MM-AAAA): data format. Defaults to '15-10-2020'.

        Returns:
            dict: response from api
        """
        # Validate date before to sent req
        validate_date = self.__validate_data(_date)
        if validate_date.get('state'):
            opt = {
                'url': f'https://mindicador.cl/api/uf/{_date}',
                'method': 'GET',
                'headers': {}
            }
            return self.__request_api(opt)
        else:
            return validate_date.get('fail')

    def __request_api(self, options={}) -> dict:
        """Sent request to diferent data point

        Args:
            options (dict, optional): options to sent req. Defaults to {}.

        Returns:
            dict: response of api
        """
        url = options.get('url')
        headers = options.get('headers')
        method = options.get('method')

        # Set default timeout to 5 second and retries to 3 using urllib3 PoolManager
        retries = Retry(connect=3, read=3, redirect=3)
        timeout = Timeout(connect=5.0, read=5.0)
        http = PoolManager(retries=retries, timeout=timeout)

        # Sent req to api especific
        try:
            response = http.request(url=url, headers=headers, method=method)
        except Exception as err:
            return {'Error': err }

        return json.loads(response.data.decode('utf-8'))


    def __validate_data(self, date=''):
        """Validate Data

        Args:
            data (str): DD-MM-AAA. Defaults to ''.

        Returns:
            bool: True or False
        """

        if type(date) is str:
            try:
                datetime.strptime(date, '%d-%m-%Y')
                return {'state': True}
            except ValueError:
                return {'fail': {'error': 'Date incorrect must be dd-mm-aaa'}, 'state': False}
        return {'fail': {'error': 'Date must be str type dd-mm-aaa'}, 'state': False}
