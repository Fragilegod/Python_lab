import requests
import re

response = requests.get('https://moodle.tsu.ru/')
result = re.findall(pattern=r'[\w.]*[\-]*[\w.]+@\w+\.\w+[\.]*[\w+]*', string=response.text)
print(list(set(result)))