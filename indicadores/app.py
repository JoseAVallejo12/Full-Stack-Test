import json
import datetime
from loggic_model import LoggicModel



def lambda_handler(event, context):
    """Main funtion lambda

    Args:
        event (dict): event inf trigger the lambda
        context (srt): inf

    Returns:
        json: indicators
    """
    model = LoggicModel()
    # Get data from mongo atlas if this to be, else get from API
    res = model.get_data_by_date().get('data')
    status = 200
    if res:
        response = {
            'date': res.get('date'),
            'indicators': res.get('indicators')
        }
        print(f'From Mongo: {response}')

    else:
        res2 = model.prepare_response().get('data')
        if res2 is True:
            response = res2
        else:
            status = 400
            response = {
                'mongo': 'data not found en db',
                'api': 'One o more call to api fail'
            }

        print(f'From Api: {response}')

    #print(f'Data Log save: {response}')
    return {
        "statusCode": status,
        "body": {
            "message": response,
            # "location": ip.text.replace("\n", "")
        },
    }

#lambda_handler({}, 'context')