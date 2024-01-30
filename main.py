import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QStackedWidget
from pymongo import MongoClient

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Astronomía")

        self.stack = QStackedWidget()

        self.galaxias = QListWidget()
        self.cargar_datos(self.galaxias, "galaxias")
        self.galaxias.itemClicked.connect(self.mostrar_sistemas_solares)

        self.stack.addWidget(self.galaxias)

        self.setCentralWidget(self.stack)

    def cargar_datos(self, widget, coleccion):
        uri = "mongodb+srv://usuario:contraseña@cluster.mongodb.net/test?retryWrites=true&w=majority"
        client = MongoClient(uri)
        db = client.get_database('nombre_de_tu_base_de_datos')
        datos = db[coleccion].find()
        for dato in datos:
            widget.addItem(dato['name'])

    def mostrar_sistemas_solares(self):
        self.sistemas_solares = QListWidget()
        self.cargar_datos(self.sistemas_solares, "solar_systems")
        self.sistemas_solares.itemClicked.connect(self.mostrar_estrellas_planetas)

        self.stack.addWidget(self.sistemas_solares)
        self.stack.setCurrentWidget(self.sistemas_solares)

    def mostrar_estrellas_planetas(self):
        self.estrellas_planetas = QListWidget()
        self.cargar_datos(self.estrellas_planetas, "stars")
        self.cargar_datos(self.estrellas_planetas, "planets")
        self.estrellas_planetas.itemClicked.connect(self.mostrar_lunas)

        self.stack.addWidget(self.estrellas_planetas)
        self.stack.setCurrentWidget(self.estrellas_planetas)

    def mostrar_lunas(self):
        self.lunas = QListWidget()
        self.cargar_datos(self.lunas, "moons")

        self.stack.addWidget(self.lunas)
        self.stack.setCurrentWidget(self.lunas)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
