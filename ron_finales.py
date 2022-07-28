import requests
import json


def to_gateway(api_url, input_param):
    response = requests.post(api_url, data=json.dumps(input_param))
    # pdb.set_trace()
    print(response)