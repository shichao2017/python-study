#coding=utf-8  
import re  
import urllib.request  

def getHtml(url):  
    page = urllib.request.urlopen(url)  
    html = page.read()  
    html = html.decode('utf-8')  
    return html  
  
def getItem(html):  
    reg = re.compile(r'.*?<span class="title">(.*?)</span>.*?<p class="">.*?(\d+).*?</p>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span>(\d+)人评价',re.S)  
    items = re.findall(reg,html)  
    global index  
    for index,item in enumerate(items,index+1):  
        print (index,item)  
  
       
if __name__=='__main__':  
    index = 0  
    for i in range(0,226,25):  
        url  = "https://movie.douban.com/top250?start="  
        url += str(i) + "&filter="  
        html = getHtml(url)  
        getItem(html)  
  
    print ("\nOK!All OVER!")  
