import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from equipo_from import FormularioEquipo
from database import crear_tabla_equipos
from mantenimiento_form import FormularioMantenimiento
from database import crear_tabla_mantenimientos
from listado_equipos import ListadoEquipos
from listado_mantenimientos import ListadoMantenimientos

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QVBoxLayout, QLabel, QMessageBox,
)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        crear_tabla_equipos()
        crear_tabla_mantenimientos()
        self.setWindowTitle("Mantenimiento Técnico de Equipos")
        self.setWindowIcon(QIcon("img/icon.png"))
        self.setStyleSheet("Background-color:white;")
        self.setGeometry(100, 100, 600, 200)
        self.init_ui()




    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
    
        layout = QVBoxLayout()
        layout.setSpacing(15)
    
        label = QLabel("📋 Mantenimiento Técnico de Equipos")
        label.setStyleSheet("font-size: 50px; font-weight: bold; margin-bottom: 10px;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

    
        btn_equipos = QPushButton("➕ Registrar Equipos")
        btn_equipos.setStyleSheet("Background-color:#34A178; color:white; font-size:16px;")
        btn_equipos.clicked.connect(self.abrir_registro_equipos)
    
        btn_mantenimientos = QPushButton("🛠️ Registrar Mantenimiento")
        btn_mantenimientos.setStyleSheet("Background-color:#34A178; color:white; font-size:16px;")
        btn_mantenimientos.clicked.connect(self.abrir_registro_mantenimientos)
    
        btn_listado_equipos = QPushButton("📂 Ver Equipos Registrados")
        btn_listado_equipos.setStyleSheet("Background-color:#34A178; color:white; font-size:16px;")
        btn_listado_equipos.clicked.connect(self.abrir_listado_equipos)
    
        btn_listado_mant = QPushButton("📘 Ver Mantenimientos Registrados")
        btn_listado_mant.setStyleSheet("Background-color:#34A178; color:white; font-size:16px;")
        btn_listado_mant.clicked.connect(self.abrir_listado_mantenimientos)
    
        for btn in [btn_equipos, btn_mantenimientos, btn_listado_equipos, btn_listado_mant]:
            layout.addWidget(btn)
    
        central_widget.setLayout(layout)


    def abrir_registro_equipos(self):
        self.formulario = FormularioEquipo()
        self.formulario.show()
    def abrir_registro_mantenimientos(self):
        self.formulario = FormularioMantenimiento()
        self.formulario.show()

    def abrir_listado_equipos(self):
        self.listado = ListadoEquipos()
        self.listado.show()

    def abrir_listado_mantenimientos(self):
        self.listado = ListadoMantenimientos()
        self.listado.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())

