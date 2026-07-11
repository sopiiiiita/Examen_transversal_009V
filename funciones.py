def leer_opcion():
    while True:
        try:
            opcion_str = input("Ingrese opción: ")
            opcion = int(opcion_str)
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def cupos_tipo(tipo, planes, inscripciones):
    total_cupos = 0
    tipo_buscado = tipo.lower()
    
    for codigo, datos in planes.items():
        if datos[1].lower() == tipo_buscado:
            if codigo in inscripciones:
                total_cupos += inscripciones[codigo][1]
                
    print(f"El total de cupos disponibles es: {total_cupos}")


def busqueda_precio(p_min, p_max, planes, inscripciones):
    if p_min < 0 or p_max < 0 or p_min > p_max:
        print("No hay planes en ese rango de precios.")
        return

    resultados = []
    for codigo, datos_insc in inscripciones.items():
        precio = datos_insc[0]
        cupos = datos_insc[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            if codigo in planes:
                nombre_plan = planes[codigo][0]
                resultados.append(f"{nombre_plan}--{codigo}")
                
    if resultados:
        resultados.sort()  # Ordena alfabéticamente por el nombre del plan
        print(f"Los planes encontrados son: {resultados}")
    else:
        print("No hay planes en ese rango de precios.")


def buscar_codigo(codigo, inscripciones):
    for k in inscripciones.keys():
        if k.upper() == codigo.upper():
            return True
    return False


def actualizar_precio(codigo, nuevo_precio, inscripciones):
    if not buscar_codigo(codigo, inscripciones):
        return False

    for k in inscripciones.keys():
        if k.upper() == codigo.upper():
            inscripciones[k][0] = nuevo_precio
            return True
    return False



def validar_codigo(codigo, planes):
    if not codigo or codigo.isspace():
        return False
    for k in planes.keys():
        if k.upper() == codigo.upper():
            return False
    return True

def validar_nombre(nombre):
    return bool(nombre and not nombre.isspace())

def validar_tipo(tipo):
    return tipo.lower() in ['mensual', 'trimestral', 'anual']

def validar_duracion(duracion):
    try:
        val = int(duracion)
        return val > 0
    except ValueError:
        return False

def validar_piscina(piscina):
    return piscina.lower() in ['s', 'n']

def validar_clases(clases):
    return clases.lower() in ['s', 'n']

def validar_horario(horario):
    return bool(horario and not horario.isspace())

def validar_precio(precio):
    try:
        val = int(precio)
        return val > 0
    except ValueError:
        return False

def validar_cupos(cupos):
    try:
        val = int(cupos)
        return val >= 0
    except ValueError:
        return False


def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, planes, inscripciones):
    for k in planes.keys():
        if k.upper() == codigo.upper():
            return False

    planes[codigo] = [nombre, tipo.lower(), duracion, acceso_piscina, incluye_clases, horario]
    inscripciones[codigo] = [precio, cupos]
    return True


def eliminar_plan(codigo, planes, inscripciones):
    if not buscar_codigo(codigo, inscripciones):
        return False

    clave_real = None
    for k in inscripciones.keys():
        if k.upper() == codigo.upper():
            clave_real = k
            break

    if clave_real:
        if clave_real in planes:
            del planes[clave_real]
        if clave_real in inscripciones:
            del inscripciones[clave_real]
        return True
    return False