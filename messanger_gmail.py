import sys,os
import sqlite3 as sq
from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
import datetime as d
import smtplib , email
import time
os.chdir(r'C:\Users\user16\Desktop\png')

#########################opening an sql base#################################
con=sq.connect('messanger1.sq3')
cur=con.cursor()
cur.execute("create table if not exists Client (id_c integer primary key AUTOINCREMENT"+
", nom_c text ,addresse_c text , password_c text )")
cur.execute("create table if not exists friend (id_f integer primary key AUTOINCREMENT "+
", nom_f text , email_f text ,len_init integer,messages text) ")
con.commit()


##############################fourth window (messanger)##################################
class mainmessage(QDialog):
    def __init__(self):
        super().__init__()
        self.initwindow()
        oImage = QImage("back2.jpg")
        sImage = oImage.scaled(QSize(500,300))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)
        self.show()
    def initwindow(self):
        print('heloo')
############################## third window ####################################""########
class create(QDialog):
    def __init__(self):
        super().__init__()
        self.initwindow()
        oImage = QImage("back2.jpg")
        sImage = oImage.scaled(QSize(500,300))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)
        self.show()
    def initwindow(self) :
        self.setWindowTitle('dialerr')
        self.setWindowIcon(QtGui.QIcon('oo.png'))
        self.setGeometry(400,200,430,300)
        self.vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()
        hbox3=QHBoxLayout()
        hbox4=QHBoxLayout()
        hbox5=QHBoxLayout()


        self.tedit=QTextEdit()

        self.email=self.line()
        self.password=self.line()
        self.name=self.line()
        self.nickname=self.line()
        self.passwordN =self.line()
        self.passwordN.setEchoMode(QLineEdit.Password)

        hbox1.addWidget(self.label(' name :','orange'))
        hbox1.addWidget(self.name)
        hbox2.addWidget(self.label(' adress email :','orange'))
        hbox2.addWidget(self.email)
        hbox3.addWidget(self.label(' password :','orange'))
        hbox3.addWidget(self.password)


        hbox.addWidget(self.button(' save ',85,35,'blue'))


        self.vbox.addLayout(hbox1)
        self.vbox.addLayout(hbox2)
        self.vbox.addLayout(hbox3)
        self.vbox.addLayout(hbox)
        hbox.setContentsMargins(100,0,0,0)
        self.setLayout(self.vbox)
        self.show()
    def label(self,message=' ',color='red'):
        l=QLabel(message,self)
        l.setStyleSheet('color:'+color)
        l.setFont(QtGui.QFont('sanserif',9))
        return l
    def button(self,name=' ',a=50,c=50,color='rgb(0,5,150)'):
        b=QPushButton(name)
        b.setStyleSheet('background-color:'+color)
        b.setMaximumSize(a,c)
        if name==' save ' :
            b.clicked.connect(self.save)
        return b
    def save(self):


        cur.execute("insert into Client (nom_c ,addresse_c, password_c ) values (?,?,?)",(self.name.text(),self.email.text(),self.password.text()))
        con.commit()
        self.win=MainWindow()
        self.close()

    def line(self,color='green',width=200):
        lline=QLineEdit()
        lline.setStyleSheet('background-color:'+color)
        lline.setMaximumWidth(width)
        lline.setTextMargins(8,3,3,3)
        lline.setFont(QtGui.QFont('sanserif',10))
        return lline
################################## First Window ########################################################################
class MainWindow(QDialog):
    def __init__(self):
       QWidget.__init__(self)
       self.initwindow()
       oImage = QImage("back2.jpg")
       sImage = oImage.scaled(QSize(500,300))                   # resize Image to widgets size
       palette = QPalette()
       palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
       self.setPalette(palette)

       self.show()
    def initwindow(self) :
        global name , password

        self.setWindowTitle('dialerr')
        self.setWindowIcon(QtGui.QIcon('oo.png'))
        self.setGeometry(400,200,430,300)
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        hbox1=QHBoxLayout()
        hbox2=QHBoxLayout()


        self.tedit=QTextEdit()

        self.nameline=self.line()
        self.passwordline=self.line()
        self.passwordline.setEchoMode(QLineEdit.Password)

        hbox1.addWidget(self.label(' Please insert name :','orange'))
        hbox1.addWidget(self.nameline)
        hbox2.addWidget(self.label(' insert your password :','orange'))
        hbox2.addWidget(self.passwordline)
        hbox.addWidget(self.label(" you don't have an account ?" ))
        hbox.addWidget(self.button(' Create account ',85,35,'blue'))

        name=self.nameline.text()
        password=self.passwordline.text()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.button('Log in',40,35,'grey'))
        vbox.addLayout(hbox)
        hbox.setContentsMargins(100,0,0,0)
        self.setLayout(vbox)
        self.show()
    def label(self,message=' ',color='red'):
        l=QLabel(message,self)
        l.setStyleSheet('color:'+color)
        l.setFont(QtGui.QFont('sanserif',9))
        return l
    def button(self,name=' ',a=50,c=50,color='rgb(0,5,150)'):
        b=QPushButton(name)
        b.setStyleSheet('background-color:'+color)
        b.setMaximumSize(a,c)

        if name=='Log in' :
            b.clicked.connect(self.log_in)
        if name==' Create account ' :
            b.clicked.connect(self.create_a)

        return b
    def line(self,color='green',width=200):
        lline=QLineEdit()
        lline.setStyleSheet('background-color:'+color)
        lline.setMaximumWidth(width)
        lline.setTextMargins(8,3,3,3)
        lline.setFont(QtGui.QFont('sanserif',10))
        return lline
    def log_in(self):

        self.win = log()
        self.close()
    def create_a(self):
        self.win=create()
        self.close()
