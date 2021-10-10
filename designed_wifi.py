from PyQt5.QtWidgets import QPushButton , QTextEdit , QDialog , QGroupBox , QVBoxLayout , QLabel,QApplication
from PyQt5 import QtGui
import os , sys
import subprocess
os.chdir(r'C:\Users\user16\Desktop\png')
class window(QDialog):
    def __init__(self):
        super().__init__()
        self.title= ' wifi mot de passe'
        self.top=200
        self.left=200
        self.width=500
        self.height=300
        self.initwindow()
    def initwindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon('s4.png'))
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.setStyleSheet('background-color:black')
        vbox=QVBoxLayout()
        self.createlayout()
        self.tedit=QTextEdit()
        pix=QtGui.QPixmap('mylogo.png')
        image=QLabel(self)
        image.setPixmap(pix)

        vbox.addWidget(self.label)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.push)
        vbox.addWidget(self.tedit)
        vbox.addWidget(image)
        self.setLayout(vbox)

        self.show()
    def createlayout(self):
        self.label=QLabel('Ce programme cherche les mots de passe de wifi deja enregistreé')
        self.label.setStyleSheet('color:white')

        self.label2=QLabel('click the button to search')
        self.label2.setStyleSheet('color:red')
        self.label2.setFont(QtGui.QFont('sanserif',15))
        self.push=QPushButton('search',self)
        self.push.setStyleSheet('background-color:yellow')
        self.push.clicked.connect(self.wifi)

#http://www.wallpapers13.com/joker-comic-wallpaper-hd/
    def wifi(self):
        ch='searching wifi ...'+'\n'*2
        data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('cp1252').split('\n')
        profiles = [i.split(':')[1][1:-1] for i in data if 'Profil Tous les utilisateurs' in i  ]
        for i in profiles :
            r= subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('cp1252').split('\n')
            r= [ b.split(':')[1][1:-1] for b in r if '    Contenu de la cl‚' in b  ]
            try :
                ch=ch+('{:<30} |  {:<}'.format(i ,r[0]))+'\n'
            except IndexError :
                ch=ch+('{:<30} | {:<}' .format(i ,''))+'\n'
        self.tedit.setText(ch)
        self.tedit.setStyleSheet('color:rgb(200,50,70)')
        self.tedit.setFont(QtGui.QFont('sanserif',11))
app=QApplication(sys.argv)
w=window()
sys.exit(app.exec())


