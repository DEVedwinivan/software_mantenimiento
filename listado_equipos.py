from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from database import obtener_todos_equipos

class ListadoEquipos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listado de Equipos")
        self.setGeometry(200, 200, 800, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.tabla = QTableWidget()
        layout.addWidget(self.tabla)
        self.setLayout(layout)
        self.cargar_datos()
        self.tabla.setAlternatingRowColors(True)
        self.tabla.setStyleSheet("QTableWidget { border: none; }")
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla.verticalHeader().setVisible(False)


    def cargar_datos(self):
        datos = obtener_todos_equipos()
        columnas = ["ID", "N° Serie", "Marca", "Modelo", "Usuario", "Ubicación", "Fecha Compra", "Estado"]
        self.tabla.setRowCount(len(datos))
        self.tabla.setColumnCount(len(columnas))
        self.tabla.setHorizontalHeaderLabels(columnas)

        for fila, equipo in enumerate(datos):
            for columna, valor in enumerate(equipo):
                self.tabla.setItem(fila, columna, QTableWidgetItem(str(valor)))