############################### second window #######################################################
class log(QWidget):
    def __init__(self):
        super().__init__()
        self.name=name
        self.password=password
        cur.execute("select addresse_c  from Client where nom_c = '{}'".format(self.name))
        self.email=cur.fetchall()[0][0]
        self.initWindow()
        oImage = QImage("back2.jpg")
        sImage = oImage.scaled(QSize(500,300))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)
        self.show()
    def initWindow(self) :
        self.setWindowTitle('dialerr')
        self.setWindowIcon(QtGui.QIcon('oo.png'))
        self.setGeometry(400,200,450,450)
        self.vbox=QVBoxLayout()
        self.greatvbox=QVBoxLayout()
        vbox1=QVBoxLayout()
        hbox=QHBoxLayout()
        hbox1=QHBoxLayout()
        self.tedit=QTextEdit()
        self.vbox.addWidget(self.label(' List of freinds :'))
        self.lista=self.list()
        self.vbox.addWidget(self.lista)
        vbox1.addWidget(self.button(' Add friend ',150,35,'orange'))
        vbox1.addWidget(self.button(' delete friend ',150,35, 'orange'))
        vbox1.addWidget(self.button(' Exit ',150,35, 'orange'))
        hbox.addLayout(self.vbox)
        hbox.addLayout(vbox1)
        self.greatvbox.addLayout(hbox)
        #################
        self.label_messageavec=self.label("messages avec : ")
        self.label_writemessage=self.label("write a message ..")
        self.messagesender=self.line('pink',350)
        self.label_detect=self.label(" Hit enter to send message \ click on refresh to check new message  ",8,'grey')
        hbox1.addWidget(self.messagesender)
        hbox1.addWidget(self.button(' refresh ',100,30,'green'))
        ######################
        self.greatvbox.addWidget(self.label_messageavec)
        self.greatvbox.addWidget(self.tedit)
        self.greatvbox.addWidget(self.label_writemessage)
        self.greatvbox.addLayout(hbox1)
        self.greatvbox.addWidget(self.label_detect)
        self.setLayout(self.greatvbox)
        self.show()
    def list(self,l=[]):
        l=QListWidget()
        h=cur.execute("select * from friend ")
        for i in h :
            l.insertItem(i[0],i[1])
            l.clicked.connect(self.slotlist)
        return l

    def label(self,message=' ',a=11,color='red'):
        l=QLabel(message,self)
        l.setStyleSheet('color:'+color)
        l.setFont(QtGui.QFont('sanserif',a))
        return l
    def button(self,name=' ',a=50,c=50,color='rgb(0,5,150)'):
        b=QPushButton(name)
        b.setStyleSheet('background-color:'+color)
        b.setMaximumSize(a,c)
        if name==' Add friend ':
            b.clicked.connect(self.add)
        if name==' delete friend ':
            b.clicked.connect(self.delete)
        if name==' Exit ' :
            b.clicked.connect(self.exit)
        if name ==' refresh ' :
            b.clicked.connect(self.fetch)
        return b
    def add(self):
        text,ok=QInputDialog.getText(self,'add freind',"write your friend's name",QLineEdit.Normal)
        if ok and text != "" :
            text1,ok1 =QInputDialog.getText(self,'add freind',"write your friend's email",QLineEdit.Normal)
            if ok1 and text1 != "" :
                try :
                    print(len(self.recive_mail_one(text1)[0]))
                    cur.execute("insert into friend(nom_f, email_f, len_init,messages) values(?,?,?,?)",(text,text1,len(self.recive_mail_one(text1)[0]),""))
                    con.commit()
                except IndexError :
                    cur.execute("insert into friend(nom_f, email_f, len_init,messages) values(?,?,?,?)",(text,text1,0,""))
                    cur.execute("select id_f from friend where nom_f ='{}'".format(text))
                    x=cur.fetchall()[0][0]
                    con.commit()
                    self.lista.insertItem(x,text)

    def delete(self):
        text,ok=QInputDialog.getText(self,'delete freind',"write ",QLineEdit.Normal)
        if ok and text != "" :
            cur.execute(" delete from friend where nom_f = '{}'".format(text))
            con.commit()
    def exit(self):
        self.exit()
    def slotlist(self):
        self.items=self.lista.currentItem()
        cur.execute("select messages from friend where nom_f ='{}'".format(str(self.items.text()) ))
        h=cur.fetchall()[0][0]
        self.tedit.setText(h)
        self.label_messageavec.setText( "messages avec : "+str(self.items.text()) )

    def line(self,color='green',width=200):
        lline=QLineEdit()
        lline.setStyleSheet('background-color:'+color)
        lline.setMaximumWidth(width)
        lline.setTextMargins(8,3,3,3)
        lline.setFont(QtGui.QFont('sanserif',10))
        if color=='pink':
            lline.returnPressed.connect(self.pink)
        return lline
    def recive_mail_one(self,mail) :
        import imaplib , email

        imap_url='imap.gmail.com'
        def search(key, value, con):
            result, data =con.search(None ,key , '"{}"'.format(value))
            return data
        def get_body(msg) :
            if msg.is_multipart():
                return get_body(msg.get_payload(0))
            else :
                return msg.get_payload(None , True)
        def get_emails(result_bytes):
            msgs=[]
            for num in result_bytes[0].split() :
                typ , data = con.fetch(num,'(RFC822)')
                msgs.append(data)
            return msgs
        con =imaplib.IMAP4_SSL(imap_url)
        con.login(self.email,self.password)
        con.select('INBOX')


        x=search('FROM',mail,con)
        print(x)
        msgs=get_emails(x)

        return x[0].decode('utf-8').split(' ') , get_body(email.message_from_bytes(msgs[-1][0][1])).decode('utf-8')
    def send_email(self,email,msg):

        try:
            server=smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            #put there ur mail and password
            server.login(self.email,self.password)
            message='subject {} \n\n {}'.format(' ',msg)
            server.sendmail(self.email,email,message)
            server.quit()
            return 1
        except:
            print('shit , email failed to send')
    def pink(self): # this function woerk when you hit enter after writing a message
        print('hello')

        cur.execute("select email_f from friend where nom_f = '{}'".format(str(self.items.text()) ))
        em=cur.fetchall()
        self.send_email(em[0][0],self.messagesender.text())
        time=str(d.datetime.today())[:-10:]
        cur.execute("select messages from friend where nom_f ='{}'".format(str(self.items.text()) ))
        ch1=cur.fetchall()[0][0]
        ch1=ch1+self.name+'('+time+')----->'+self.messagesender.text()+'\n'
        self.tedit.clear()
        self.tedit.setText(ch1)

        cur.execute('update friend set messages = "{}"  where nom_f = "{}"'.format(ch1,str(self.items.text()) ))
        con.commit()

    def fetch(self ):
        name=self.items.text()
        cur.execute("select messages from friend where nom_f ='{}'".format(str(self.items.text()) ))
        ch1=cur.fetchall()[0][0]
        cur.execute("select email_f from friend where nom_f = '{}'".format(str(self.items.text()) ))
        mail=cur.fetchall()[0][0]
        cur.execute("select len_init from friend where nom_f = '{}'".format(name))
        h=cur.fetchall()

        try :
            if h[0][0]<len(self.recive_mail_one(mail)[0]) :
                c=name+'-----> '+self.recive_mail_one(mail)[1]+'\n'
                ch=ch1+c
                cur.execute("update friend set messages = '{}'  where nom_f = '{}'".format(ch,name ))
                cur.execute("update friend set len_init= {} where nom_f = '{}'".format(len(self.recive_mail_one(mail)[0]),name ))
                con.commit()
                self.tedit.clear()
                self.tedit.setText(ch)
                self.label_detect.clear()
                self.label_detect.setText('New message found !')
            else :
                self.label_detect.clear()
                self.label_detect.setText('No new message detected !')
        except IndexError :
            self.label_detect.clear()
            self.label_detect.setText('No new message detected !')

if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())
    app1 = QCoreApplication(sys.argv)

    playlist = QMediaPlaylist()
    url = QUrl.fromLocalFile("Massari-RealLoveOfficialVideo.mp3")
    playlist.addMedia(QMediaContent(url))
    playlist.setPlaybackMode(QMediaPlaylist.Loop)

    player = QMediaPlayer()
    player.setPlaylist(playlist)
    player.play()
    app1.exec()
