from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from database import obtener_todos_mantenimientos

class ListadoMantenimientos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Listado de Mantenimientos")
        self.setGeometry(200, 200, 900, 400)
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
        datos = obtener_todos_mantenimientos()
        columnas = ["ID", "Equipo ID", "Fecha", "Técnico", "Tipo", "Descripción", "Partes Reemplazadas", "Costo"]
        self.tabla.setRowCount(len(datos))
        self.tabla.setColumnCount(len(columnas))
        self.tabla.setHorizontalHeaderLabels(columnas)

        for fila, mantenimiento in enumerate(datos):
            for columna, valor in enumerate(mantenimiento):
                self.tabla.setItem(fila, columna, QTableWidgetItem(str(valor)))
