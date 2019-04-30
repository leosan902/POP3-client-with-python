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
        Email_Dialog.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowMaximizeButtonHint|QtCore.Qt.WindowCloseButtonHint )
        self.pushButton_DeletarEmail = QtWidgets.QPushButton(Email_Dialog)
        self.pushButton_DeletarEmail.setGeometry(QtCore.QRect(490, 30, 75, 23))
        self.pushButton_DeletarEmail.setObjectName("pushButton_DeletarEmail")
        self.pushButton_DeletarEmail.hide()
        self.label_emails = QtWidgets.QLabel(Email_Dialog)
        self.label_emails.setGeometry(QtCore.QRect(130, 0, 151, 71))
        self.label_emails.setMinimumSize(QtCore.QSize(151, 71))
        self.label_emails.setObjectName("label_emails")
        self.label_emails.hide()
        self.pushButton_Voltar = QtWidgets.QPushButton(Email_Dialog)
        self.pushButton_Voltar.setGeometry(QtCore.QRect(660, 30, 75, 23))
        self.pushButton_Voltar.setObjectName("pushButton_Entrar_Voltar")
        self.pushButton_Voltar.clicked.connect(self.button_pressed_Voltar)
        self.pushButton_Voltar.hide()
        self.pushButton_Sair = QtWidgets.QPushButton(Email_Dialog)
        self.pushButton_Sair.setGeometry(QtCore.QRect(360, 30, 75, 23))
        self.pushButton_Sair.setObjectName("pushButton_Sair")
        self.pushButton_Sair.hide()
        self.pushButton_Sair.clicked.connect(self.button_pressed_sair)
        self.textBrowser_NEmails = QtWidgets.QTextBrowser(Email_Dialog)
        self.textBrowser_NEmails.setGeometry(QtCore.QRect(880, 30, 81, 41))
        self.textBrowser_NEmails.setObjectName("textBrowser_NEmails")
        self.textBrowser_NEmails.hide()
        self.label_NEmails = QtWidgets.QLabel(Email_Dialog)
        self.label_NEmails.setGeometry(QtCore.QRect(880, 10, 61, 20))
        self.label_NEmails.setObjectName("label_NEmails")
        self.label_NEmails.hide()
        self.listWidget_Emails = QtWidgets.QListWidget(Email_Dialog)
        self.listWidget_Emails.setGeometry(QtCore.QRect(60, 90, 881, 521))
        self.listWidget_Emails.setObjectName("listWidget_Emails")
        self.listWidget_Emails.itemClicked.connect(self.PrintClick)
        self.listWidget_Emails.hide()
        self.textBrowser_email = QtWidgets.QTextBrowser(Email_Dialog)
        self.textBrowser_email.setGeometry(QtCore.QRect(60, 90, 881, 521))
        self.textBrowser_email.setObjectName("textBrowser_email")
        self.textBrowser_email.hide()
        self.pushButton_Entrar = QtWidgets.QPushButton(Email_Dialog)
        self.pushButton_Entrar.setGeometry(QtCore.QRect(100, 300, 75, 23))
        self.pushButton_Entrar.setObjectName("pushButton")
        self.pushButton_Reset = QtWidgets.QPushButton(Email_Dialog);
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.pushButton_Reset.setGeometry(QtCore.QRect(390, 630, 131, 23))
        self.pushButton_Reset.hide()
        self.widget = QtWidgets.QWidget(Email_Dialog)
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
        self.pushButton_DeletarEmail.clicked.connect(self.button_pressed_deletar)
        self.pushButton_Entrar.clicked.connect(self.button_pressed_Entrar)
        self.pushButton_Reset.clicked.connect(self.button_pressed_Reset)
        self.QMessageBox_Error_Login = QtWidgets.QMessageBox(Email_Dialog)
        self.QMessageBox_Error_Login.setText("Algum dos campos esta incorreto")
        self.QMessageBox_Error_Login.setWindowTitle("Login erro")
        QtCore.QMetaObject.connectSlotsByName(Email_Dialog)
        self.retranslateUi(Email_Dialog)
         
    def button_pressed_sair(self):
        self.changeLogin()
        
    def button_pressed_Reset(self):
        PopClient.resetEmail()

    def button_pressed_deletar(self):
      PopClient.deletarEmail(self.listWidget_Emails.currentItem().text())
      self.listWidget_Emails.takeItem(self.listWidget_Emails.currentRow())
      self.textBrowser_email.hide()
      self.listWidget_Emails.show()
      self.pushButton_Voltar.hide()
     
    def button_pressed_Entrar(self):
        
        try:
         
         data=PopClient.login(self.lineEdit_EmailServer.text(),self.lineEdit_Port.text(),self.lineEdit_Login.text(),self.lineEdit_Senha.text())
         if(data==1):
             PopClient.emails(ui)
             self.pushButton_Entrar.hide()
             self.changeWindow()
         else:
             return -1
        except:
          self.QMessageBox_Error_Login.show()
          self.lineEdit_Senha.clear()
          
          
          
        
        
         

    def changeWindow(self):
         self.pushButton_Sair.show()
         self.label_Sever.hide()
         self.label_Login.hide()
         self.label_port.hide()
         self.label_Senha.hide()
         self.lineEdit_EmailServer.hide()
         self.lineEdit_Senha.hide()
         self.lineEdit_Port.hide()
         self.lineEdit_Login.hide()
         self.textBrowser_NEmails.show()
         self.label_NEmails.show()
         self.widget.hide()
         self.label_emails.show()
         self.listWidget_Emails.show()
         self.pushButton_DeletarEmail.show()
         self.lineEdit_Senha.clear()
         self.pushButton_Reset.show()

    def changeLogin(self):
         self.label_Sever.show()
         self.label_Login.show()
         self.label_port.show()
         self.label_Senha.show()
         self.widget.show()
         self.lineEdit_EmailServer.show()
         self.lineEdit_Senha.show()
         self.lineEdit_Port.show()
         self.lineEdit_Login.show()
         self.textBrowser_NEmails.hide()
         self.label_NEmails.hide()
         self.label_emails.hide()
         self.listWidget_Emails.hide()
         self.pushButton_DeletarEmail.hide()
         self.pushButton_Sair.hide()
         self.pushButton_Entrar.show()
         self.pushButton_Reset.hide()

    def button_pressed_Voltar(self):
      self.textBrowser_email.hide()
      self.listWidget_Emails.show()
      self.pushButton_Voltar.hide()
      PopClient.quit()
    
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
        self.pushButton_Entrar.setText(_translate("Email_Dialog", "Ok"))
        self.label_Sever.setText(_translate("Email_Dialog", "Email Server"))
        self.label_port.setText(_translate("Email_Dialog", "Porta"))
        self.label_Login.setText(_translate("Email_Dialog", "Login"))
        self.label_Senha.setText(_translate("Email_Dialog", "Senha"))
        self.pushButton_Reset.setText(_translate("Email_Dialog", "Reset  Emails Deletados"))
    

        
    
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Email_Dialog = QtWidgets.QDialog()
    ui = Ui_Email_Dialog()
    ui.setupUi(Email_Dialog)
    PopClient = Client(ui)
    Email_Dialog.show()
    
    
    
       
    sys.exit(app.exec_())

