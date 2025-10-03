"""
Algoritmo -> Campuslands

INICIO

1. Inicializar estructuras de datos

    Lista de Usuarios (username, password, rol → ["camper", "trainer", "coordinador"])
    Lista de Rutas de entrenamiento (módulos, SGDB principal y alternativo)
    Lista de Áreas de entrenamiento (capacidad máxima 33 campers por turno)
    Lista de Matrículas (camper, ruta, trainer, fechas, salón)
    Lista de Módulos (nombre, evaluaciones, estado aprobado/reprobado)
    Archivo JSON para persistencia de todos los datos

2. Menú de Login

Opciones principales:

    A. Iniciar sesión
    B. Salir

3. Iniciar sesión

    Pedir usuario y contraseña
    Validar credenciales en lista de usuarios
    Si credenciales válidas:
    Obtener rol del usuario
    Si rol == "camper" → ir a menú camper
    Si rol == "trainer" → ir a menú trainer
    Si rol == "coordinador" → ir a menú coordinador
    Si credenciales inválidas → mostrar error y volver a login

4. Menú Camper

    Ver estado de inscripción
    Ver asignación de ruta
    Ver notas por módulos
    Salir (cerrar sesión y volver a login)

5. Menú Trainer

    Ver rutas asignadas
    Registrar notas de módulos por camper
    Ver campers asignados
    Salir (cerrar sesión y volver a login)

6. Menú Coordinador

    A. Registro de Campers

        Ingresar datos personales y académicos
        Cambiar estado (Inscrito, Aprobado, etc.)
        Evaluar prueba inicial → PROMEDIO = (Teórica + Práctica) / 2
        Si PROMEDIO >= 60 → Estado = "Aprobado"

    B. Gestión de Rutas

        Crear rutas (con módulos, SGDB principal y alternativo)
        Asignar rutas a campers aprobados
        Validar capacidad de áreas (máx. 33 campers por horario)

    C. Registro de Trainers

        Registrar nuevo trainer
            
            Nombre(s):
            Apellidos:


        Asignar rutas a trainer según horario

    D. Módulo de Matrícula

        Asignar ruta, trainer, fechas y salón a campers

    E. Gestión de Módulos y Evaluación

        Calcular nota final:
        NOTA FINAL = 30% Teoría + 60% Práctica + 10% Quices/Trabajos
        Si NOTA FINAL >= 60 → Módulo Aprobado
        Si NOTA FINAL < 60 → Camper con bajo rendimiento

    F. Reportes

        Listar campers inscritos
        Listar campers aprobados
        Listar trainers activos
        Listar campers con bajo rendimiento
        Listar campers y trainers por ruta
        Reporte por módulo: cuántos aprobaron y perdieron por ruta y trainer

    G. Consultas

        Consultar campers en riesgo alto

    H. Salir (cerrar sesión y volver a login)

7. Guardado en JSON

    Guardar el estado actual de:
    Campers
    Trainers
    Coordinadores
    Rutas
    Matrículas
    Módulos

8. Repetición del flujo

Volver siempre al menú de login hasta que el usuario elija Salir.

FIN
"""
import os
import json

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def pause():
    input("\nPresione ENTER para continuar...")

def validador_input(msg):
    while True:
        mensaje = input(msg).strip()
        if mensaje == "":
            print("\n⚠️ ERROR: Este campo no puede estar vacío. Intente de nuevo.\n")
        else:
            return mensaje

def leer_indices(seleccion, maximo=None):
    indices = []
    for x in seleccion.split(","):
        try:
            num = int(x.strip())
            if maximo is None or 1 <= num <= maximo:
                indices.append(num)
        except ValueError:
            continue
    return indices

estados = (
    "En proceso de ingreso",
    "Inscrito", 
    "Aprobado", 
    "Cursando", 
    "Graduado", 
    "Expulsado", 
    "Retirado"
    )

horarios = (
    "06:00 - 10:00",
    "10:00 - 14:00",
    "14:00 - 18:00",
    "18:00 - 22:00"
    )

