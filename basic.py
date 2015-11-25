import urllib2
import requests
from bs4 import BeautifulSoup
import wget 
import gevent
import gevent.monkey 
gevent.monkey.patch_all()

url = "http://xkcd.com/{index}/"

def worker(index):
    response = urllib2.urlopen(url.format(index=index)).read()
    soup = BeautifulSoup(response, "lxml")
    a = soup.find(id='comic')
    b = a.find_all("img")
    print "http:"+b[0]['src']
    wget.download("http:"+b[0]['src'],"/Users/poorvakkapoor/GitHub/new_dir/scrapper/images")
    print "number of files downloaded", index

def threads():
  thread_list = []
  index = 1
  while (urllib2.urlopen(url.format(index=index)).getcode() != 404 and index != 404):
      thread_list.append(gevent.spawn(worker,index))
      if index%100 == 0:
          print thread_list
          gevent.joinall(thread_list)
          thread_list = []
      index += 1

if __name__  == '__main__':
  threads()
  

