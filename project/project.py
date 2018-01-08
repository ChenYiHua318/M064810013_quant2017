
# coding: utf-8

# In[6]:


import requests
import re
import random
import configparser
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


# In[7]:


app = Flask(__name__)


# In[8]:


#line_bot_api = LineBotApi('gEd5m4sXZAnpxQ3qYdncBsx5zq0Hw9SyZkpSnfrr4DuutHtW1btEjuJ04+cu2k2yp9wNDPrdU1luU4Kq+vOykCsRmQm1E3YYP0037puK9EMRZFkBl4PFGmpv1Zq2m4jF2QWtIlAK0edGHxmpQnoFngdB04t89/1O/w1cDnyilFU=')
#handler = WebhookHandler('b7e44ac55197b90ef44413e52768c000')
line_bot_api = LineBotApi('gEd5m4sXZAnpxQ3qYdncBsx5zq0Hw9SyZkpSnfrr4DuutHtW1btEjuJ04+cu2k2yp9wNDPrdU1luU4Kq+vOykCsRmQm1E3YYP0037puK9EMRZFkBl4PFGmpv1Zq2m4jF2QWtIlAK0edGHxmpQnoFngdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b7e44ac55197b90ef44413e52768c000')
client_id = ('maggie2009612@gmail.com')
client_secret = ('Maggie3183399168')


# In[9]:


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'ok'

def pattern_mega(text):
    patterns = ['mega', 'mg', 'mu', 'ＭＥＧＡ', 'ＭＥ', 'ＭＵ','ｍｅ', 'ｍｕ', 'ｍｅｇａ', 'GD', 'MG', 'google',]
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
        
