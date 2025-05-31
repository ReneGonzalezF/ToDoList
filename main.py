from back import creaTablaTareas,agregarTarea, eliminarTarea, mostrarTarea, marcarTareaComoCompletada,mostrarPendientes,mostrarCompletadas,validarId
from datetime import datetime

creaTablaTareas()

while True:
    #menu basico
    print("-----------------------------------------")
    print("BIENVENIDO A TO DO LIST")
    print("INGRESE UNA DE LAS OPCIONES: ")
    print("1.- AGREGAR TAREA")
    print("2.- MOSTRAR TODAS LAS  TAREAS")
    print("3.- MARCAR TAREA COMO COMPLETADA")
    print("4.- ELIMINAR TAREA")
    print("5.- MOSTRAR PENDIENTES")
    print("6.- MOSTRAR COMPLETADAS")
    print("7.- SALIR")
    #Validar que opcion sea numero:
    while True:    
        opcion=input()
       
        if opcion.isdigit():
            opcion=int(opcion)
            break
        else:
            print("INGRESE UNA OPCION VALIDA!")
        
    #opcion 1 se valida que el texto no esté vacio
    
    if opcion==1:
         texto=input("INGRESE TAREA:")
         fecha=datetime.now().strftime('%Y-%m-%d %H:%M')
         while texto=='':
                print("DEBE INGRESAR UNA TAREA")
                texto=input("INGRESE TAREA: ")
                continue
         agregarTarea(texto,fecha)
                   
    #opcion 2 ---------------------------------------
    elif opcion==2:
         for i in mostrarTarea():
              estado="COMPLETADA" if i[2]==1 else "INCOMPLETA"
              print(f"MOSTRANDO TAREAS:--ID TAREA: {i[0]}--TAREA: {i[1]} --ESTADO: {estado} --FECHA: {i[3]}")
         
         
    #opcion 3 ---------------------------------------
    elif opcion==3:
         
         id=input("INGRESE ID DE TAREA: ")
         validoTarea=validarId(id) #le aplico la funcion a la variable validoTarea para que tenga resultado de la variable

         while not id.isdigit() or not validoTarea: #Si el resultado de validoTare por ende de la variable es falso, se ejecuta el bucle.
              id=input("INGRESE UN ID VALIDO! ")
              
         marcarTareaComoCompletada(id)
         print("TAREA MARCADA COMO COMPLETADA")
    #opcion 4 -----------------------------------
    elif opcion == 4:
         
         id=input("INGRESE ID DE TAREA: ")
         validoTarea=validarId(id) #le aplico la funcion a la variable validoTarea para que tenga resultado de la variable

         while not id.isdigit() or not validoTarea: #Si el resultado de validoTare por ende de la variable es falso, se ejecuta el bucle.
              id=input("INGRESE UN ID VALIDO! ")
              
         eliminarTarea(id)
         print("TAREA ELIMINADA")
    #OPCION 5-------------------------
    elif opcion==5:
         for i in mostrarPendientes():
              estado="COMPLETADA" if i[2]==0 else "INCOMPLETA"
              print(f"ID: {i[0]}/ TAREA: {i[1]} / ESTADO: {estado} / FECHA: {i[3]}")
         
    #opcion 6---------------------------------------
    elif opcion==6:
         for i in mostrarCompletadas():
              estado="COMPLETADA" if i[2]==0 else "INCOMPLETA"
              print(f"ID: {i[0]}/ TAREA: {i[1]} / ESTADO: {estado} / FECHA: {i[3]}")
    elif opcion==7:
         print("SALIENDO DEL PROGRAMA...")
         break
