import requests
import json
import re
import qqlolapi.exceptions

def call(url, params={}):
    answer = requests.get(url, params=params)
    data_string = re.sub("^var[\s\S]*=", "", answer.text)
    if data_string[-1:] == ";":
        data_string = data_string[:-1]
    data = json.loads(data_string)
    if data['status'] == "-1":
        raise qqlolapi.exceptions.APIError(data['msg'], data['status'])
    return data['msg']