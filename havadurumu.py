#döviz kurları kodunu inceleyiniz!
from selenium import webdriver  #sayfayı açmak içindir
import time  #assayfa yüklenmesi sırasında bekleme yapmak için
from bs4 import BeautifulSoup   #sayfa içerisinde ki sadece ilgili kısımları bulup almak için
browser=webdriver.Chrome()  #chrome aracılığılya ilgili siteye bağlanılacağı belirtildi.
browser.get("https://tr.freemeteo.com/havadurumu/iskenderun/7-days/list/?gid=311111&language=turkish&country=turkey")
html = browser.page_source      
time.sleep(2)
soup = BeautifulSoup(html, 'html.parser')
ilkParca=soup.find("div",{"class": "today sevendays"})   #sayfada bulmasını isteiğimiz kısım.sayfada 1 tane olduğu için find_all değilde find yazıldı.
bilgiler=ilkParca.find_all("div",{"class": "hover"})

for bilgi in bilgiler:   
    tarih=bilgi.find_all("div",{"class": "title"})
    tarihler = ((str(tarih).split("<span>",2)[1]).split("<",1)[0])
    asgariDerece = bilgi.find_all("div",{"class": "temps"})
    derece=((str(asgariDerece).split("<span>",1))[1].split("<",1))[0]
    print(tarihler+"="+derece)
    
browser.close()