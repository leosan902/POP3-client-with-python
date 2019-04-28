from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import sys,email
from ssl import wrap_socket
from os import linesep
import time,email
import base64
POP3_PORT_SSL = 995
ENCODING = 'utf-8'
f=open('Hearde.txt','w')
contents = f.read()
f.close()

f=open('guru99.txt','w')
f.write(contents)
f.close()
start = contents.find('filename="') 
end = contents.find('"', start+10)
Hearder=contents[start+10:end]
f=open(Hearder,'wb')
start = contents.find('\n\n\n\n',start) 
end = contents.find('\n.', start)
Hearder=contents[start+3:end-1]
print(Hearder.encode(ENCODING))
dados=base64.b64decode(Hearder+"==")
f.write(dados)
f.close()