import http.server
import socketserver

# A simple script to use the python simple server in python3
# Using SimpleHTTPRequestHandler means GET only

# define the handler to be the Simple server
handler = http.server.SimpleHTTPRequestHandler

# define the server using the handler
PORT = 8000
httpd = socketserver.TCPServer(("localhost", PORT), handler)

# Set variables which the CGIHTTPRequestHandler expects
# httpd.server_name = "myServer"
# httpd.server_port = PORT

print("staring simple server...")

# run the server. To kill it, issue Ctrl + C
httpd.serve_forever()
