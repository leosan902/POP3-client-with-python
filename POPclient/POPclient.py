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
import base64
POP3_PORT_SSL = 995
ENCODING = 'utf-8'

TIMEOUT = 1

CRLF = "\r\n"

def getAttachment(contents):
    Hearder =''
    if 'filename=' in contents:
        
        start = contents.find('filename="') 
        end = contents.find('"', start+10)
        Hearder=contents[start+10:end]
        f=open(Hearder,'wb')
        Hearder = 'Attachment: '+Hearder
        start = contents.find('\r\n\r\n',start+3) 
        end = contents.find('\n.', start)
        Hearder2=contents[start:end-1]
        dados=base64.b64decode(Hearder2+"==")
        f.write(dados)
        f.close()
    return Hearder


def send_data(sock, data):
    """Sends data to a given socket."""
    print(data)
    sock.send((data).encode(ENCODING))
        
    buff = sock.recv(4096)
    print(buff)
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


def send_dataHeader(sock, data,self,numero):
    """Sends data to a given socket."""
    sock.send((data).encode(ENCODING))
     
    menssagem = ''
   
    while True:
            buff = sock.recv(4096)
            
            buff=(str(buff, 'utf-8'))
            menssagem+=buff
            if '\n.\r' in menssagem:
             break
   
    hearders(menssagem,self,numero)


    
        
 
def num_Mens(sock):
    menssagem=send_data(sock, 'STAT'+CRLF)
    menssagem=(str(menssagem, 'utf-8'))
    start = menssagem.find(' ') 
    end = menssagem.find(' ', start+1)
    menssagem=menssagem[start+1:end]
    return menssagem

def listagem(sock,num,self):
    
    for x in range(1,num+1):
        send_dataHeader(sock, 'RETR '+str(x)+CRLF,self,x)
       
def email_Reader(email,QDialog):
    menssagem=email
    Hearder=getAttachment(menssagem)
    start = menssagem.find('\nFrom:') 
    end = menssagem.find('\n', start+1)
    Hearder+=menssagem[start:end]
    start = menssagem.find('\nDate:') 
    end = menssagem.find('\n', start+1)
    Hearder+=menssagem[start:end]
    start = menssagem.find('\nTo:') 
    end = menssagem.find('\n', start+1)
    Hearder+=menssagem[start:end]
    start = menssagem.find('\nSubject:') 
    end = menssagem.find('\n', start+1)
    Hearder+=menssagem[start:end]
    start = menssagem.find('Received:') 
    start = menssagem.find('\n',start)
    end = menssagem.find(')', start)
    Hearder+=('Received: '+menssagem[start+14:end+1])
    
    QDialog.textBrowser_email.setText(Hearder)

  

def  send_dataEmail(sock,data,QDialog):
    sock.send((data).encode(ENCODING))
    
    menssagem = ''
    while True:
       
            buff = sock.recv(4096)
            
            buff=(str(buff, 'utf-8'))
            menssagem+=buff
            if '\n.\r' in menssagem:
             break
        
    
    email_Reader(menssagem,QDialog)   

def listEmails(sock,self):
    sock.send(('LIST'+CRLF).encode(ENCODING))
       
    menssagem = ''
   
    while True:
            buff = sock.recv(4096)
            
            buff=(str(buff, 'utf-8'))
            menssagem+=buff
            if '\n.\r' in menssagem:
             break
   
    listHeaders(sock,menssagem,self)

def listHeaders(sock,menssagem,self):
    start = menssagem.find(' ') 
    end = menssagem.find(' ', start+1)
    tamanho=int(menssagem[start+1:end])
    menssagem = menssagem[menssagem.find("\r\n")+1:]
    for x in range (0,tamanho):
        numeros = int(menssagem[:menssagem.find(' ')])
        send_dataHeader(sock, 'TOP '+str(numeros)+' 0'+CRLF,self,numeros)
        menssagem = menssagem[menssagem.find(' '):]
        menssagem = menssagem[menssagem.find('\n'):]
    


class Client():
    def __init__(self,QDialog):
        self.QDialog = QDialog
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
         self.ssl_sock = wrap_socket(s)
         self.ssl_sock.settimeout(TIMEOUT)
         self.ssl_sock.connect(('pop.gmail.com',POP3_PORT_SSL))
         data = self.ssl_sock.recv(4096)
         

 
    def login(self):
         send_data(self.ssl_sock, 'USER lwoas6432@gmail.com'+CRLF)
         send_data(self.ssl_sock, 'PASS azxsdc32'+CRLF)
         #if(data.startswith(b'+OK')==True):           
              
    def emails(self,QDialog):
        self.numero_Mens =num_Mens(self.ssl_sock)
        QDialog.textBrowser_NEmails.setText(self.numero_Mens)
        listEmails(self.ssl_sock,self.QDialog)
        #listagem(self.ssl_sock,num_emails,self.QDialog)
        
 
    def identificarMensagem(self,texto):
        send_dataEmail(self.ssl_sock, 'RETR '+texto+CRLF,self.QDialog)
     
   

    def deletarEmail(self,texto):
       end = texto.find('\n')
       texto=texto[:end]
       while True:
           if b'OK' in send_data(self.ssl_sock, 'NOOP'+CRLF):
            time.sleep(0.1)
            send_data(self.ssl_sock, 'DELE '+texto+CRLF)
            tempNumero= int(self.numero_Mens)
            tempNumero-= 1
            self.numero_Mens= str(tempNumero)
            self.QDialog.textBrowser_NEmails.setText(self.numero_Mens)
            break



        