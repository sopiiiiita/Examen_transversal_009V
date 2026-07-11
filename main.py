from funciones import (
    leer_opcion, cupos_tipo, busqueda_precio, actualizar_precio,
    validar_codigo, validar_nombre, validar_tipo, validar_duracion,
    validar_piscina, validar_clases, validar_horario, validar_precio,
    validar_cupos, agregar_plan, eliminar_plan
)

def main():
    # Inicialización de las estructuras de datos requeridas
    planes = {
        'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
        'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
        'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
        'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
        'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
        'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
    }

    inscripciones = {
        'F001': [14990, 30],
        'F002': [22990, 10],
        'F003': [39990, 0],
        'F004': [35990, 6],
        'F005': [159990, 2],
        'F006': [18990, 15]
    }

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por tipo de plan")
        print("2. Búsqueda de planes por rango de precio")
        print("3. Actualizar precio de plan")
        print("4. Agregar plan")
        print("5. Eliminar plan")
        print("6. Salir")
        print("=====================================")
        
        opcion = leer_opcion()
        
        if opcion == 1:
            tipo = input("Ingrese tipo de plan a consultar: ")
            cupos_tipo(tipo, planes, inscripciones)
            
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, planes, inscripciones)
            
        elif opcion == 3:
            while True:
                codigo = input("Ingrese código del plan: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                except ValueError:
                    print("Debe ingresar un valor entero válido.")
                    continue
                
                if nuevo_precio <= 0:
                    print("El precio debe ser un valor entero positivo.")
                    continue

                if actualizar_precio(codigo, nuevo_precio, inscripciones):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                    
                resp = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                if resp == 'n':
                    break
                    
        elif opcion == 4:
            codigo = input("Ingrese código del plan: ")
            nombre = input("Ingrese nombre del plan: ")
            tipo = input("Ingrese tipo (mensual/trimestral/anual): ")
            duracion = input("Ingrese duración (meses): ")
            piscina = input("¿Incluye acceso a piscina? (s/n): ")
            clases = input("¿Incluye clases grupales? (s/n): ")
            horario = input("Ingrese horario: ")
            precio = input("Ingrese precio: ")
            cupos = input("Ingrese cupos: ")
            
            # Validación independiente de campos en el programa principal
            if not validar_codigo(codigo, planes):
                print("Error en la validación del código.")
            elif not validar_nombre(nombre):
                print("Error en la validación del nombre.")
            elif not validar_tipo(tipo):
                print("Error en la validación del tipo.")
            elif not validar_duracion(duracion):
                print("Error en la validación de la duración.")
            elif not validar_piscina(piscina):
                print("Error en la validación del acceso a piscina.")
            elif not validar_clases(clases):
                print("Error en la validación de las clases.")
            elif not validar_horario(horario):
                print("Error en la validación del horario.")
            elif not validar_precio(precio):
                print("Error en la validación del precio.")
            elif not validar_cupos(cupos):
                print("Error en la validación de los cupos.")
            else:
                # Conversión de tipos tras validación exitosa
                piscina_bool = True if piscina.lower() == 's' else False
                clases_bool = True if clases.lower() == 's' else False
                
                exito = agregar_plan(
                    codigo, nombre, tipo, int(duracion), piscina_bool, 
                    clases_bool, horario, int(precio), int(cupos), 
                    planes, inscripciones
                )
                
                if exito:
                    print("Plan agregado")
                else:
                    print("El código ya existe")
                    
        elif opcion == 5:
            codigo = input("Ingrese el código del plan que desea eliminar: ")
            if eliminar_plan(codigo, planes, inscripciones):
                print("Plan eliminado")
            else:
                print("El código no existe")
                
        elif opcion == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()