import requests
from bs4 import BeautifulSoup
import time


host = 'http://159.65.151.192/'  # change hostname
slug_login = 'index.php/login/verifylogin/'
slug_insert_user = 'index.php/user/insert_user/'
slug_remove_user = 'index.php/user/remove_user/'

username = 'admin@example.com'  # change username & password
password = 'adminexample'

session = requests.Session()


login_data = {
    'email': username,
    'password': password
}

resp = session.post(host+slug_login, data=login_data)


# print(resp.text)


######################################
# Inserting User
######################################

# for i in range(1, 2):
#     insert_user_data = {
#         'email': 'fisat'+str(i)+'@bot.com',
#         'password': 'fisatexam',
#         'first_name': None,
#         'last_name': None,
#         'contact_no': None,
#         'gid': 5,
#         'subscription_expired': None,
#         'su': 2
#     }
#     resp = session.post(host+slug_insert_user, data=insert_user_data)
#     print(insert_user_data['email'])


######################################
# Deleting User
######################################
# for i in range(17, 50):
#     resp = session.get(host+slug_remove_user+str(i))
#     print(i)
