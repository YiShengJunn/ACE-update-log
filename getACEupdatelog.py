import requests
from datetime import datetime, timedelta

yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
CHECK_UPDATE_URL = "https://as-api.tdacestudio.com/api/as/conf/version?is_apple_chip=0"
HEADERS = { "User-Agent": "win;1.9.0;windows-10;1201787499",
           "platform":"win",
            "device": "windows-10",
            "version":"1.9.0",
            "channel":"general",
            "lan":"CHN"}
respone = requests.get(CHECK_UPDATE_URL, headers=HEADERS).json()
title = respone["data"]["tip"]["title"]
content = respone["data"]["tip"]["content"].rstrip()

readme_onlyr = open("README.md","r",encoding="utf-8")
readme = open("README.md","a+",encoding="utf-8")
if title in readme_onlyr.read():
    pass
else:
    readme.write("\n## "+title+"\n**更新日期："+yesterday+"**  \n"+content)
    readme.close()