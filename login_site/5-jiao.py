#coding:utf8
'''
Created on 2018.10.25

@author: dell
'''
from bs4 import BeautifulSoup
import requests
import time
import xlwt
import requests
import os
 
urls = list(range(30))
for i in range(len(urls)):
    urls[i]='http://list.iqiyi.com/www/1/-6------------24-'+str((i+1))+'-1-iqiyi--.html'
def get_webData(url):
    data_info = []
    time.sleep(3)
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div.site-piclist_info > div.mod-listTitle_left > p > a')
    imgs = soup.select('div.site-piclist_pic > a > img')
    actors = soup.select('div.site-piclist_info > div.role_info')
    spans = soup.select('div.site-piclist_info > div.mod-listTitle_left > span')
    for title,img,actors,span in zip(titles,imgs,actors,spans):
        data = {
                'title':title.get_text(),
                'img':str("D://pics//"+str(title.get_text())+".jpg"),
                'actors':list(actors.stripped_strings),
                'span':span.get_text()
                }
        #print(data)
        dataVal_list.append(data.values())
        data_info.append(data)
    #print(list(data.keys()))
    for m,n in enumerate(list(data.keys())):
        sheet.write(0,m,n)
              
    for i,p in enumerate(dataVal_list):
        for j,q in enumerate(p):
            #print(q)
            sheet.write(i+1,j,q)
     
    for title,img in zip(titles,imgs):
        url="http:"+str(img.get('src'))
        root="D://pics//"
        name=title.get('title')
        path=root+name+'.jpg'
        print(path)
        try:
            if not os.path.exists(root):
                os.mkdir(root)          
            if not os.path.exists(path):
                r=requests.get(url)
                with open(path,'wb')as f:
                    f.write(r.content)
                    f.close()
                    print("文件保存成功")
            else:
                print("文件已存在")
        except:
            print("爬取失败")
             
    return data_info
def main():
    for url in urls:
        data_info = get_webData(url)
        #print(data_info)
        print('---------------------------\n')
  
if __name__ == '__main__':
    f = xlwt.Workbook(encoding='utf-8')
    sheet = f.add_sheet('Movies','cell_overwrite_ok=True')
    dataVal_list=[]
    main()
    f.save('Movies.xls')