from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import about,scan,create
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR coder")
        self.القائمة=qt.QListWidget()        
        self.القائمة.clicked.connect(self.c)
        self.القائمة.addItem("مسح رمز QR")
        self.القائمة.addItem("إنشاء رمز QR")
        self.القائمة.addItem("عن المطور")
        qt1.QShortcut("return",self).activated.connect(self.c)
        l=qt.QVBoxLayout()        
        l.addWidget(self.القائمة)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)        
    def c(self):
        العناصر=self.القائمة.currentRow()
        if العناصر==0:
            scan.dialog(self).exec()
        if العناصر==1:
            create.dialog(self).exec()
        if العناصر==2:
            about.dialog(self).exec()
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()