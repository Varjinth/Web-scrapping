from django.apps import AppConfig




class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

'''
from bs4 import BeautifulSoup
import requests
source= requests.get('https://www.flipkart.com/florida-blue-analog-round-dial-digital-silicon-strap-aviator-sunglass-uv-protection-analog-digital-watch-boys/p/itmd51d636f9f470?pid=WATGY4R3MZBSXWRQ&lid=LSTWATGY4R3MZBSXWRQIQJAQB&marketplace=FLIPKART&fm=productRecommendation%2FattachForSwatchProducts&iid=R%3Aas%3Bp%3ASGLFHQPHY2GZ4HFP%3Bpt%3App%3Buid%3Ad04ee673-a37b-11ed-830b-2fc6caf71955%3B.WATGY4R3MZBSXWRQ&ppt=pp&ppn=pp&ssid=knsm7axa4w0000001675398773894&otracker=pp_reco_Frequently%2BBought%2BTogether_1_Frequently%2BBought%2BTogether_WATGY4R3MZBSXWRQ_productRecommendation%2FattachForSwatchProducts&otracker1=pp_reco_PINNED_productRecommendation%2FattachForSwatchProducts_Frequently%2BBought%2BTogether_NA_productCard_cc_1_NA_view-all&cid=WATGY4R3MZBSXWRQ').text

soup= BeautifulSoup(source, 'lxml')
# soup=soup.prettify()
# title=soup.find('span', class_="G6XhRU").text
description=soup.find("span", class_="B_NuCI").text
price=soup.find("div" ,class_="_30jeq3 _16Jk6d").text
category  = soup.find_all('a', {'class': '_2whKao'})[1].text
img=soup.find_all('img', {'class': 'q6DClP'})[2]['src']
img_data = requests.get(img).content
try:
    size=soup.find('a', class_='_1fGeJ5').text
except:
    size= 'unknown'


# print(img_data)

# #content = second_a_tag

title = soup.find('span', class_="G6XhRU").text
print(title, description, price,category, size)
# print(title,description,price,img)
# print(category)
# with open('flip.html', "w", encoding="utf-8") as f:
#     f.write(str(soup))
'''