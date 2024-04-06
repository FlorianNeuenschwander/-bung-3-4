##uebung 3 und 4
##uebung3
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"



class Figur:
    def __init__(self):
        self.name = "Figur"


    def Umfang(self):
        return 0


    def __str__(self):
        return self.name


class Dreieck(Figur):
    def __init__(self, A, B, C):
        super().__init__()
        self.name = "Dreieck"
        self.A = A
        self.B = B
        self.C = C



    def Umfang(self):
        AB = self.distance(self.A, self.B)
        BC = self.distance(self.B, self.C)
        AC = self.distance(self.A, self.C)
        return AB + BC + AC




    def distance(self, point1, point2):
        return math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)



    def __str__(self):
        return f"Dreieck {self.A}-{self.B}-{self.C}"





class Rechteck(Figur):
    def __init__(self, A, B):
        super().__init__()
        self.name = "Rechteck"
        self.A = A
        self.B = B

    def Umfang(self):
        AB = abs(self.A.x - self.B.x)
        BC = abs(self.A.y - self.B.y)
        return 2 * (AB + BC)

    def __str__(self):
        return f"Rechteck {self.A} - {self.B}"



class Kreis(Figur):
    def __init__(self, M, r):
        super().__init__()
        self.name = "Kreis"
        self.M = M
        self.r = r

    def Umfang(self):
        return 2 * math.pi * self.r

    def __str__(self):
        return f"Kreis M={self.M} r={self.r}"




class Polygon(Figur):
    def __init__(self, *vertices):
        super().__init__()
        self.name = "Polygon"
        self.vertices = vertices




    def Umfang(self):
        perimeter = 0
        for i in range(len(self.vertices)):
            perimeter += self.distance(self.vertices[i], self.vertices[(i+1)%len(self.vertices)])
        return perimeter




    def distance(self, point1, point2):
        return math.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)




    def __str__(self):
        vertices_str = ' - '.join(str(vertex) for vertex in self.vertices)
        return f"Polygon {vertices_str}"
    




    A = Point(0, 0)
    B = Point(10, 0)
    C = Point(0, 10)

    dreieck = Dreieck(A, B, C)
    print(dreieck)
    print("Umfang:", dreieck.Umfang())

##uebung4

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):
        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        # Layout erstellen:
        layout = QFormLayout()




        # Widget-Instanzen erstellen:
        self.nameLineEdit = QLineEdit()
        self.zahlLineEdit = QLineEdit()
        self.adresseLineEdit = QLineEdit()  
        self.plzLineEdit = QLineEdit()          
        self.ortLineEdit = QLineEdit()   
        self.calendar = QCalendarWidget()  

        
        
        self.button = QPushButton("Save")

        # Layout füllen:
        layout.addRow("Vorname:", self.nameLineEdit)
        layout.addRow("Name:", self.zahlLineEdit)
        layout.addRow("Geburtsdatum:", self.calendar)
        layout.addRow("Adresse:", self.adresseLineEdit)  
        layout.addRow("PLZ:", self.plzLineEdit)          
        layout.addRow("Ort:", self.ortLineEdit)        
        
        layout.addRow(self.button)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()





    def createConnects(self):
        self.button.clicked.connect(self.auswertung)

    def auswertung(self):
        name = self.nameLineEdit.text()
        print("Der Name ist", name)
        try:
            zahl = float(self.zahlLineEdit.text())
            print("Die Zahl ist:", zahl)
            print("Zahl * 2 = ", zahl*2)
        except ValueError:
            print("keine gültige Zahl eingegeben!!") 


def save(self):
        vorname = self.nameLineEdit.text()
        name = self.zahlLineEdit.text()
        geburtsdatum = self.calendar.selectedDate().toString("MM/dd/yyyy")
        adresse = self.adresseLineEdit.text()
        plz = self.plzLineEdit.text()
        ort = self.ortLineEdit.text()

        
        data = f"{vorname},{name},{geburtsdatum},{adresse},{plz},{ort}"

        with open("output.txt", "w") as file:
            file.write(data)
        print("Daten erfolgreich gespeichert.")


def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()


##Die Qcombo Box und das File Menu habe ich nicht herausgefunden
