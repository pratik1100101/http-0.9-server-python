"""
This is a simple HTTP server script that walks you through the basics of any HTTP server.
It uses Python's `socket` library to enable setting up a server-side connection.

HTTP server setup typically works this way:
1. We define the address (our local PC, "127.0.0.1") and a specific port (e.g., 8080).
2. We set up the server socket, think of this like getting a phone ready to receive calls.
3. We assign (bind) the phone number (host and port) to the server socket and
   start listening for incoming connections.
4. We then enter a loop to continuously process client connections:
   i. Get the client details and decode the incoming request, as all network
      communication happens in bytes.
   ii. Parse the request headers to identify the HTTP method (e.g., GET) and the
       requested path (e.g., '/').
   iii. If the method is GET and the path is '/', we serve the 'index.html'
        file. For any other path or method, we return appropriate HTTP error responses.

**What is a stream:**
When you perform an `open()` operation, the operating system allocates resources and sets
up a connection between your program and the specified file. The "stream" object you
get back is like a conveyor belt delivering data (usually bytes or characters) sequentially.
Through this stream object, you can then:
Read, write, and manage data flow efficiently without loading everything into memory at once.

How to run:
Use the powershell/cmd/apple equivalent and run the command:
$ python main.py

This is a sample terminal output:
Server online, listening on http://127.0.0.1:8080
Accepted connection from ('127.0.0.1', 51662)
--- Request received ---
 GET / HTTP/1.1
Host: 127.0.0.1:8080
Connection: keep-alive
sec-ch-ua: "Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8


------------------------
"""

import socket

HOST = "127.0.0.1"  # Localhost
PORT = 8080  # Since HTTP works on TCP port 80

# 1. Create a server socket -- setting up the phone
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. (Optional but recommended)
#    Allow the socket to reuse the address. This helps avoid "Address already in use" errors
#    when restarting the server quickly after a crash or shutdown since the OS always waits
#    for sometime before freeing up the address.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 3. Bind the socket to the host and port -- setting up our phone number
server_socket.bind((HOST, PORT))

# 4. Listen for incoming connections (up to 5 queued connections)
server_socket.listen(5)
print(f"Server online, listening on http://{HOST}:{PORT}")

try:
    while True:
        # 5. Accept a new connection from a client -- extracting their phone number
        client_sock, client_addr = server_socket.accept()
        print(f"Accepted connection from {client_addr}")

        # 6. Receive the client's request and decoding it in the utf-8 format
        #    1500 is the number of bytes that we process. This is a critical number in
        #    networking, not specifically for HTTP connections, but because it's the
        #    default Maximum Transmission Unit (MTU) for standard Ethernet networks.
        request = client_sock.recv(1500).decode("utf-8")
        print("--- Request received ---\n", request, "\n------------------------")

        # Basic request parsing for the first line (e.g., "GET / HTTP/1.1")
        headers = request.split("\n")
        first_line_components = headers[0].split()

        # Ensure we have at least 2 components (method and path)
        if len(first_line_components) < 2:
            response = "HTTP/1.1 400 Bad Request\nContent-Type: text/plain\n\nMalformed Request"
        else:
            http_method = first_line_components[0]
            path = first_line_components[1]

            if http_method == "GET":
                if path == "/":
                    file_path = "index.html"
                    # Use 'with open' for safe file handling (ensures file is closed)
                    with open(file_path, "r", encoding="utf-8") as fin:
                        content = fin.read()
                    response = (
                        f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\nContent-Length: {len(content.encode('utf-8'))}\n\n"
                        + content
                    )
                else:
                    response = "HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\nResource Not Found"
            else:
                # Not allowing any other HTTP method
                response = "HTTP/1.1 405 Method Not Allowed\nContent-Type: text/plain\nAllow: GET\n\nMethod Not Allowed"

        # 7. Send the constructed HTTP response back to the client
        client_sock.sendall(response.encode("utf-8"))

        # 8. Remember to always close the client socket
        client_sock.close()
        print(f"Connection with {client_addr} closed.")

except KeyboardInterrupt:
    # Handles Ctrl+C shut down the server
    print("\nServer shutting down.")
finally:
    # Ensure the server socket is closed when the program exits
    server_socket.close()
