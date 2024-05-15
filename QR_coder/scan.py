from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
from PyQt6.QtWidgets import QFileDialog
import cv2,pyperclip,webbrowser
class dialog(qt.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("مسح رمز QR")
        self.تحديد=qt.QPushButton("تحديد الصورة")
        self.تحديد.setDefault(True)
        self.تحديد.clicked.connect(self.opinFile)
        self.إظهار=qt.QLabel("مسار الصورة هو")
        self.مسار=qt.QLineEdit()
        self.مسار.setAccessibleName("مسار الصورة هو")
        self.مسار.setReadOnly(True)
        self.بدء=qt.QPushButton("بدء المسح")
        self.بدء.setDefault(True)
        self.بدء.clicked.connect(self.scan)
        self.إظهار1=qt.QLabel("نتيجة المسح هي")
        self.نتيجة=qt.QLineEdit()
        self.نتيجة.setReadOnly(True)
        self.نتيجة.setAccessibleName("نتيجة المسح هي")
        self.نسخ=qt.QPushButton("نسخ النتيجة")
        self.نسخ.setDefault(True)
        self.نسخ.clicked.connect(self.copy)
        self.رابط=qt.QPushButton("فتح الرابط")
        self.رابط.setDisabled(True)
        self.رابط.setDefault(True)
        self.رابط.clicked.connect(self.opin_link)
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.تحديد)
        l.addWidget(self.إظهار)
        l.addWidget(self.مسار)
        l.addWidget(self.بدء)
        l.addWidget(self.إظهار1)
        l.addWidget(self.نتيجة)
        l.addWidget(self.نسخ)
        l.addWidget(self.رابط)
    
    def opinFile(self):
        file, _ = QFileDialog.getOpenFileName(self, "تحديد صورة", "", "صور (*.png *.jpg *.jpeg)")
        if file:
            self.مسار.setText(file)                                 
    
    def scan(self):        
        الصورة=cv2.imread(self.مسار.text())
        الماسح=cv2.QRCodeDetector()
        try:
            البيانات, bbox, _ = الماسح.detectAndDecodeMulti(الصورة)
            if bbox is not None:
                self.نتيجة.setText(البيانات)
                self.نتيجة.setFocus()
            else:
                qt.QMessageBox.warning(self,"تنبيه","لا يوجد رمز QR في الصورة")
            if البيانات.startswith("http"):
                self.رابط.setDisabled(False)
        except:
            qt.QMessageBox.warning(self,"تنبيه","حدث خطأ في مسح الصورة, ربما الصورة فارغة أو غير صالحة")
    def copy(self):
        pyperclip.copy(self.نتيجة.text())    
    def opin_link(self):
        webbrowser.open(self.نتيجة.text())