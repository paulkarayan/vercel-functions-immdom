from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import os
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        print(parse_qs(self.path[2:]))

        user = parse_qs(self.path[2:]).get('username', 'paulkarayan')
        GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')

        url = "https://api.github.com/users/{user}".format(user=user)
        headers =  {
                    "Authorization": "Bearer {GITHUB_ACCESS_TOKEN}".format(GITHUB_ACCESS_TOKEN=GITHUB_ACCESS_TOKEN),
                    "Content-Type": "application/json"
                }
        r = requests.get(url, headers=headers)

        self.wfile.write(r.text().encode())
        return
