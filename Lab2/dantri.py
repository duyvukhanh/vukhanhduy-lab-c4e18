from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel

url = "http://www.dantri.com.vn"

# 1 . Download web page
# 1.1 . Create a connection
conn = urlopen(url)

# 1.2 . Read data
data = conn.read()

# 1.3 . Decode
html_content = data.decode("utf-8")
# print(html_content)

# 1.4 . Save html_content to file ( chi lam 1 lan )

# f = open("dantri.html","w")
# f.write(html_content)
# f.close



# 2 . Extract ROI ( Region of interest )
# html xml xhtml
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())
ul = soup.find("ul","ul1 ulnew")

# 3 . Extract info

li_list = ul.find_all("li")

list_of_dict = []

for li in li_list:
    # print(li.prettify())
    # print("* "*20)
    
    # h4 = li.find("h4")
    # a = h4.find("a")

    # h4 = li.h4
    # a = h4.a

    a = li.h4.a
    # print(a.string)
    # print("*************")
    # print(url + a["href"])

    dictionary = {}
    dictionary["Title"] = a.string
    dictionary["Link"] = url + a["href"]

    list_of_dict.append(dictionary)

pyexcel.save_as(records=list_of_dict, dest_file_name="dantri.xlsx")

    


# 3 . Exreact info