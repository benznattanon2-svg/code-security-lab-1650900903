import os
import http.server
import socketserver
import subprocess
from datetime import datetime

PORT = int(os.environ.get('PORT', 8080))
DB_CONNECTED = bool(os.environ.get('DB_PASSWORD'))

class AppHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # INTENTIONAL SECURITY FLAW FOR BANDIT TO CATCH
        # 1. B602: subprocess with shell=True (Command Injection risk)
        user_input = "echo 'Lab 4'"
        subprocess.Popen(user_input, shell=True)
        
        # 2. B307: use of eval (Arbitrary Code Execution risk)
        calc = eval("1 + 1")

        msg = f'<html><body><h2>Code Security Lab</h2>'
        msg += f'<p>Time: {datetime.now().isoformat()}</p>'
        msg += f'<p>DB connection configured: {DB_CONNECTED}</p>'
        msg += f'</body></html>'
        self.wfile.write(msg.encode())
    def log_message(self, fmt, *args): pass

with socketserver.TCPServer(('', PORT), AppHandler) as httpd:
    print(f'Serving on port {PORT}')
    httpd.serve_forever()
