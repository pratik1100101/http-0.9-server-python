# Basic HTTP/0.9 Server in Python

This project demonstrates a fundamental HTTP server implementation using Python's built-in `socket` library. It's designed to illustrate the core concepts of how an HTTP server works at a low level, specifically supporting the very basic HTTP/0.9 GET requests.

## How it Works

The server setup typically involves these steps:

1.  **Address and Port Definition:** We define the server's address (localhost, `127.0.0.1`) and a specific port (e.g., `8080`).
2.  **Socket Creation:** A server socket is created, analogous to getting a phone ready to receive calls.
3.  **Binding and Listening:** The server socket is assigned a "phone number" (host and port) and starts listening for incoming client connections.
4.  **Connection Processing Loop:** The server enters a continuous loop to handle incoming requests:
    * It accepts a new client connection.
    * Receives and decodes the incoming HTTP request (all network communication happens in bytes).
    * Parses the request headers to identify the HTTP method (e.g., `GET`) and the requested path (e.g., `/`).
    * If the method is `GET` and the path is `/`, it serves the `index.html` file. For any other path or unsupported HTTP method, it returns appropriate HTTP error responses (e.g., 404 Not Found, 405 Method Not Allowed).

### What is a Stream?

When you perform an `open()` operation, the operating system allocates resources and sets up a connection between your program and the specified file. The "stream" object you get back is like a conveyor belt delivering data (usually bytes or characters) sequentially. Through this stream object, you can then:
Read, write, and manage data flow efficiently without loading everything into memory at once.

## How to Run

1.  **Prerequisites:**
    * Ensure you have Python 3 installed.
    * Make sure `server.py` (or `main.py`) and `index.html` are in the same directory.
    * Create a simple `index.html` file in the same directory, e.g.:
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Simple HTTP Server</title>
        </head>
        <body>
            <h1>Hello from your Python HTTP/0.9 Server!</h1>
            <p>This is a very basic web page served locally.</p>
        </body>
        </html>
        ```

2.  **Execute the server:**
    Open your PowerShell, Command Prompt, or Apple equivalent terminal, navigate to the directory where your server script is, and run the command:

    ```bash
    python server.py # Or python main.py if you named it main.py
    ```

3.  **Access in browser:**
    Open your web browser and go to: `http://127.0.0.1:8080`

## Sample Terminal Output
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
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image:apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

Connection with ('127.0.0.1', 51662) closed.