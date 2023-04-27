
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from  PyQt5.QtGui import QPixmap, QBrush, QPalette

def pon():
    dia = QDialog()
    win_card = QWidget()
    win_card.setWindowTitle('Weather forecast') 
    win_card.resize(700, 700)

    dia.setStyleSheet("""
            QWidget {
                background: #fcfc8b;
                background-image: url(D:/Projects/maze/1772.jpg); 
                background-position: center;
                border-radius: 11px;    

            }
            
            QPushButton{
                background: #03dbfc;
                color: #ffffff;
                border-radius: 11px;
                min-width: 6em;    
                min-height: 2em;
                font-family: Arial;
                font: bold 18px;      
            }
            
            QLineEdit{
                background: rgba(255, 255, 255, 40);
                opacity: 0;
                min-width: 20em;
                max-height: 7em;
                font-family: Arial;
                font: bold 18px;
                border-color: beige;
                color:#8903ff;
                
            }

            QLabel{
                color: #8903ff;
                font: bold 18px;
                background: rgba(255, 255, 255, 40);
                opacity: 0;
                

            }

    """
    )


    oneEdit = QLineEdit()
    oneEdit.setPlaceholderText("Input your city or  town")

    twoEdit = QLineEdit()
    twoEdit.setReadOnly(True) 

    threeEdit = QLineEdit()
    threeEdit.setReadOnly(True) 

    fourEdit = QLineEdit()
    fourEdit.setReadOnly(True) 

    fiveEdit = QLineEdit()
    fiveEdit.setReadOnly(True) 

    sixEdit = QLineEdit()
    sixEdit.setReadOnly(True) 

    sevenEdit = QLineEdit()
    sevenEdit.setReadOnly(True) 

    eightEdit = QLineEdit()
    eightEdit.setReadOnly(True) 

    nineEdit = QLineEdit()
    nineEdit.setReadOnly(True) 

    tenEdit = QLineEdit()
    tenEdit.setReadOnly(True) 

    weatherButton = QPushButton("Find out weather")

    oneH = QHBoxLayout()
    twoH = QHBoxLayout()
    threeH = QHBoxLayout()
    fourH = QHBoxLayout()
    fiveH = QHBoxLayout()
    sixH = QHBoxLayout()
    sevenH = QHBoxLayout()
    eightH = QHBoxLayout()
    nineH = QHBoxLayout()
    tenH = QHBoxLayout()
    elevenH = QHBoxLayout()
    twelveH = QHBoxLayout()

    im = QPixmap("D:\\Projects\\maze\\2275.png")
    im = im.scaledToWidth(250)
    im = im.scaledToHeight(250) 
    label = QLabel()
    label.setPixmap(im)

    im1 = QPixmap("D:\\Projects\\maze\\temperature-feels-like-icon-495x512-ylzv705f.png")
    im1 = im1.scaledToWidth(50)
    im1 = im1.scaledToHeight(50) 
    label1 = QLabel()
    label1.setPixmap(im1) 
    label1.hide()

    im2 = QPixmap("D:\\Projects\\maze\\1839341.png")
    im2 = im2.scaledToWidth(50)
    im2 = im2.scaledToHeight(50) 
    label2 = QLabel()
    label2.setPixmap(im2)

    im3 = QPixmap("D:\\Projects\\maze\\climate-control-home-temperature-png-17.png")
    im3 = im3.scaledToWidth(50)
    im3 = im3.scaledToHeight(50) 
    label3 = QLabel()
    label3.setPixmap(im3) 
    label3.hide()

    im4 = QPixmap("D:\\Projects\\maze\\1839341.png")
    im4 = im4.scaledToWidth(50)
    im4 = im4.scaledToHeight(50) 
    label4 = QLabel()
    label4.setPixmap(im4) 
    label4.hide()

    im5 = QPixmap("D:\\Projects\\maze\\728093.png")
    im5 = im5.scaledToWidth(50)
    im5 = im5.scaledToHeight(50) 
    label5 = QLabel()
    label5.setPixmap(im5) 
    label5.hide()

    im6 = QPixmap("D:\\Projects\\maze\\661295.png")
    im6 = im6.scaledToWidth(50)
    im6 = im6.scaledToHeight(50) 
    label6 = QLabel()
    label6.setPixmap(im6) 
    label6.hide()

    im7 = QPixmap("D:\\Projects\\maze\\6740814.png")
    im7 = im7.scaledToWidth(50)
    im7 = im7.scaledToHeight(50) 
    label7 = QLabel()
    label7.setPixmap(im7) 
    label7.hide()

    im8 = QPixmap("D:\\Projects\\maze\\3095235.png")
    im8 = im8.scaledToWidth(50)
    im8 = im8.scaledToHeight(50) 
    label8 = QLabel()
    label8.setPixmap(im8) 
    label8.hide()

    im9 = QPixmap("D:\\Projects\\maze\\img_315328.png")
    im9 = im9.scaledToWidth(40)
    im9 = im9.scaledToHeight(40) 
    label9 = QLabel()
    label9.setPixmap(im9) 
    label9.hide()

    im10 = QPixmap("D:\\Projects\\maze\\weather-overcast.png")
    im10 = im10.scaledToWidth(50)
    im10 = im10.scaledToHeight(50) 
    label10 = QLabel()
    label10.setPixmap(im10) 
    label10.hide()

    im0 = QPixmap("D:\\Projects\\maze\\8354127.png")
    im0 = im0.scaledToWidth(50)
    im0 = im0.scaledToHeight(50) 
    label0 = QLabel()
    label0.setPixmap(im0)




    oneV = QVBoxLayout()



    oneV.addLayout(oneH)

    oneV.addLayout(twoH)

    oneV.addLayout(threeH)

    oneV.addLayout(fourH)

    oneV.addLayout(fiveH)

    oneV.addLayout(sixH)

    oneV.addLayout(sevenH)

    oneV.addLayout(eightH)

    oneV.addLayout(nineH)

    oneV.addLayout(tenH)

    oneV.addLayout(elevenH)

    oneV.addLayout(twelveH)



    oneH.addStretch(1)
    oneH.addWidget(label)
    oneH.addStretch(1)

    twoH.addStretch(1)
    twoH.addWidget(label0)
    twoH.addWidget(oneEdit)
    twoH.addStretch(1)

    threeH.addStretch(1)
    threeH.addWidget(label3)
    threeH.addWidget(twoEdit)
    threeH.addStretch(1)

    fourH.addStretch(1)
    fourH.addWidget(label1)
    fourH.addWidget(threeEdit)
    fourH.addStretch(1)

    fiveH.addStretch(1)
    fiveH.addWidget(label4)
    fiveH.addWidget(fourEdit)
    fiveH.addStretch(1)

    sixH.addStretch(1)
    sixH.addWidget(label5)
    sixH.addWidget(fiveEdit)
    sixH.addStretch(1)

    sevenH.addStretch(1)
    sevenH.addWidget(label6)
    sevenH.addWidget(sixEdit)
    sevenH.addStretch(1)

    eightH.addStretch(1)
    eightH.addWidget(label7)
    eightH.addWidget(sevenEdit)
    eightH.addStretch(1)

    nineH.addStretch(1)
    nineH.addWidget(label8)
    nineH.addWidget(eightEdit)
    nineH.addStretch(1)

    tenH.addStretch(1)
    tenH.addWidget(label9)
    tenH.addWidget(nineEdit)
    tenH.addStretch(1)

    elevenH.addStretch(1)
    elevenH.addWidget(label10)
    elevenH.addWidget(tenEdit)
    elevenH.addStretch(1)

    twelveH.addWidget(weatherButton)
    API = 'f81703c1f3b81ad93e6644153c4a426e'
    #url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API}'
    def weather():
        city = oneEdit.text()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            likefeel = data["main"]["feels_like"]
            pressure = data["main"]["pressure"]
            humidity = data["main"]["humidity"]
            temp_min = data["main"]["temp_min"]
            sealevel = data["main"]["sea_level"]
            temp_max = data["main"]["temp_max"]
            windspeed = data["wind"]["speed"]
            clouds = data["clouds"]["all"]

            label1.show()
            label3.show()
            label4.show()
            label5.show()
            label6.show()
            label7.show()
            label8.show()
            label9.show()
            label10.show()
            

            temp1 = temp - 273
            temp2 = round(temp1, 0)

            likefeel1 = likefeel - 273
            likefeel2 = round(likefeel1, 0)

            temp_min1 = temp_min - 273
            temp_min2 = round(temp_min1, 0)

            temp_max1 = temp_max - 273
            temp_max2 = round(temp_max1, 0)


            pon1 = "Temperature:"+" "+ str(temp2)+" "+"°C"
            pon2 = "Like feel temperature:"+" "+ str(likefeel2)+" "+"°C"
            pon3 = "Pressure:"+" "+ str(pressure)+" "+"millimeters of mercury"
            pon4 = "Humidity:"+" "+ str(humidity)+" "+"%"
            pon5 = "Min. temperature:"+" "+ str(temp_min2)+" "+"°C"
            pon6 = "Max. temperature:"+" "+ str(temp_max2)+" "+"°C"
            pon7 = "Sea level:"+" "+ str(sealevel)+" "+"m"
            pon8 = "Wind speed:"+" "+ str(windspeed)+" "+"m/s"
            pon9 = "Clouds:"+" "+ str(clouds)+" "+"%"

            twoEdit.setText(str(pon1))
            threeEdit.setText(str(pon2))
            fourEdit.setText(str(pon3))
            fiveEdit.setText(str(pon4))
            sixEdit.setText(str(pon5))
            sevenEdit.setText(str(pon6))
            eightEdit.setText(str(pon7))
            nineEdit.setText(str(pon8))
            tenEdit.setText(str(pon9))        
        else:
            print('помилка')


    weatherButton.clicked.connect(weather)
    dia.setLayout(oneV) 
    dia.show()
    dia.exec_()