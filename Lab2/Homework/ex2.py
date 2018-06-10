from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

# 1 . Download web page
conn = urlopen(url)
data = conn.read()
html_content = data.decode("utf-8")



# 2 . Extract ROI ( Region of interest )
soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table",id = "tableContent")

# 3 . Extract info
list_needed = []
td_list = table.find_all("td","b_r_c")

for i in range(0,len(td_list),6):
    dictionary = {}

    dictionary["Title"] = td_list[i].string
    dictionary["Quy 4 - 2016"] = td_list[i+1].string
    dictionary["Quy 1 - 2017"] = td_list[i+2].string
    dictionary["Quy 2 - 2017"] = td_list[i+3].string
    dictionary["Quy 3 - 2017"] = td_list[i+4].string
    
    list_needed.append(dictionary)
    



pyexcel.save_as(records=list_needed, dest_file_name="vinamilk.xlsx")