rutas = (
    ("Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)", []),
    ("Programación Web (HTML, CSS y Bootstrap)", []),
    ("Programación formal", [
        "Java", 
        "JavaScript", 
        "C#"
        ]),
    ("Bases de datos", [
        "MySQL", 
        "MongoDB", 
        "PostgreSQL"
        ]),
    ("Backend", [
        "NetCore", 
        "Spring Boot", 
        "NodeJS", 
        "Express"
        ])
)

riesgos = (
    "Bajo",
    "Medio",
    "Alto"
)

usuarios = {
    "cordcamp2025" : {
    "nombres_admin" : "Jorge Alberto",
    "apellidos_admin" : "Gomez Chaparro",
    "rol_admin" : "coordinador"
    }
}
areas = {}
matriculas = []
evaluaciones = []

def login():
    try:
        clear_screen()
        print("¡BIENVENIDO A CAMPUSLANDS!")
        print("-" * 50)
        print("\nMenú de login\n")
        print("1. Iniciar sesión")
        print("0. Salir\n")
        option_login = input(">>> Ingrese una opción (0-1): ")
        isActiveLogin = True
        while isActiveLogin:
            match option_login:
                case "1":
                    clear_screen()
                    print("CAMPUSLANDS")
                    print("-" * 50)
                    print("Iniciar sesión")
                    user = input("\n>>> Ingrese su nombre de usuario: ")
                    if user not in usuarios:
                        print(f"\nEl usuario {user} aún no ha sido registrado")
                    else:
                        pass
    except ValueError:
        print("⚠️ ERROR: Debe ingresar un número entre 0 y 2.")
        pause()
    
def menu_coordinador():
    print("CAMPUSLANDS ADMIN")
    print("-" * 50)
    print("\n>> Menú ADMIN <<\n")
    print("1. Registrar camper")
    print("2. Registrar trainer")
    print("3. Gestión de rutas")
    print("4. Módulo de matrícula")
    print("5. Gestión de módulos y evaluación")
    print("6. Reportes")
    print("7. Consultas")
    print("0. Salir\n")
    option_coordinador = input(">>> Ingrese una opción (0-7): ")
    return option_coordinador

