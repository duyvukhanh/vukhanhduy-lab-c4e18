from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch',
    'max_downloads': 1 
}
dl = YoutubeDL(options)

url = "https://www.apple.com/itunes/charts/songs"
# 1 . Download web page
conn = urlopen(url)
data = conn.read()
html_content = data.decode("utf-8")

# 2 . Extract ROI ( Region of interest )
soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("section","section chart-grid")

# 3 . Extract info
list_of_song = []
li_list = ul.find_all("li")

for li in li_list:
    h3 = li.h3
    h4 = li.h4
  
    dictionary = {}   
    dictionary["Name"] = h3.string
    dictionary["Artist"] = h4.string
    list_of_song.append(dictionary)
    
    download = ""
    download = h3.string + " " + h4.string
    dl.download([download])


pyexcel.save_as(records=list_of_song, dest_file_name="itunes_top100.xlsx")
