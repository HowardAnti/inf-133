from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    try:
        server_address = ('',8000)
        httpd = server_class(server_address, handler_class)
        print ('Starting up webserver http://localhost:8000/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print ('Shutting down webserver')
        httpd.socket.close()

if __name__ == '__main__':
    run()