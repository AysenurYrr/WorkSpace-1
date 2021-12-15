"""
PyQt5 ile kullanıcı login ekranı tasarlayın.
Önceden belirlenen bir kullanıcı login olduktan sonra ekrana hoşgeldin yazısı yazsın.


"""

import sys
import sqlite3 
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.baglantı_olustur()

        self.init_ui()
    
    
    def baglantı_olustur(self):
        baglanti = sqlite3.connect("user_data.db")

        self.cursor = baglanti.cursor()

        self.cursor.execute("Create Table If not exists üyeler (kullanici_adı TEXT,parola TEXT)")
        
        baglanti.commit()

    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giris Yap")
        self.kayit = QtWidgets.QPushButton("Kayıt Ol")
        self.yazi_alani=QtWidgets.QLabel("Merhaba")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.kayit)

        h_box=QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)



        self.show()
    def login(self):

        adi = self.kullanici_adi.text()
        par = self.parola.text()


        self.cursor.execute("Select * From üyeler where kullanici_adı = ? and parola = ?",(adi,par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok\n Lütfen tekrar deneyin.")
        else:
            self.yazi_alani.setText("Hoşgeldin " + adi)
            
    def kayit_ol(self):
        pass

app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())