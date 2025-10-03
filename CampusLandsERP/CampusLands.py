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

    C. Gestión de Trainers

        Registrar nuevo trainer
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

estados = (
    "En proceso de ingreso",
    "Inscrito", 
    "Aprobado", 
    "Cursando", 
    "Graduado", 
    "Expulsado", 
    "Retirado"
    )

riesgos = (
    "Bajo",
    "Medio",
    "Alto"
)

usuarios = {
    "cordcamp2025" : {
    "rol" : "coordinador"
    }
}
rutas = {}
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
        print("ERROR: Debe ingresar un número entre 0 y 2.")
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

def registro_camper():
    clear_screen()
    print("CAMPUSLANDS ADMIN")
    print("-" * 50)
    print("\n>> Registro de campers <<\n")
    print("1. Registrar información")
    print("2. Registrar nota de prueba inicial")
    print("3. Cambiar estado")
    print("4. Modificar riesgo")
    print("0. Salir\n")
    option_registro = input(">>> Ingrese una opción (0-4): ")
    
    isActiveRegistro = True
    while isActiveRegistro:
        match option_registro:
            case "1":
                clear_screen()
                print("CAMPUSLANDS ADMIN")
                print("-" * 50)
                print("\nRegistrando información...\n")
                cod_camper = input("\t> Número de identificación: ")
                if cod_camper in usuarios:
                    print("Este número de identificación ya fue registrado.")
                else:
                    nombres = input("\t> Nombre(s): ")
                    apellidos = input("\t> Apellido(s): ")
                    direccion = input("\t> Dirección: ")
                    acudiente = input("\t> Nombre del acudiente: ")
                    movil = input("\t> Número de teléfono movil: ")
                    telefono = input("\t> Número de teléfono fijo: ")
                    estado_camper = (estados[0])
                    riesgo_camper = (riesgos[0])
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
                    print("\nInformación registrada con éxito")
                pause()
                
            case "2":
                clear_screen()
                print("CAMPUSLANDS ADMIN")
                print("-" * 50)
                print("\nRegistrando nota de prueba inicial...\n")
                cod_camper = input("\t> Número de identificación: ")
                if cod_camper not in usuarios:
                    print("\nEste número de identificación no ha sido registrado.")
                else:
                    print(f"\t> Aspirante: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
                    nota_prueba_inicio = int(input("\n\t> Nota de prueba inicial (0-100): "))
                    usuarios[cod_camper]["nota_prueba_inicio"] = nota_prueba_inicio
                    if nota_prueba_inicio >= 60:
                        usuarios[cod_camper]["estado_camper"] = estados[2]
                        print(f"\nEl aspirante aprobó la prueba inicial. Su estado ha cambiado a '{estados[2]}'.")
                    else:
                        usuarios[cod_camper]["estado_camper"] = estados[0]
                        print("\nEl aspirante no aprobó la prueba inicial.")
                    pause()
                    
            case "3":
                clear_screen()
                print("CAMPUSLANDS ADMIN")
                print("-" * 50)
                print("\nCambiar estado\n")
                cod_camper = input("\t> Número de identificación: ")
                if cod_camper not in usuarios:
                    print("\nEste número de identificación no ha sido registrado.")
                else:
                    print(f"\t> Aspirante: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
                    print("\nLista de estados:")
                    for idx, estado in enumerate(estados, 1):
                        print(f"{idx}. {estado}")
                    num_estado = int(input("\n>>> Ingrese el número del nuevo estado: "))
                    usuarios[cod_camper]["estado_camper"] = estados[num_estado - 1]
                    print("\nEstado cambiado con éxito")
                pause()
            
            case "4":
                clear_screen()
                print("CAMPUSLANDS ADMIN")
                print("-" * 50)
                print("\nModificar riesgo\n")
                cod_camper = input("\t> Número de identificación: ")
                if cod_camper not in usuarios:
                    print("\nEste número de identificación no ha sido registrado.")
                else:
                    print(f"\t> Aspirante: {usuarios[cod_camper]['nombres']} {usuarios[cod_camper]['apellidos']}\n")
                    print("\nLista de riesgos:")
                    for idx, riesgo in enumerate(riesgo, 1):
                        print(f"{idx}. {riesgo}")
                    num_riesgo = int(input("\n>>> Ingrese el número del nuevo riesgo: "))
                    usuarios[cod_camper]["riesgo_camper"] = riesgo[num_riesgo - 1]
                    print("\nRiesgo modificado con éxito")
                pause()
                
            case "0":
                print("Volviendo al menú principal...")
                pause()
                isActiveRegistro = False
    
def gestion_rutas():
    pass
def gestion_trainers():
    pass
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
    pause()
    isActiveCoordinador = False
    return isActiveCoordinador

def exception(msg):
    print(msg)
    pause()


def main_coordinador():
    clear_screen()
    option_coordinador = menu_coordinador()
    
    isActiveCoordinador = True
    while isActiveCoordinador:
        match option_coordinador:
            case "1":
                registro_camper()
            case "2":
                gestion_rutas()
            case "3":
                gestion_trainers()
            case "4":
                modulo_matricula()
            case "5":
                gestion_modulos_evaluacion()
            case "6":
                reportes()
            case "7":
                consultas()
            case "0":
                salir("Cerrando sesión...")
            case _:
                exception("ERROR: Debe ingresar un número entre 0 y 7.")

def menu_trainer():
    pass

def menu_camper():
    pass

# if __name__ == "__main__":
    # pass

main_coordinador()