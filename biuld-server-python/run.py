import logging
import http.server
import socketserver
import getpass

class MyHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,format,*args):
        logging.info("%s -- [%s] %s\n"%(
            self.client_address[0],
            self.log_date_time_string(),
            format%args
        ))
logging.basicConfig(
    filename='/log/http_server.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.getLogger().addHandler(logging.StreamHandler())
logging.info('get startd')
PORT=8080

httpd = socketserver.TCPServer(("",PORT),MyHTTPHandler)
logging.info('Listen PORT: %s',PORT)
logging.info('User: %s',getpass.getuser())

httpd.serve_forever()
