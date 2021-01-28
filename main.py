from instagram_private_api import Client, ClientCompatPatch
import requests
import json

BotToken = '1633415315:AAE5UXzuUpQW9LlekvNVFsbMHUdWsV9TX74'

global requestURL
requestURL = 'http://api.telegram.org/bot' + BotToken + '/getUpdates'


def GatherPost(messages):
    messages = json.dumps(messages)
    json_messages = json.loads(messages)

    result = json_messages['result']




    print(result)


def GetTelegramMessages():
    resultraw = requests.get(requestURL)
    result = resultraw.json()
    return result


GatherPost(GetTelegramMessages())
