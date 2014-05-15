from bs4 import BeautifulSoup
from urllib2 import *
import traceback
import re

DESKTOP = "/Users/saratsista/Desktop"

def grab_html(url):
  ''' 
    Method to seperate the html portion from the webpage that contains links to lecture material. 
  '''
  html_doc = urlopen(url).read()
  soup = BeautifulSoup(html_doc, "lxml")
  resource_list = soup.find_all("div", class_="course-lecture-item-resource")
  for lecture in resource_list:
    #print lecture.a['href']			# prints urls of only the first element of type 'a' in each lecture tag
    link_elements = lecture.find_all("a") 	# Within each lecture find all the 'a' tags
    for link in link_elements:			# here 'link' is already 'a' tag. So do link['href'] instead of link.a['href']
      download_file(link['href'])
    break	# For now, download only one lecture material    

def download_file(url):
  '''
    Method to download the file and save it to desktop
  '''
  # XXX:TODO 1. find out a way to download both typed and printed pdfs which have the same url
  # 	     2. Rename the mp4 to the name of the lecture
  #	     3. Download files of a lecture into respective folder
  # First find out the type of file being downloaded from the url
  pattern = re.compile(".pptx|.pdf|[.]*txt|[.]*srt|.mp4")
  match = pattern.search(url)
  # If file is a subtitle
  if match.group().find('txt') > -1 or match.group().find('srt') > -1:
    path = DESKTOP + '/subtitle.'+match.group()
    print path
    subtitle = urlopen(url)
    with open(path,'w') as file:
	file.write(subtitle.read())  
  # For files of all other types
  else:
    path = DESKTOP + file_name(url, match.group())
    print path
    ppt = urlopen(url)
    with open(path, 'w') as file:
	file.write(ppt.read())
   
def file_name(url, ext):
  '''
    Method that sets the name of the file to be downloaded to the one given in the url
    url = url from which file is to be downloaded
    ext = extension of the file given by the url
  '''
  pattern = re.compile("/[\w-]+"+ext)
  match = pattern.search(url)
  return match.group() 


if __name__ == '__main__':
  url = raw_input("Enter the url of the lectures page in coursera\n")
  try:
    grab_html(url)
  except ValueError:
    print "The URL is not valid"
  except URLError:
    print traceback.format_exc()
    print "Cannot access the URL. Either the URL is wrong or there is no  Internet Connection."
