# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#!/usr/bin/env python3
import sys
import socket
from ssl import wrap_socket
from os import linesep
import time
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from Emailreader import Ui_Email_Dialog

POP3_PORT_SSL = 995
ENCODING = 'utf-8'

TIMEOUT = 10
SERVER_REPLY_BUFFER = 50
CRLF = "\r\n"

   

def send_data(sock, data,profile=True):
    """Sends data to a given socket."""
    sock.send((data).encode(ENCODING))


    if profile:
        sys.stderr.write(data + linesep)

    buff = sock.recv()
    data = buff
    time.sleep(0.5)
    print (buff)
def send_data2(sock, data,data2,profile=True):
    """Sends data to a given socket."""
    sock.send((data).encode(ENCODING))

    if profile:
        sys.stderr.write(data + linesep)

    buff = sock.recv()
    data2 = buff
    print (buff)
    while True:
          buff = sock.recv()
          print (buff)
          f.write(str(buff, 'utf-8'))
          if buff.endswith(b'.\r\n'):
            break
    
def login(login,senha):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            ssl_sock = wrap_socket(s)
            ssl_sock.settimeout(TIMEOUT)
            ssl_sock.connect(('pop.gmail.com',POP3_PORT_SSL))
            data = ssl_sock.recv(4096)
            print (data)
    with ssl_sock:
            
            send_data(ssl_sock, 'USER '+login+CRLF,data)
            
            if(data.startswith(b'+OK')==True):
              send_data(ssl_sock, 'PASS '+senha+CRLF,data)
              print('PASS '+senha)
              
              if(data.startswith(b'+OK')==True):
                  send_data(ssl_sock, 'QUIT'+CRLF,data)
                  print(data)
                  return 1
              
          #send_data(ssl_sock, 'STAT'+CRLF)
          #send_data2(ssl_sock, 'LIST '+CRLF)
          #send_data2(ssl_sock, 'RETR 4'+CRLF)
          #send_data(ssl_sock, 'RSET'+CRLF)
            
   
         

class Ui_Login_Dialog(object):
    
        
    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName("Login_Dialog")
        Login_Dialog.resize(519, 428)
        self.pushButton = QtWidgets.QPushButton(Login_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 300, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Login_Dialog)
        self.widget.setGeometry(QtCore.QRect(91, 10, 311, 271))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Sever = QtWidgets.QLabel(self.widget)
        self.label_Sever.setObjectName("label_Sever")
        self.verticalLayout.addWidget(self.label_Sever)
        self.lineEdit_EmailServer = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_EmailServer.setObjectName("lineEdit_EmailServer")
        self.verticalLayout.addWidget(self.lineEdit_EmailServer)
        self.label_port = QtWidgets.QLabel(self.widget)
        self.label_port.setObjectName("label_port")
        self.verticalLayout.addWidget(self.label_port)
        self.lineEdit_Port = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.verticalLayout.addWidget(self.lineEdit_Port)
        self.label_Login = QtWidgets.QLabel(self.widget)
        self.label_Login.setObjectName("label_Login")
        self.verticalLayout.addWidget(self.label_Login)
        self.lineEdit_Login = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Login.setObjectName("lineEdit_Login")
        self.verticalLayout.addWidget(self.lineEdit_Login)
        self.label_Senha = QtWidgets.QLabel(self.widget)
        self.label_Senha.setObjectName("label_Senha")
        self.verticalLayout.addWidget(self.label_Senha)
        self.lineEdit_Senha = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Senha.setObjectName("lineEdit_Senha")
        self.verticalLayout.addWidget(self.lineEdit_Senha)
        self.lineEdit_Senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retranslateUi(Login_Dialog)
        self.pushButton.clicked.connect(self.button_pressed)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)
        
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def retranslateUi(self, Login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "Login Dialog"))
        self.pushButton.setText(_translate("Login_Dialog", "Ok"))
        self.label_Sever.setText(_translate("Login_Dialog", "Email Server"))
        self.label_port.setText(_translate("Login_Dialog", "Porta"))
        self.label_Login.setText(_translate("Login_Dialog", "Login"))
        self.label_Senha.setText(_translate("Login_Dialog", "Senha"))
    def button_pressed(self):
        
       
        if ( login(self.lineEdit_Login.text(),self.lineEdit_Senha.text())==1):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Email_Dialog()
            self.ui.setupUi(self.window)
            Login_Dialog.hide()
            self.window.show()
       
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Dialog = QtWidgets.QDialog()
    ui = Ui_Login_Dialog()
    ui.setupUi(Login_Dialog)
    Login_Dialog.show()
    sys.exit(app.exec_())





        

