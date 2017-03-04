from http.server import BaseHTTPRequestHandler, HTTPServer
import re
import cgi


class MiiyooServerRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if re.search("/senddata", self.path) is not None:
            form = cgi.FieldStorage(
				fp=self.rfile,
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})
            print(form["data"].value)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes("{}", "ASCII"))
            return
        self.send_response(403)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(bytes("{}", "ASCII"))

    def do_GET(self):
        if re.search("/status/*", self.path) is not None:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            # Fucking CORS
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes("""{"connectedDeviceName":"ONYX",
            "bluetoothAddress":"8CDE52B866B5",
            "firmwareUpdateProgres":0,
            "remoteDevice":"not connected",
            "devicestatus":"NORMAL",
            "localDevice":"connected",
            "previousdevice_connectionurl":"btspp://8CDE52B866B5:1;authenticate=false;encrypt=false;master=false",
            "readOnlyMode":false,
            "streamToDeviceEnabled":true,
            "delay":0,
            "writeOnlyMode":false,
            "currentFW":"91",
            "waitingforusbcable":true,
            "bluetoothOn":true,
            "previousdevice_name":"ONYX",
            "uienabled":true,
            "newFWVersionAvailable":false,
            "previousdevice_bluetoothaddress":"8CDE52B866B5",
            "statusCode":1}""", "ASCII"))
            return
        self.send_response(403)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(bytes("{}", "ASCII"))


class MiiyooServer():
    def start(self):
        server = HTTPServer(("localhost", 6969), MiiyooServerRequestHandler)
        server.serve_forever()

if __name__ == "__main__":
    m = MiiyooServer()
    m.start()
