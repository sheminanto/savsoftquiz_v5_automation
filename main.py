import requests
from bs4 import BeautifulSoup
import time


host = 'http://128.199.29.189/'
slug_login = 'index.php/login/verifylogin/'
slug_insert_user = 'index.php/user/insert_user/'
slug_remove_user = 'index.php/user/remove_user/'

username = 'admin@example.com'
password = 'admin'

session = requests.Session()


login_data = {
    'email': username,
    'password': password
}

resp = session.post(host+slug_login, data=login_data)


# print(resp.text)


# for i in range(101, 10000):
#     insert_user_data = {
#         'email': 'bot'+str(i)+'@bot.com',
#         'password': 'bot',
#         'first_name': 'bot',
#         'last_name': 'bot',
#         'contact_no': None,
#         'gid': 1,
#         'subscription_expired': '2031-04-05',
#         'su': 2
#     }
#     resp = session.post(host+slug_insert_user, data=insert_user_data)
#     print(insert_user_data['email'])


for i in range(17, 50):
    resp = session.get(host+slug_remove_user+str(i))
    print(i)
