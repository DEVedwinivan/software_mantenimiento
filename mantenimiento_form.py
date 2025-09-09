from PyQt5.QtWidgets import (
    QWidget, QLabel, QComboBox, QLineEdit, QTextEdit, QPushButton,
    QFormLayout, QMessageBox
)
from database import insertar_mantenimiento, obtener_equipos

class FormularioMantenimiento(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registrar Mantenimiento")
        self.setGeometry(200, 200, 400, 350)
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        title = QLabel("Registrar Nuevo Equipo")  # O "Registrar Mantenimiento"
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addRow(title)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        self.equipos_cb = QComboBox()
        equipos = obtener_equipos()
        self.equipos_dict = {}
        for id_, serie in equipos:
            self.equipos_cb.addItem(f"{serie} (ID: {id_})", id_)
            self.equipos_dict[serie] = id_

        self.fecha = QLineEdit()
        self.tecnico = QLineEdit()
        self.tipo = QLineEdit()
        self.descripcion = QTextEdit()
        self.partes = QLineEdit()
        self.costo = QLineEdit()

        layout.addRow("Equipo:", self.equipos_cb)
        layout.addRow("Fecha (DD/MM/AAAA):", self.fecha)
        layout.addRow("Técnico:", self.tecnico)
        layout.addRow("Tipo (preventivo, correctivo):", self.tipo)
        layout.addRow("Descripción:", self.descripcion)
        layout.addRow("Partes Reemplazadas:", self.partes)
        layout.addRow("Costo:", self.costo)

        btn_guardar = QPushButton("Guardar")
        btn_guardar.clicked.connect(self.guardar_mantenimiento)
        layout.addRow(btn_guardar)

        self.setLayout(layout)

    def guardar_mantenimiento(self):
        equipo_id = self.equipos_cb.currentData()
        insertar_mantenimiento(
            equipo_id,
            self.fecha.text(),
            self.tecnico.text(),
            self.tipo.text(),
            self.descripcion.toPlainText(),
            self.partes.text(),
            float(self.costo.text())
        )
        QMessageBox.information(self, "Éxito", "Mantenimiento registrado correctamente.")
        self.close()
