# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guimatcher.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GUIMatcher(object):
    def setupUi(self, GUIMatcher):
        GUIMatcher.setObjectName("GUIMatcher")
        GUIMatcher.resize(400, 370)
        self.text = QtWidgets.QLabel(GUIMatcher)
        self.text.setGeometry(QtCore.QRect(30, 30, 340, 120))
        self.text.setObjectName("text")
        self.matchButton = QtWidgets.QPushButton(GUIMatcher)
        self.matchButton.setGeometry(QtCore.QRect(30, 300, 340, 40))
        self.matchButton.setObjectName("matchButton")
        self.text_2 = QtWidgets.QLabel(GUIMatcher)
        self.text_2.setGeometry(QtCore.QRect(30, 180, 340, 15))
        self.text_2.setObjectName("text_2")
        self.appFile = QtWidgets.QLineEdit(GUIMatcher)
        self.appFile.setGeometry(QtCore.QRect(30, 200, 340, 20))
        self.appFile.setObjectName("appFile")
        self.text_3 = QtWidgets.QLabel(GUIMatcher)
        self.text_3.setGeometry(QtCore.QRect(30, 240, 340, 15))
        self.text_3.setObjectName("text_3")
        self.proFile = QtWidgets.QLineEdit(GUIMatcher)
        self.proFile.setGeometry(QtCore.QRect(30, 260, 340, 20))
        self.proFile.setObjectName("proFile")

        self.retranslateUi(GUIMatcher)
        QtCore.QMetaObject.connectSlotsByName(GUIMatcher)

    def retranslateUi(self, GUIMatcher):
        _translate = QtCore.QCoreApplication.translate
        GUIMatcher.setWindowTitle(_translate("GUIMatcher", "Dialog"))
        self.text.setText(_translate("GUIMatcher", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">Party Matching</span></p><p><span style=\" font-size:9pt;\">Logiciel de couplage optimal entre deux listes d\'éléments<br/>selon l\'algorithme de Gale-Shapley</span></p><p><span style=\" font-size:9pt;\">Ce logiciel a été développé en 2016 par André nasturas et<br/>Benjamin Loglisci dans le cadre du projet d\'études du cours<br/>d\'Intelligence Artificielle et Recherche Opérationnelle (3I025<br/> de l\'UPMC.</span></p></body></html>"))
        self.matchButton.setText(_translate("GUIMatcher", "Matcher"))
        self.text_2.setText(_translate("GUIMatcher", "<html><head/><body><p><span style=\" font-size:9pt;\">Choisissez un fichier contenant les données des demandeurs :</span></p></body></html>"))
        self.text_3.setText(_translate("GUIMatcher", "<html><head/><body><p><span style=\" font-size:9pt;\">Choisissez un fichier contenant les données des demandeurs :</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUIMatcher = QtWidgets.QDialog()
    ui = Ui_GUIMatcher()
    ui.setupUi(GUIMatcher)
    GUIMatcher.show()
    sys.exit(app.exec_())
