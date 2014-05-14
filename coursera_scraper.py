from bs4 import BeautifulSoup
from urllib2 import *
import urllib2

def grab_html(url):
  html_request = urllib2.Request(url)
  html_doc = urlopen(html_request)
  print html_doc.info()    # Print the header of the document
  data = html_doc.read()
  print "content read = %d" %(len(data)) # Print the data read
  soup = BeautifulSoup(html_doc, "lxml")
  resource_list = soup.find_all("div", class_="course-lecture-item-resource")
  print soup.prettify()
  for lecture in resource_list:
    print lecture
    break
#  print tag.attrs
#  print soup.prettify()
#  print html_doc.read(100)


if __name__ == '__main__':
  url = raw_input("Enter the url of the lectures page in coursera\n")
  try:
    grab_html(url)
  except ValueError:
    print "The URL is not valid"
  except URLError:
    print "Cannot access the URL. Try checking your Internet Connection."
