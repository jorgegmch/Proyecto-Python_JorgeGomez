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
    B. Registrarse (solo campers nuevos, los trainers y coordinadores los crea el coordinador)
    C. Salir

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

7. Registro de Campers desde Login

    Opción "Registrarse" en el login
    Pedir datos básicos del nuevo camper
    Crear usuario con rol = "camper"
    Guardar en estructuras de datos y archivo JSON

8. Guardado en JSON

    Guardar el estado actual de:
    Campers
    Trainers
    Coordinadores
    Rutas
    Matrículas
    Módulos

9. Repetición del flujo

Volver siempre al menú de login hasta que el usuario elija Salir.

FIN
"""
import os
import json

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def pause():
    input("\nPresione ENTER para continuar...")

def salir():
    print("\n¡Hasta luego!")
    print("Gracias por usar el programa.\n")

usuarios = {}
rutas = {}
areas = {}
matriculas = []
evaluaciones = []

def login():
    try:
        while True:
            clear_screen()
            print("¡BIENVENIDO A CAMPUSLANDS!")
            print("-" * 50)
            print("\nMenú de login\n")
            print("1. Iniciar sesión")
            print("2. Registrarse como camper")
            print("0. Salir\n")
            option_login = input("Ingrese una opción (0-2): ")

            match option_login:
                case "1":
                    clear_screen()
                    print("CAMPUSLANDS")
                    print("\tIniciar sesión")
                    print("-" * 50)

                    user = input("\n>>> Ingrese su nombre de usuario: ")
                    


    except ValueError:
        print("ERROR: Debe ingresar un número entre 0 y 2.")
        pause()



def menu_coordinador():
    pass

def menu_trainer():
    pass

def menu_camper():
    pass

def main():
    isActive = True
    while isActive:
        pass


if __name__ == "__main__":
    pass