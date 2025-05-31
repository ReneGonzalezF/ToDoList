import sqlite3
from datetime import datetime

#Crear Tabla Tarea
def creaTablaTareas():
    conexion = sqlite3.connect('tareas.db')
    cursor = conexion.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS tareas  ( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT, 
                    completado INTEGER NOT NULL CHECK (completado IN (0,1)),
                    ingreso TEXT)''')
                    
    conexion.commit()
    conexion.close()


#Agregar nueva tarea
def agregarTarea(texto,fecha):
    conexion=sqlite3.connect('tareas.db')
    cursor=conexion.cursor()
    cursor.execute(''' INSERT INTO tareas (titulo,completado,ingreso) VALUES (?,?,?)''',(texto,0,fecha))
    conexion.commit()
    conexion.close()

#Mostrar Tareas
def mostrarTarea():
    conexion = sqlite3.connect('tareas.db')
    cursor = conexion.cursor()
    cursor.execute(''' SELECT id ,titulo , completado  ,ingreso  FROM tareas ORDER BY id DESC''')
    todas=cursor.fetchall()
    conexion.close()
    return todas
#funcion para validar si existe el id ingresado:
def validarId(id):
    conexion = sqlite3.connect('tareas.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM tareas WHERE id = ?",(id,))
    resultado=cursor.fetchone()
    conexion.close()
    return resultado is not None

#updatea el valor de 0 a 1
def marcarTareaComoCompletada(id):
    conexion = sqlite3.connect('tareas.db')
    cursor = conexion.cursor()
    cursor.execute("UPDATE tareas SET completado = 1 WHERE id = ?", (id,))
    conexion.commit()
    conexion.close()
#Elimina todos los datos de la tarea donde coincida el id
def eliminarTarea(id):
    conexion=sqlite3.connect('tareas.db')
    cursor=conexion.cursor()
    cursor.execute("DELETE  FROM tareas WHERE id=?", (id,))
    conexion.commit()
    conexion.close()
#muestra en base al id todas las pendientes
def mostrarPendientes():
    conexion=sqlite3.connect('tareas.db')
    cursor=conexion.cursor()
    cursor.execute('''SELECT id,titulo, completado, ingreso FROM tareas WHERE completado=0''')
    pendientes=cursor.fetchall()
    conexion.close()
    return pendientes
#muestra en base al id todas las completadas
def mostrarCompletadas():
    conexion=sqlite3.connect('tareas.db')
    cursor=conexion.cursor()
    cursor.execute('''SELECT id ,titulo, completado, ingreso FROM tareas WHERE completado=1''')
    completadas=cursor.fetchall()
    conexion.close()
    return completadas

    
    