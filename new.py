def openwindow(self):
    self.window = QtGui.QMainWindow()
    self.ui = Ui_otherwindow()
    self.ui.setupUi(self.window)
    self.window.show()


data = []
data.append(self.IDKundennummer, self.kundennummer_txt.text(), self.txtFirmenname, self.Firma_text.text(), self.txtAlias,
            self.Alias_txt.text(), self.txtAnschrift, self.Strasse_text.text(), self.txtPLZ, self.PLZ_text.text(), self.txtOrt,
            self.Ort_text, self.txtLand, self.Land_text, self.txtEmail, self.Email_text, self.txtKontaktperson,
            self.Kontaktperson_text.text(), self.self.txtTelefonnummer, self.Telefonnummer_text.text())