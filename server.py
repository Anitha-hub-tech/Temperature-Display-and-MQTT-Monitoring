from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket
import os

# Get local IP address
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to an external address (Google DNS)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

# Change to the directory where dashboard.html is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Set up the server
PORT = 8080
HOST = "0.0.0.0"  # Listen on all network interfaces

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/dashboard.html"
        return super().do_GET()

server = HTTPServer((HOST, PORT), MyHandler)
local_ip = get_local_ip()

print(f"🚀 Server started!")
print(f"📍 Local IP: {local_ip}")
print(f"🌐 Access the dashboard at:")
print(f"   http://{local_ip}:{PORT}")
print(f"   or")
print(f"   http://localhost:{PORT} (local access only)")
print(f"\n💡 Share this IP with others on your network: {local_ip}:{PORT}")
print(f"\nPress Ctrl+C to stop the server...")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\n✋ Server stopped.")
    server.server_close()
