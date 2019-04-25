# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Emailreader.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import sys,email
from ssl import wrap_socket
from os import linesep
import time,email

POP3_PORT_SSL = 995
ENCODING = 'utf-8'

TIMEOUT = 1
f= open("guru99.txt","w+")
CRLF = "\r\n"

def extract_mime_part_matching(stream, mimetype):
    """Return the first element in a multipart MIME message on stream
    matching mimetype."""

    msg = mimetools.Message(stream)
    msgtype = msg.gettype()
    params = msg.getplist()

    data = StringIO.StringIO()
    if msgtype[:10] == "multipart/":

        file = multifile.MultiFile(stream)
        file.push(msg.getparam("boundary"))
        while file.next():
            submsg = mimetools.Message(file)
            try:
                data = StringIO.StringIO()
                mimetools.decode(file, data, submsg.getencoding())
            except ValueError:
                continue
            if submsg.gettype() == mimetype:
                break
        file.pop()
    return data.getvalue()
      

def send_data(sock, data,profile=True):
    """Sends data to a given socket."""
    sock.send((data).encode(ENCODING))


    if profile:
        sys.stderr.write(data + linesep)

    buff = sock.recv()
    print (buff)
    return buff

def hearders(menssagem,self,numero):
    Hearder = str(numero)
    Hearder += ' '
    start = menssagem.find('\nFrom:') 
    end = menssagem.find('\n', start+1)
    Hearder+=menssagem[start:end]
    start = menssagem.find('\nDate:') 
    end = menssagem.find('\n', start+1)
    Hearder+=menssagem[start:end]
    self.listWidget_Emails.addItem(Hearder)


def send_dataHeader(sock, data,self,numero,profile=True):
    """Sends data to a given socket."""
    sock.send((data).encode(ENCODING))
    
    if profile:
        sys.stderr.write(data + linesep)
    menssagem = ''
    buff = sock.recv()
    data2 = buff
    menssagem+=(str(buff, 'utf-8'))
    while True:
          buff = sock.recv()
         
         
          buff=(str(buff, 'utf-8'))
          menssagem+=buff
          
          if buff.endswith('.\r\n'):
            break
   
    hearders(menssagem,self,numero)


    
        
 
def num_Mens(sock,profile=True):
    menssagem=send_data(sock, 'STAT'+CRLF)
    menssagem=(str(menssagem, 'utf-8'))
    start = menssagem.find(' ') 
    end = menssagem.find(' ', start+1)
    menssagem=menssagem[start+1:end]
    return menssagem

def listagem(sock,num,self,profile=True):
    
    for x in range(1,num+1):
        send_dataHeader(sock, 'RETR '+str(x)+CRLF,self,x)
       
def email_Reader(email,QDialog):
    menssagem=email
    start = menssagem.find('\nFrom:') 
    end = menssagem.find('\n', start+1)
    Hearder=menssagem[start:end]
    start = menssagem.find('\nDate:') 
    end = menssagem.find('\n', start+1)
    Hearder+=menssagem[start:end]
    start = menssagem.find('\nTo:') 
    end = menssagem.find('\n', start+1)
    Hearder+=menssagem[start:end]
    start = menssagem.find('\nSubject:') 
    end = menssagem.find('\n', start+1)
    Hearder+=menssagem[start:end]
    Hearder+=' |No horario|'   
    start = menssagem.find('(version=TLS1 cipher=ECDHE-RSA-AES128-SHA bits=128/128)') 
    start = menssagem.find('  ',start) 
    end = menssagem.find('\n', start+1)
    Hearder+=menssagem[start+6:end]
    QDialog.textBrowser_email.setText(Hearder)



def  send_dataEmail(sock,data,QDialog,profile=True):
    sock.send((data).encode(ENCODING))
    
    if profile:
        sys.stderr.write(data + linesep)
    menssagem = ''
    while True:
        try:
            buff = sock.recv(4096)
            buff=(str(buff, 'utf-8'))
            menssagem+=buff
        except socket.timeout:
            break
    f.write(menssagem)
    email_Reader(menssagem,QDialog)   




class Client():
    def __init__(self,QDialog):
        self.QDialog = QDialog
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
         self.ssl_sock = wrap_socket(s)
         self.ssl_sock.settimeout(TIMEOUT)
         self.ssl_sock.connect(('pop.gmail.com',POP3_PORT_SSL))
         data = self.ssl_sock.recv(4096)
         print (data)


 
    def login(self):
         send_data(self.ssl_sock, 'USER lwoas6432@gmail.com'+CRLF)
         send_data(self.ssl_sock, 'PASS azxsdc32'+CRLF)
         #if(data.startswith(b'+OK')==True):           
              
    def emails(self,QDialog):
        num_emails=int(num_Mens(self.ssl_sock))
        print(num_emails)
        listagem(self.ssl_sock,num_emails,self.QDialog)
        send_data(self.ssl_sock, 'RSET'+CRLF)

    def identificarMensagem(self,texto):
     send_dataEmail(self.ssl_sock, 'RETR '+texto+CRLF,self.QDialog)



        