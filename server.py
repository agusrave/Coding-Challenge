"""
Created on Mon Jun 20 15:40:25 2022

@author: Agustina Ravettino
"""
import sys
import cgi
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse
from urllib.parse import parse_qs
from zipfile import ZipFile
from functions import pandas_function, unzip_file


HOST_NAME = "localhost"
PORT = 8080

def read_html_template(path):
    """function to read HTML file"""
    try:
        with open(path) as f:
            file = f.read()
    except Exception as e:
        file = e
    return file


class PythonServer(SimpleHTTPRequestHandler):
    """Python HTTP Server that handles GET and POST requests"""
    def do_GET(self):
        try:
            parsed = urlparse(self.path)
            path = parsed.path
            #print(parsed.path)
            #print(parse_qs(parsed.query)['nombre'][0])
            #print(self.headers.get("authorization"))
            if  path == '/':
                self.send_response(200, "OK")
                self.end_headers()
                file = read_html_template("./index.html")
                self.wfile.write(bytes(file, "utf-8"))
        except:
            pass

    def do_POST(self):
        try:
            if self.path == '/processfile':
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    zipfile = fields.get("zipfile")[0]
                    password = fields.get("password")[0]

                    if(password=="process"): #password 
    
                        os.system("rm -rf directory")
                        os.system("mkdir directory")

                        #Generate a new directory to save the file uploaded
                        f = open("directory/zipfile.zip", "wb")
                        f.write(zipfile)
                        f.close()

                        # 1. Unzip directory uploaded
                        os.system("unzip directory/zipfile.zip -d directory")
                        os.system("rm directory/zipfile.zip")

                        # 1. Execute bash script
                        os.system("bash script.sh directory")
                        
                        # 2. Call python function
                        result = pandas_function('directory_stats.txt') 

                        # Send result
                        self.send_response(200, "OK")
                        self.end_headers()
                        self.wfile.write(bytes(result, "utf-8"))
                    else:
                        html = f"<html><head></head><body><h1>Password incorrect, try again!</h1></body></html>"
                        self.send_response(200, "OK")
                        self.end_headers()
                        self.wfile.write(bytes(html, "utf-8"))
            

        except:
            html = f"<html><head></head><body><h1>Error while attempting to process file </h1></body></html>"
            self.send_response(200, "OK")
            self.end_headers()
            self.wfile.write(bytes(html, "utf-8"))

       

if __name__ == "__main__":
    server = HTTPServer((HOST_NAME, PORT), PythonServer)
    print(f"Server started http://{HOST_NAME}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped successfully")
        sys.exit(0)