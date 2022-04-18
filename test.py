import sys
import requests

domain = 'http://' + sys.argv[1]
requests.get("http://43.133.4.167?"+domain)
