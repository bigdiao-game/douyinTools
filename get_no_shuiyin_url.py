# encoding=utf-8
import json
import re

import requests

USER_AGENT = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/66.0.3329.0 Mobile Safari/537.36 '


def getNoShuiYinUrl(url):
    response = requests.get(url)
    uq = re.findall('video/(\\d+)/', str(response.url))[0]
    urlEx = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={uq}'
    response2 = requests.get(urlEx).text
    toJson = json.loads(response2)
    urlRet = str(toJson['item_list'][0]['video']['play_addr']['url_list'][0]).replace('playwm', 'play')
    return urlRet


if __name__ == '__main__':
    //test url
    result = getNoShuiYinUrl('https://v.douyin.com/JYNyMo6/')
    print(result)
