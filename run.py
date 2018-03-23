#! /usr/bin/env python
from app import app
from config import DEBUG, HOST, PORT
HOST = "0.0.0.0"
DEBUG = True
PORT = 8080
# git remote add origin https://github.com/kaiesha96/info3180-project1.git
# git push -u origin master
if __name__ == "__main__":
    app.run(debug = DEBUG, host = HOST, port = PORT)
    
