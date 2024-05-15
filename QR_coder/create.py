from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import qrcode,os
class dialog(qt.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("إنشاء رمز QR")
        self.تحديد=qt.QPushButton("تحديد موقع حفظ الصورة")
        self.تحديد.setDefault(True)
        self.تحديد.clicked.connect(self.opinFile)        
        self.إظهار=qt.QLabel("موقع الحفظ هو")
        self.مسار=qt.QLineEdit()
        self.مسار.setReadOnly(True)
        self.مسار.setAccessibleName("موقع الحفظ هو")
        self.إظهار1=qt.QLabel("أكتب المحتوا هنا")
        self.المحتوا=qt.QLineEdit()
        self.المحتوا.setAccessibleName("أكتب المحتوا هنا")
        self.إنشاء=qt.QPushButton("إنشاء رمز QR")
        self.إنشاء.setDefault(True)
        self.إنشاء.clicked.connect(self.create)
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.تحديد)
        l.addWidget(self.إظهار)
        l.addWidget(self.مسار)
        l.addWidget(self.إظهار1)
        l.addWidget(self.المحتوا)
        l.addWidget(self.إنشاء)
    def opinFile(self):
        file=qt.QFileDialog()
        file.setAcceptMode(qt.QFileDialog.AcceptMode.AcceptOpen)
        if file.exec()==qt.QFileDialog.DialogCode.Accepted:
            self.مسار.setText(file.selectedFiles()[0])                                             
    def create(self):        
        if not self.مسار.text().lower().endswith(('.png', '.jpg', '.jpeg')):                    
            qt.QMessageBox.warning(self, "تنبيه", "عند تحديد مسار الحفظ يجب كتابة إسم ملف الصورة ووضع في نهايته امتداد صورة (png, jpg, jpeg)")
            return    
        if not self.المحتوا.text():        
            qt.QMessageBox.warning(self, "تنبيه", "يجب إدخال المحتوى")
            return
        الرمز=qrcode.make(self.المحتوا.text(),box_size=20)
        الرمز.save(self.مسار.text())                    
        qt.QMessageBox.information(self,"تنبيه","تم إنشاء رمز QR وحفظه")