def topvip():
    target_url = 'https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010101/TS0201010101/index.htm'
    print('Start parsing 頂級尊榮....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for index,data in enumerate(soup.select('h3.fs15 a')):
        if index==15:
            return content
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content

def sunrose():
    target_url = 'https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010101/TS0201010102/index.htm'
    print('Start parsing 太陽玫瑰....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for index,data in enumerate(soup.select('h3.fs15 a')):
        if index==15:
            return content
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content

def depart():
    target_url = 'https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010101/TS0201010103/index.htm'
    print('Start parsing 百貨量販....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for index,data in enumerate(soup.select('h3.fs15 a')):
        if index==15:
            return content
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content

def mobile():
    target_url = 'https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010101/TS0201010104/index.htm'
    print('Start parsing 行動生活....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for index,data in enumerate(soup.select('h3.fs15 a')):
        if index==15:
            return content
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content

def article():
    target_url = 'https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010101/TS0201010105/index.htm'
    print('Start parsing 人文知性....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for index,data in enumerate(soup.select('h3.fs15 a')):
        if index==15:
            return content
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content

def visa_intro():
    target_url = 'https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010103/index.htm'
    print('Start parsing visa金融卡_卡片介紹....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for index,data in enumerate(soup.select('h3.fs15 a')):
        if index==15:
            return content
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content

def visa_know():
    target_url = 'https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010103/index.htm'
    print('Start parsing visa金融卡_用卡須知....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for index,data in enumerate(soup.select('div.listbox ul h3 a')):
        if index==15:
            return content
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content

def creditserve():
    target_url = 'https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010104/index.htm'
    print('Start parsing 商戶收單服務....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for index,data in enumerate(soup.select('div.listbox ul h3 a')):
        if index==15:
            return content
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content


# In[ ]:


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print('event.reply_token',event.reply_token)
    print("event.message.text:", event.message.text)
    if event.message.text == "頂級尊榮":
        content = topvip() 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0
    if event.message.text == "太陽玫瑰":
        content = sunrose() 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0
    if event.message.text == "百貨量販":
        content = depart() 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0
    if event.message.text == "行動生活":
        content = moblie() 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0
    if event.message.text == "人文知性":
        content = article() 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0   
    if event.message.text == "visa金融卡_卡片介紹":
        content = visa_intro() 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0
    if event.message.text == "visa金融卡_用卡須知":
        content = visa_know() 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0
    if event.message.text == "商戶收單服務":
        content = creditserve() 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0
    
    
    if event.message.text == "信用卡介紹":
        buttons_template = TemplateSendMessage(alt_text='信用卡介紹 template',
                                               template=ButtonsTemplate(title='選擇卡種',text='請選擇',
                                                                        thumbnail_image_url='https://i.imgur.com/oeMEirX.jpg',
                                                                        actions=[MessageTemplateAction(label='頂級尊榮',text='頂級尊榮'),
                                                                                 MessageTemplateAction(label='太陽玫瑰',text='太陽玫瑰'),
                                                                                 MessageTemplateAction(label='百貨量販',text='百貨量販'),
                                                                                 MessageTemplateAction(label='行動生活',text='行動生活'),
                                                                                 MessageTemplateAction(label='人文知性',text='人文知性')]))
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0

    
    if event.message.text == "VISA金融卡":
        buttons_template = TemplateSendMessage(alt_text='VISA金融卡 template',
                                               template=ButtonsTemplate(title='選擇服務',text='請選擇',
                                                                        thumbnail_image_url='https://i.imgur.com/ayjQVPm.png',
                                                                        actions=[MessageTemplateAction(label='visa金融卡_卡片介紹',text='visa金融卡_卡片介紹'),
                                                                                 MessageTemplateAction(label='visa金融卡_用卡須知',text='visa金融卡_用卡須知')]))
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    if event.message.text == "商戶收單服務":
        buttons_template = TemplateSendMessage(alt_text='商戶收單服務 template',
                                               template=ButtonsTemplate(title='選擇服務',text='請選擇',
                                                                        thumbnail_image_url='https://i.imgur.com/hfvRaU5.jpg',
                                                                        actions=[MessageTemplateAction(label='商戶收單服務',text='商戶收單服務')]))
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0  
    

    if event.message.text == "信用卡":
        buttons_template = TemplateSendMessage(alt_text='信用卡 template',
                                               template=ButtonsTemplate(title='選擇服務',text='請選擇',
                                                                        thumbnail_image_url='https://i.imgur.com/PZt0ijH.png',
                                                                        actions=[MessageTemplateAction(label='信用卡介紹',text='信用卡介紹'),
                                                                                 URITemplateAction(label='信用卡權益',uri='https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010102/index.htm'),
                                                                                 MessageTemplateAction(label='VISA金融卡',text='VISA金融卡'),
                                                                                 MessageTemplateAction(label='商戶收單服務',text='商戶收單服務'),
                                                                                 URITemplateAction(label='ApplePay',url='https://mkp.taishinbank.com.tw/TsCms/marketing/expose/WM_20171123163746660/index.html'),
                                                                                 URITemplateAction(label='SamsungPay',uri='https://mkp.taishinbank.com.tw/TsCms/marketing/expose/WM_20170831104709577/index.html'),
                                                                                 URITemplateAction(label='AndroidPay',uri='https://mkp.taishinbank.com.tw/TsCms/marketing/expose/WM_20170928144417314/index.html')]))
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    
    
    buttons_template = TemplateSendMessage(alt_text='目錄 template',
                                           template=ButtonsTemplate(title='選擇服務',text='請選擇',
                                                                    thumbnail_image_url='https://i.imgur.com/iq7eFeI.jpg',
                                                                    actions=[MessageTemplateAction(label='個人金融',text='個人金融'),
                                                                             URITemplateAction(label='微型企業',uri='https://www.taishinbank.com.tw/TS/TS03/index.htm'),
                                                                             URITemplateAction(label='法人金融',uri='https://www.taishinbank.com.tw/TS/TS04/index.htm'),
                                                                             URITemplateAction(label='海外分子行',uri='https://www.taishinbank.com.tw/TS/TS05/index.htm')]))
    line_bot_api.reply_message(event.reply_token, buttons_template)


# In[ ]:


if __name__ == '__main__':
    app.run()

