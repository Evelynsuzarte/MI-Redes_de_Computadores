import http.server
import socketserver


class myhandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'motherpage.html'
        return http.server.SimpleHTTPRequestHandler(self)

        