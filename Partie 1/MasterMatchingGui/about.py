# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(400, 300)
        self.close = QtWidgets.QPushButton(About)
        self.close.setGeometry(QtCore.QRect(30, 230, 340, 40))
        self.close.setObjectName("close")
        self.text = QtWidgets.QLabel(About)
        self.text.setGeometry(QtCore.QRect(30, 30, 340, 180))
        self.text.setObjectName("text")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Dialog"))
        self.close.setText(_translate("About", "Fermer"))
        self.text.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">Party Matching</span></p><p><span style=\" font-size:9pt;\">Logiciel de couplage optimal entre deux listes d\'éléments<br/>selon l\'algorithme de Gale-Shapley</span></p><p><span style=\" font-size:9pt;\">Ce logiciel a été développé en 2016 par André nasturas et<br/>Benjamin Loglisci dans le cadre du projet d\'études du cours<br/>d\'Intelligence Artificielle et Recherche Opérationnelle (3I025<br/> de l\'UPMC.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())
