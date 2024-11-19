from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>Laptop Configuration</h2>

<table>
  <tr>
    <td>Name</td>
    <td>Lenovo</td>
  </tr>
  <tr>
    <td>OS</td>
    <td>Windows 11</td>
  </tr>
  <tr>
    <td>Primary Memory</td>
    <td>16GB</td>
  </tr>
  <tr>
    <td>Secondary Memory</td>
    <td>256GB</td>
  </tr>
  <tr>
    <td>Processor</td>
    <td>Intel i5</td>
  </tr>
  
</table>

</body>
</html>


'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()