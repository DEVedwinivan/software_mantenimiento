from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox
)
from database import insertar_equipo

class FormularioEquipo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registrar Equipo")
        self.setGeometry(150, 150, 400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        title = QLabel("Registrar Nuevo Equipo")  # O "Registrar Mantenimiento"
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addRow(title)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        self.numero_serie = QLineEdit()
        self.marca = QLineEdit()
        self.modelo = QLineEdit()
        self.usuario = QLineEdit()
        self.ubicacion = QLineEdit()
        self.fecha_compra = QLineEdit()
        self.estado = QLineEdit()

        layout.addRow("Número de Serie:", self.numero_serie)
        layout.addRow("Marca:", self.marca)
        layout.addRow("Modelo:", self.modelo)
        layout.addRow("Usuario Asignado:", self.usuario)
        layout.addRow("Ubicación:", self.ubicacion)
        layout.addRow("Fecha de Compra (DD/MM/AAAA):", self.fecha_compra)
        layout.addRow("Estado del Equipo:", self.estado)

        btn_guardar = QPushButton("Guardar")
        btn_guardar.clicked.connect(self.guardar_equipo)
        layout.addRow(btn_guardar)

        self.setLayout(layout)

    def guardar_equipo(self):
        insertar_equipo(
            self.numero_serie.text(),
            self.marca.text(),
            self.modelo.text(),
            self.usuario.text(),
            self.ubicacion.text(),
            self.fecha_compra.text(),
            self.estado.text()
        )
        QMessageBox.information(self, "Éxito", "Equipo registrado correctamente.")
        self.close()
