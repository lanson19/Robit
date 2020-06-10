from http.server import BaseHTTPRequestHandler, HTTPServer

state = '{"w":false,"a":false,"s":false,"d":false,"up":false,"left":false,"down":false,"right":false}'

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def _set_response_css(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/css')
        self.end_headers()

    def do_GET(self):
        global state
        if self.path == '/':
            self._set_response()
            f = open("index.html", "r")
            self.wfile.write(f.read().encode('utf-8'))

        if self.path == '/styles.css':
            self._set_response_css()
            f = open("styles.css", "r")
            self.wfile.write(f.read().encode('utf-8'))

        if self.path == '/state':
            self._set_response()
            self.wfile.write(state.encode('utf-8'))
        #self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
        

    def do_POST(self):
        global state
        self._set_response()
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length)
        state = post_data.decode('utf-8')


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