def registro_campers():
    isActiveRegistroCamper = True
    while isActiveRegistroCamper:
        clear_screen()
        print("CAMPUSLANDS ADMIN")
        print("-" * 50)
        print("\n>> Registro de campers <<\n")
        print("1. Registrar información")
        print("2. Registrar nota de prueba inicial")
        print("3. Cambiar estado")
        print("4. Modificar riesgo")
        print("0. Salir\n")
        option_registro_camper = input(">>> Ingrese una opción (0-4): ")
        
        try:
            match option_registro_camper:
                case "1":
                    clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\nRegistrando información del camper...\n")
                    cod_camper = input("\t> Número de identificación: ")
                    if cod_camper in usuarios:
                        print("\nEste número de identificación ya fue registrado. Intente de nuevo.")
                    else:
                        nombres = validador_input("\t> Nombre(s): ").title()
                        apellidos = validador_input("\t> Apellidos: ").title()
                        direccion = validador_input("\t> Dirección: ").upper()
                        acudiente = validador_input("\t> Nombre del acudiente: ").title()
                        movil = validador_input("\t> Número de teléfono movil: ")
                        telefono = validador_input("\t> Número de teléfono fijo: ")
                        estado_camper = estados[0]
                        riesgo_camper = riesgos[0]
                        nota_prueba_inicio = None
                        ruta = None
                        calificaciones = None
                        rol = "camper"
                        
                        usuarios[cod_camper] = {
                            "nombres" : nombres,
                            "apellidos" : apellidos,
                            "direccion" : direccion,
                            "acudiente" : acudiente,
                            "movil" : movil,
                            "telefono" : telefono,
                            "riesgo_camper" : riesgo_camper,
                            "estado_camper" : estado_camper,
                            "nota_prueba_inicio" : nota_prueba_inicio,
                            "ruta" : ruta,
                            "calificaciones" : calificaciones,
                            "rol" : rol
                        }
                        print("\nInformación registrada con éxito.")
                    pause()
                case "2":
                    clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\nRegistrando nota de prueba inicial...\n")
                    
                    cod_camper = input("\t> Número de identificación: ")
                    if cod_camper not in usuarios:
                        print("\nEste número de identificación no ha sido registrado. Intente de nuevo.")
                    else:
                        print(f"\t> Aspirante: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
                        nota_prueba_inicio = int(input("\t> Nota de prueba inicial (0-100): "))
                        usuarios[cod_camper]['nota_prueba_inicio'] = nota_prueba_inicio

                        if nota_prueba_inicio >= 60:
                            usuarios[cod_camper]['estado_camper'] = estados[1]
                            print(f"\nEl aspirante aprobó la prueba inicial. Su estado ha cambiado a '{estados[1]}'.")
                        else:
                            usuarios[cod_camper]['estado_camper'] = estados[0]
                            print("\nEl aspirante no aprobó la prueba inicial.")
                    pause()
                        
                case "3":
                    clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\nCambiar estado\n")
                    cod_camper = input("\t> Número de identificación: ")
                    if cod_camper not in usuarios:
                        print("\nEste número de identificación no ha sido registrado. Intente de nuevo.")
                    else:
                        print(f"\t> Aspirante: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
                        print("-" * 25)
                        print("\nLISTA DE ESTADOS:\n")
                        for idx, estado in enumerate(estados, 1):
                            print(f"{idx}. {estado}")
                        num_estado = int(input("\n>>> Ingrese el número del item que desea asignar como nuevo estado: "))
                        usuarios[cod_camper]['estado_camper'] = estados[num_estado - 1]
                        print("\nEstado cambiado con éxito.")
                    pause()
                
                case "4":
                    clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\nModificar riesgo\n")
                    cod_camper = input("\t> Número de identificación: ")
                    if cod_camper not in usuarios:
                        print("\nEste número de identificación no ha sido registrado. Intente de nuevo.")
                    else:
                        print(f"\t> Aspirante: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
                        print("-" * 25)
                        print("\nLISTA DE ESTADOS DE RIESGO:\n")
                        for idx, riesgo in enumerate(riesgos, 1):
                            print(f"{idx}. {riesgo}")
                        num_riesgo = int(input("\n>>> Ingrese el número del item que desea asignar como nuevo estado de riesgo: "))
                        usuarios[cod_camper]['riesgo_camper'] = riesgos[num_riesgo - 1]
                        print("\nEstado de riesgo modificado con éxito.")
                    pause()
                    
                case "0":
                    salir("\nVolviendo al menú principal...")
                    pause()
                    isActiveRegistroCamper = False
                case _:
                    exception("\n⚠️ ERROR: Debe ingresar un número entre 0 y 4. Intente de nuevo.")
        except ValueError:
            exception("\n⚠️ ERROR: Debe ingresar una opción de la lista. Intente de nuevo.")

def registro_trainers():
    isActiveRegistroTrainer = True
    while isActiveRegistroTrainer:
        clear_screen()
        print("CAMPUSLANDS ADMIN")
        print("-" * 50)
        print("\n>> Registro de trainers <<\n")
        print("1. Registrar información")
        print("2. Asignar horario")
        print("3. Asignar ruta")
        print("0. Salir\n")
        option_registro_trainer = input("Ingrese una opción (0-3): ")

        try:
            match option_registro_trainer:
                case "1":
                    clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\nRegistrando información del trainer...\n")
                    user_trainer = input("\t> Nombre de usuario: ")
                    if user_trainer in usuarios:
                        print("\nEste usuario ya ha sido registrado. Intente de nuevo.")
                    else:
                        nombre_trainer = validador_input("\t> Nombre(s): ").title()
                        apellido_trainer = validador_input("\t> Apellidos: ").title()
                        direccion_trainer = validador_input("\t> Dirección: ").upper()
                        movil_trainer = validador_input("\t> Número de teléfono movil: ")
                        telefono_trainer = validador_input("\t> Número de teléfono fijo: ")
                        horario_trainer = None
                        ruta_trainer = []
                        rol_trainer = "trainer"

                        usuarios[user_trainer] = {
                            "nombre_trainer" : nombre_trainer,
                            "apellido_trainer" : apellido_trainer,
                            "direccion_trainer" : direccion_trainer,
                            "movil_trainer" : movil_trainer,
                            "telefono_trainer" : telefono_trainer,
                            "horario_trainer" : horario_trainer,
                            "ruta_trainer" : ruta_trainer,
                            "rol_trainer" : rol_trainer
                            }
                        print("\nInformación registrada con éxito.")
                    pause()

                case "2": 
                    clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\n>> Asignar horario <<\n")
                    user_trainer = input("\t> Nombre de usuario: ")
                    if user_trainer not in usuarios:
                        print("\nEste trainer aún no ha sido registrado. Intente nuevamente.")
                    else:
                        print(f"\t> Trainer: {usuarios[user_trainer]['nombre_trainer']} {usuarios[user_trainer]['apellido_trainer']}\n")
                        print("-" * 25)
                        print("\nLISTA DE HORARIOS DISPONIBLES:\n")
                        for idx, horarios_trainer in enumerate(horarios, 1):
                            print(f"{idx}. {horarios_trainer}")
                        num_horario = int(input("\n>>> Ingrese el número del item que desea asignar como horario: "))
                        usuarios[user_trainer]['horario_trainer'] = horarios[num_horario - 1]
                        print("\nHorario asignado con éxito.")
                    pause()


                case "3":
                    clear_screen()
                    print("CAMPUSLANDS ADMIN")
                    print("-" * 50)
                    print("\n>> Asignar ruta <<\n")
                    user_trainer = input("\t> Nombre de usuario: ")
                    if user_trainer not in usuarios:
                        print("\nEste trainer aún no ha sido registrado. Intente nuevamente.")
                    else:
                        print(f"\t> Trainer: {usuarios[user_trainer]['nombre_trainer']} {usuarios[user_trainer]['apellido_trainer']}\n")

                    if not usuarios[user_trainer]['horario_trainer']:
                        print("\nEste trainer aún no tiene un horario asignado. Asigne un horario primero (opción 2).")
                        pause()
                        break
                    
                    horario_trainer = usuarios[user_trainer]['horario_trainer']
                    nombre_trainer = f"{usuarios[user_trainer]['nombre_trainer']} {usuarios[user_trainer]['apellido_trainer']}"

                    if rutas[0][0] not in usuarios[user_trainer]['ruta_trainer']: 
                        usuarios[user_trainer]['ruta_trainer'].append(rutas[0][0])
                    if rutas[1][0] not in usuarios[user_trainer]['ruta_trainer']:
                        usuarios[user_trainer]['ruta_trainer'].append(rutas[1][0])
                    print(f"\n'{rutas[0][0]}' y '{rutas[1][0]}', asignadas por defecto como rutas básicas.")
                    print("-" * 25)

                    print("\nASIGNACIÓN DE RUTA ESPECIALIZADA:")
                    tema_1, subtemas_1 = rutas[2]
                    print(f"\nSeleccione 2 especializaciones para la ruta de {tema_1}\n")
                    for idx, sub_1 in enumerate(subtemas_1, 1):
                        print(f"{idx}. {sub_1}")
                    num_espec_1 = leer_indices(input("\n>>> Ingrese dos números de items separados por comas: "))
                    if 1 <= len(num_espec_1) <= 2:
                        for i in num_espec_1:
                            if 1 <= i <= len(subtemas_1):
                                usuarios[user_trainer]['ruta_trainer'].append(f"{tema_1} - {subtemas_1[i - 1]}")

                    tema_2, subtemas_2 = rutas[3]
                    print(f"\nSeleccione 1 especialización para la ruta de {tema_2}\n")
                    for idx, sub_2 in enumerate(subtemas_2, 1):
                        print(f"{idx}. {sub_2}")
                    num_espec_2 = int(input("\n>>> Ingrese el número del SGBD a asignar: "))
                    if 1 <= num_espec_2 <= len(subtemas_2):
                        usuarios[user_trainer]['ruta_trainer'].append(f"{tema_2} - {subtemas_2[num_espec_2 - 1]}")

                    tema_3, subtemas_3 = rutas[4]
                    print(f"\nSeleccione 2 especializaciones para la ruta de {tema_3}\n")
                    for idx, sub_3 in enumerate(subtemas_3, 1):
                        print(f"{idx}. {sub_3}")
                    num_espec_3 = leer_indices(input("\n>>> Ingrese dos números de items separados por comas: "))
                    if 1 <= len(num_espec_3) <= 2:
                        for i in num_espec_3:
                            if 1 <= i <= len(subtemas_3):
                                usuarios[user_trainer]['ruta_trainer'].append(f"{tema_3} - {subtemas_3[i - 1]}")
                    print("\nRuta asignada con éxito.")
                    pause()

                    for ruta in usuarios[user_trainer]['ruta_trainer']:
                        nombre_area = f"Ruta: {ruta} | Horario: {horario_trainer} | Trainer: {nombre_trainer}"
                        if nombre_area not in areas:
                            areas[nombre_area] = {
                                "ruta": ruta,
                                "horario": horario_trainer,
                                "trainer": nombre_trainer,
                                "campers": []
                            }
                            print(f"✅ Área creada: {nombre_area}")
                        else:
                            print(f"❌ El área {nombre_area} ya existe.")

                case "0":
                    salir("\nVolviendo al menú principal...")
                    pause()
                    isActiveRegistroTrainer = False
                case _:
                    exception("\n⚠️ ERROR: Debe ingresar un número entre 0 y 2")
        except ValueError:
            exception("\n⚠️ ERROR: Tipo de dato no válido.")

def gestion_rutas():
    # Crear rutas (con módulos, SGDB principal y alternativo)
    # Asignar rutas a campers aprobados
    # Validar capacidad de áreas (máx. 33 campers por horario)
    try:
        clear_screen()
        print("CAMPUSLANDS ADMIN")
        print("-" * 50)
        print("\n>>> Asignar ruta a campers <<<\n")

        cod_camper = input("\t> Número de identificación del camper: ")
        if cod_camper not in usuarios:
            print("\nEste número de identificación no ha sido registrado. Intente de nuevo.")

        else:
            print(f"\t> Camper: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
            print("-" * 25)
            print("\nAREAS Y RUTAS DISPONIBLES:")

            keys_areas = list(areas.keys())
            disponibles = []
            for idx, area in enumerate(keys_areas, 1):
                cupo = len(areas[area]['campers'])
                if cupo < 33:
                    print(f"{idx}. {area} | {cupo}/33")
                    disponibles.append(area)
                else:
                    print(f"{idx}. {area} | ❌ Ruta llena.")

            if not disponibles:
                print("\n No hay rutas con cupos disponibles.")
                pause()
                return

            num_area = int(input("\n>>> Ingrese el número de la ruta que desea asignar: "))
            if num_area < 1 or num_area > len(keys_areas):
                print("\nERROR: Opción inválida.")

            area_selec = keys_areas[num_area - 1]
            if len(areas[area_selec]['campers']) >= 33:
                print("\nEsta ruta no tiene cupos disponibles.")

            areas[area_selec]['campers'].append(cod_camper)
            usuarios[cod_camper]['ruta'] = area_selec
            usuarios[cod_camper]['estado_camper'] = estados[3]
            print(f"\n✅ El camper {usuarios[cod_camper]['nombres']} fue añadido a {area_selec}")
        pause()
    except ValueError:
            exception("\n⚠️ ERROR: Debe ingresar una opción de la lista. Intente de nuevo.")

def modulo_matricula():
    pass
def gestion_modulos_evaluacion():
    pass
def reportes():
    pass
def consultas():
    pass

def salir(msg):
    print(msg)

def exception(msg):
    print(msg)
    pause()


def main_coordinador():
    isActiveCoordinador = True
    while isActiveCoordinador:
        clear_screen()
        option_coordinador = menu_coordinador()
        
        match option_coordinador:
            case "1":
                registro_campers()
            case "2":
                registro_trainers()
            case "3":
                gestion_rutas()
            case "4":
                modulo_matricula()
            case "5":
                gestion_modulos_evaluacion()
            case "6":
                reportes()
            case "7":
                consultas()
            case "0":
                salir("\nCerrando sesión...\n")
                isActiveCoordinador = False
            case _:
                exception("\n⚠️ ERROR: Debe ingresar un número entre 0 y 7.")

def menu_trainer():
    pass

def menu_camper():
    pass

# if __name__ == "__main__":
    # pass

main_coordinador()