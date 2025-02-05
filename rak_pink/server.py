import http.server
import socketserver

# Define the port number to serve on
PORT = 8901

# Define a simple handler for HTTP requests
Handler = http.server.SimpleHTTPRequestHandler

# Create the HTTP server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTTP on port {PORT}...")
    try:
        # Start the server
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Gracefully shut down on Ctrl+C
        print("\nShutting down the server.")
        httpd.shutdown()