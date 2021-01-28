from instagram_private_api import Client, ClientCompatPatch
import requests


BotToken = '1633415315:AAE5UXzuUpQW9LlekvNVFsbMHUdWsV9TX74'

global requestURL
requestURL = 'http://api.telegram.org/bot' + BotToken + '/getUpdates'

ResultRaw = requests.get(requestURL)
Result = ResultRaw.json()

print(Result)