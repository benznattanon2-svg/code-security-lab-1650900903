import os
import http.server
import socketserver
from datetime import datetime
PORT = int(os.environ.get('PORT', 8080))
class AppHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        msg = f'<html><body><h2>Code Security Lab</h2>'
        msg += f'<p>Time: {datetime.now().isoformat()}</p>'
        msg += f'<p>App version: 1.0</p></body></html>'
        self.wfile.write(msg.encode())
    def log_message(self, fmt, *args): pass
with socketserver.TCPServer(('', PORT), AppHandler) as httpd:
    print(f'Serving on port {PORT}')
    httpd.serve_forever()
