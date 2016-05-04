import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"}
res = requests.get("http://www.xinshipu.com/zuofa/163906",headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
block = soup.select(".re-up")[0] #先把整個區塊截取出來
name = block.select(".font18.no-overflow")[0].text
grade = block.select(".font16.ml10.col")[0].text
grade2 = block.select(".font16.ml10.col")[1].text
info = block.select(".cg2.mt12")
receipenum = block.select(".cg2.mt12 span:nth-of-type(2)")[0].text
readtimes = block.select(".cg2.mt12 span:nth-of-type(4)")[0].text
collecttimes = block.select(".cg2.mt12 span:nth-of-type(2)")[0].text
#print(block)
print("食譜名稱:%s"%name)
print("評分:%s,%s"%(grade,grade2))
print("食譜號:%s"%receipenum)
print("閱讀次數:%s"%readtimes)
print("收藏次數:%s"%collecttimes)