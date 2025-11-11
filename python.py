from http.server import SimpleHTTPRequestHandler, HTTPServer

print("Server starting on port 3000...")
HTTPServer(("", 3000), SimpleHTTPRequestHandler).serve_forever()
