# Simple Python TCP Web Server & Client
Our project demonstrates a basic HTTP server and client using Python sockets.

## Files

- **server.py**:  
  - Listens on port 6789  
  - Serves static HTML files  
  - Returns `200 OK` or `404 Not Found`

- **client.py**:  
  - Connects to the server  
  - Sends an HTTP GET request for a file  
  - Prints the full HTTP response

- **HelloWorld.html**:  
  Sample HTML page to test the server

---

## Quick Start

**Run the server** (Terminal 1):
```
python server.py
```

You should see:
```
Ready to serve...
```

### Test in browser:
Open: http://localhost:6789/HelloWorld.html


### Test in terminal:
**Run the client** (Terminal 2):
```
python client.py localhost 6789 HelloWorld.html
```
This prints the raw HTTP response.

### Test 404:
```

python client.py localhost 6789 NoFile.html (or really any file name that doesn't exist)
```

You’ll get a `404 Not Found` page.