# -*- coding:utf-8 -*-

import re
import requests
def downloadPic(html,keyword):
    jpg_url=re.findall('"objURL":"(.*?)",',html,re.S)
    i=0
    print('找到关键字:'+keyword+'的图片，现在开始下载图片...')
    for each in jpg_url:
        print('正在下载第'+str(i+1)+'张图片，图片地址:'+str(each))
        try:
            jpg = requests.get(each,timeout = 10)
        except requests.exceptions.ConnectionError:
            print('[错误] 当前图片无法下载')
            continue
        string = keyword+'_'+str(i+1)+'.jpg'
        fp = open(string,'wb')
        fp.write(jpg.content)
        fp.close()
        i+=1

if __name__ == '__main__':
    word = input("输入关键字:")
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn=200&gsm=0&ct=&ic=0&lm=-1&width=0&height=0'
    result=requests.get(url)
    downloadPic(result.text,word)
