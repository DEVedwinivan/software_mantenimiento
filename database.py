import sqlite3

DB_NAME = 'equipos.db'

def conectar():
    return sqlite3.connect(DB_NAME)

def crear_tabla_equipos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_serie TEXT NOT NULL,
            marca TEXT,
            modelo TEXT,
            usuario TEXT,
            ubicacion TEXT,
            fecha_compra TEXT,
            estado TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insertar_equipo(numero_serie, marca, modelo, usuario, ubicacion, fecha_compra, estado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO equipos (numero_serie, marca, modelo, usuario, ubicacion, fecha_compra, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (numero_serie, marca, modelo, usuario, ubicacion, fecha_compra, estado))
    conn.commit()
    conn.close()

def crear_tabla_mantenimientos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mantenimientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipo_id INTEGER,
            fecha TEXT,
            tecnico TEXT,
            tipo TEXT,
            descripcion TEXT,
            partes_reemplazadas TEXT,
            costo REAL,
            FOREIGN KEY(equipo_id) REFERENCES equipos(id)
        )
    ''')
    conn.commit()
    conn.close()

def insertar_mantenimiento(equipo_id, fecha, tecnico, tipo, descripcion, partes_reemplazadas, costo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO mantenimientos (equipo_id, fecha, tecnico, tipo, descripcion, partes_reemplazadas, costo)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (equipo_id, fecha, tecnico, tipo, descripcion, partes_reemplazadas, costo))
    conn.commit()
    conn.close()

def obtener_equipos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, numero_serie FROM equipos")
    equipos = cursor.fetchall()
    conn.close()
    return equipos

def obtener_todos_equipos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipos")
    datos = cursor.fetchall()
    conn.close()
    return datos

def obtener_todos_mantenimientos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mantenimientos")
    datos = cursor.fetchall()
    conn.close()
    return datos


