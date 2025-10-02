"""
Algoritmo -> Campuslands

INICIO

1. INICIALIZAR estructuras de datos:
    - Lista de Campers
    - Lista de Trainers
    - Lista de Coordinadores
    - Lista de Rutas de entrenamiento
    - Lista de Áreas de entrenamiento
    - Lista de Módulos
    - Lista de Matrículas
    - Archivo JSON para persistencia

2. MOSTRAR menú de LOGIN:
    A. Iniciar sesion
    B. Registrarse
    C. Salir

3. SI usuario elige "Camper":
    MOSTRAR menú camper:
        - Ver estado de inscripción
        - Ver asignación de ruta
        - Ver notas por módulos
        - Salir

4. SI usuario elige "Trainer":
    VALIDAR credenciales
    MOSTRAR menú trainer:
        - Ver rutas asignadas
        - Registrar notas de módulos por camper
        - Ver campers asignados
        - Salir

5. SI usuario elige "Coordinador":
    VALIDAR credenciales
    MOSTRAR menú coordinador:
        A. Registro de Campers
            - Ingresar datos personales y académicos
            - Cambiar estado (Inscrito, Aprobado, etc.)
            - Evaluar prueba inicial (teórica + práctica)
                - PROMEDIO = (Teórica + Práctica) / 2
                - SI PROMEDIO >= 60:
                    Estado = "Aprobado"
        B. Gestión de rutas:
            - Crear rutas (con módulos, SGDB principal y alternativo)
            - Asignar rutas a campers aprobados
            - Validar capacidad de áreas (máx 33 campers por horario)
        C. Gestión de Trainers:
            - Registrar nuevo trainer
            - Asignar rutas a trainer según horario
        D. Módulo de matrícula:
            - Asignar ruta, trainer, fechas y salón a campers
        E. Gestión de módulos y evaluación:
            - Registrar notas finales por módulo:
                - NOTA FINAL = (30% Teoría + 60% Práctica + 10% Quices/Trabajos)
                - SI NOTA FINAL >= 60:
                    Módulo Aprobado
                - SI NOTA FINAL < 60:
                    Campers en bajo rendimiento
        F. Reportes:
            - Listar campers inscritos
            - Listar campers aprobados
            - Listar trainers activos
            - Listar campers con bajo rendimiento
            - Listar campers y trainers por ruta
            - Reporte por módulo: cuántos aprobaron y perdieron por ruta y trainer
        G. Consultas:
            - Consultar campers en riesgo alto

6. GUARDAR toda la información en archivo JSON:
    - Guardar estado actual de campers, trainers, rutas, matrículas, etc.

7. REPETIR menú principal hasta que usuario seleccione "Salir"

FIN
"""
import json
import os 



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
    clear_screen()
    print("")
    pass

def menu_coordinador():
    pass

def menu_trainer():
    pass

def menu_camper():
    pass


if __name__ == "__main__":
    pass