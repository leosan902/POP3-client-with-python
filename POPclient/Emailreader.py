# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Emailreader.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import socket
from ssl import wrap_socket
from os import linesep
import time,email
from POPclient import Client

      


class Ui_Email_Dialog(object):
    def setupUi(self, Email_Dialog):
        Email_Dialog.setObjectName("Email_Dialog")
        Email_Dialog.resize(966, 668)
        Email_Dialog.setAcceptDrops(False)
        self.pushButton_DeletarEmail = QtWidgets.QPushButton(Email_Dialog)
        self.pushButton_DeletarEmail.setGeometry(QtCore.QRect(490, 30, 75, 23))
        self.pushButton_DeletarEmail.setObjectName("pushButton_DeletarEmail")
        self.label_emails = QtWidgets.QLabel(Email_Dialog)
        self.label_emails.setGeometry(QtCore.QRect(130, 0, 151, 71))
        self.label_emails.setMinimumSize(QtCore.QSize(151, 71))
        self.label_emails.setObjectName("label_emails")
        self.pushButton_Voltar = QtWidgets.QPushButton(Email_Dialog)
        self.pushButton_Voltar.setGeometry(QtCore.QRect(660, 30, 75, 23))
        self.pushButton_Voltar.setObjectName("pushButton_Entrar_Voltar")
        self.pushButton_Voltar.clicked.connect(self.button_pressed)
        self.pushButton_Voltar.hide()
        self.pushButton_Sair = QtWidgets.QPushButton(Email_Dialog)
        self.pushButton_Sair.setGeometry(QtCore.QRect(320, 30, 75, 23))
        self.pushButton_Sair.setObjectName("pushButton_Sair")
        #self.pushButton_Sair.clicked.connect(self.button_pressed_sair)
   
        self.textBrowser_NEmails = QtWidgets.QTextBrowser(Email_Dialog)
        self.textBrowser_NEmails.setGeometry(QtCore.QRect(880, 30, 81, 41))
        self.textBrowser_NEmails.setObjectName("textBrowser_NEmails")
        self.label_NEmails = QtWidgets.QLabel(Email_Dialog)
        self.label_NEmails.setGeometry(QtCore.QRect(880, 10, 61, 20))
        self.label_NEmails.setObjectName("label_NEmails")
        self.listWidget_Emails = QtWidgets.QListWidget(Email_Dialog)
        self.listWidget_Emails.setGeometry(QtCore.QRect(60, 90, 881, 521))
        self.listWidget_Emails.setObjectName("listWidget_Emails")
        self.listWidget_Emails.itemClicked.connect(self.PrintClick)
        self.retranslateUi(Email_Dialog)
        self.textBrowser_email = QtWidgets.QTextBrowser(Email_Dialog)
        self.textBrowser_email.setGeometry(QtCore.QRect(60, 90, 881, 521))
        self.textBrowser_email.setObjectName("textBrowser_email")
        self.textBrowser_email.hide()
        self.pushButton_DeletarEmail.clicked.connect(self.button_pressed_deletar)
        QtCore.QMetaObject.connectSlotsByName(Email_Dialog)
        self.retranslateUi(Email_Dialog)
          #send_data(ssl_sock, 'STAT'+CRLF)
          #send_data2(ssl_sock, 'LIST '+CRLF)
          #send_data2(ssl_sock, 'RETR 4'+CRLF)
    
    def button_pressed_deletar(self):
      PopClient.deletarEmail(self.listWidget_Emails.currentItem().text())
      self.listWidget_Emails.takeItem(self.listWidget_Emails.currentRow())
      self.textBrowser_email.hide()
      self.listWidget_Emails.show()
      self.pushButton_Voltar.hide()
     

    def button_pressed(self):
      self.textBrowser_email.hide()
      self.listWidget_Emails.show()
      self.pushButton_Voltar.hide()
    
    def PrintClick(self):
      PopClient.identificarMensagem(self.listWidget_Emails.currentItem().text())
      
      self.listWidget_Emails.hide()
      self.textBrowser_email.show()
      self.pushButton_Voltar.show()  

    

    def retranslateUi(self, Email_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Email_Dialog.setWindowTitle(_translate("Email_Dialog", "Email Dialog"))
        self.label_emails.setText(_translate("Email_Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">Emails</span></p></body></html>"))
        self.pushButton_Voltar.setText(_translate("Email_Dialog", "Voltar"))
        self.pushButton_Sair.setText(_translate("Email_Dialog", "Sair da conta"))
        self.pushButton_DeletarEmail.setText(_translate("Email_Dialog", "Deletar email"))
        self.label_NEmails.setText(_translate("Email_Dialog", "Nº  de emails"))
        
    

        
    
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Email_Dialog = QtWidgets.QDialog()
    ui = Ui_Email_Dialog()
    ui.setupUi(Email_Dialog)
    PopClient = Client(ui)
    Email_Dialog.show()
    PopClient.login()
    PopClient.emails(ui)
    
       
    sys.exit(app.exec_())

