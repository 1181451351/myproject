import requests


url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'i':'我和你都是中国',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'15875308503027',
    'sign':'14518738cadbeb44b9bdcc5e12354ec2',
    'ts':'1587530850302',
    'bv':'550b1abd7c280f7ac4cb663554d438e6',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
}
requests.post(url,form_data)