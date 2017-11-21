
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
import urllib.parse
import urllib.request
import json

print('=============================================')
print('5. upload the apk')
print('=============================================')

requestUrl = 'http://api.fir.im/apps'
formData = {'type':'android','bundle_id':'com.com.baiiu.zhihudaily','api_token':'05ecd7ec7bc11ca209752fdaeb2f8cb6'}
formDataEncoded = urllib.parse.urlencode(formData).encode(encoding='utf-8')
request = urllib.request.Request(requestUrl,formDataEncoded)
response = urllib.request.urlopen(request)
responseText = response.read().decode('utf-8')
# print(responseText)
data = json.loads(responseText)
icon = data['cert']['icon'];
binary = data['cert']['binary']
# print(icon['key'])
# print(binary['key'])


def uploadResource(key,token,name,version,build):
