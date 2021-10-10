from PyQt5.QtWidgets import *
from PyQt5.QtGui  import  QIcon , QFont , QImage , QPalette , QBrush , QPixmap
from PyQt5.QtCore import QSize , QRect
import sys , os
import threading
import cv2
import numpy as np

class one(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('finder')
        self.setWindowIcon(QIcon('detective1.png'))# put here window icon (full path)
        self.setGeometry(350,100,500,300)
        oImage = QImage("back2.jpg") # put here background image (full path)
        sImage = oImage.scaled(QSize(470,300))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.initwindow()
        self.show()
    def initwindow(self):
        self.vbox=QVBoxLayout()
        self.hbox=QHBoxLayout()
        self.hbox_2=QHBoxLayout()
        self.vbox.setContentsMargins(30,100,30,100)

        #---------------------------------
        label=QLabel('donner le dataSet dossier path : ')
        label.setStyleSheet('color: red')
        label.setFont(QFont('bold',11))

        self.line=QLineEdit()
        label1=QLabel('path : ')
        label1.setStyleSheet('color: grey')
        label1.setFont(QFont('ink free',15))

        self.hbox.addWidget(label1)
        self.hbox.addWidget(self.line)
        self.hbox.setContentsMargins(30,0,30,50)
        #--------------------------------------
        label_2=QLabel('Deposer votre photo ici : ')
        label_2.setStyleSheet('color: red')
        label.setFont(QFont('bold',11))

        self.line_2=QLineEdit()
        label1_2=QLabel('path : ')
        label1_2.setStyleSheet('color: grey')
        label1_2.setFont(QFont('ink free',15))

        self.hbox_2.addWidget(label1_2)
        self.hbox_2.addWidget(self.line_2)
        self.hbox_2.setContentsMargins(30,0,30,50)
        #------------------------------------------

        button=QPushButton('obtenir les images similaire')
        button.setStyleSheet('background-color:green')
        button.clicked.connect(self.b1)
        
        self.label2=QLabel('')
        self.label2.setStyleSheet('color: green')
        self.label2.setFont(QFont('ink free',12))

        self.vbox.addWidget(label)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(label_2)
        self.vbox.addLayout(self.hbox_2)
        self.vbox.addWidget(button)
        self.vbox.addWidget(self.label2)
        self.setLayout(self.vbox)
    def getpaths(self,path):
        l=[os.path.join(path,f) for f in os.listdir(path)] #list of images directories
        return l
    def b1(self):
        print(self.line.text())
        detector=cv2.ORB_create()
        flannparam=dict(algorithm=0,tree=5)
        flan=cv2.FlannBasedMatcher(flannparam,{})
        trainImg=cv2.imread(self.line_2.text(),0)
        trainkp,traindesc =detector.detectAndCompute(trainImg,None)

        path=self.line.text()
        ch=''
        for i in self.getpaths(path) :
            x=i.split("\\")[-1].split('.')[1]
            if (x=='jpg') or (x =='png'):
                QueryImg=cv2.imread(i,0)
                queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)

                if(len(queryKP)>=2) and (len(trainkp)>=2) :
                    matches=flan.knnMatch(np.asarray(queryDesc,np.float32),np.asarray(traindesc,np.float32), 2) #2
                    goodMatch=[]
                    for m,n  in matches : # n  train matches , m query matches
                        if (m.distance<0.75*n.distance):
                            goodMatch.append(m)
                    if (len(goodMatch)>26) :
                        os.startfile(i)
                        ch+='\n'+i.split("\\")[-1]
                    else :
                        print("no match")
        self.label2.setText(ch)
        
win=one()