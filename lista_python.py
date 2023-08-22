import os  # Importa el módulo 'os' para acceder a funcionalidades del sistema operativo
import sys  # Importa el módulo 'sys' para acceder a funcionalidades específicas del intérprete
import platform

dicc = {"sobresalientes": "Estudiantes Sobresalientes",
        "aprobados": "Estudiantes Aprobados",
        "reprobados": "Estudiantes reprobados",
        "nota_sobresaliente": 90,
        "nota_aprobado": 75,
        "promedio": "Promedio de Estudiantes"
        }


def imprime_materias(materias):
    for x in range(len(materias)):
        print(f"{x+1}. {materias[x]}")


def clear_cls():
    # Obtiene el nombre del sistema operativo
    sistema_operativo = platform.system()

    if sistema_operativo == "Windows":
        os.system('cls')
    elif sistema_operativo == "Linux":
        os.system('clear')
    else:
        print("No se pudo determinar el sistema operativo")


def listado(clave_listado, estudiantes, titulo=""):
    clear_cls()
    contador = 0
    nota = dicc["nota_sobresaliente"] if clave_listado == "sobresalientes" else dicc["nota_aprobado"]
    if titulo != "":
        print("\t"+titulo)
    for x in estudiantes:
        if clave_listado == "promedio":
            contador += 1
            print(str(contador)+".", x[0], x[1], x[len(x)-1])
        elif not clave_listado == "reprobados":
            if (x[7] >= nota):
                contador += 1
                print(str(contador)+".", x[0], x[1], x[len(x)-1])
        else:
            if (x[7] < nota):
                contador += 1
                print(str(contador)+".", x[0], x[1], x[len(x)-1])
    input(f"\n\tSe han encontrado {contador} {dicc[clave_listado]}.")
    print(f"\n{dicc[''+clave_listado]}:\n")


try:
    # Intenta abrir el archivo "lista.txt" en modo lectura
    with open("./lista.txt") as my_file:
        f = my_file.read()  # Lee el contenido del archivo y almacénalo en la variable 'f'
except:
    # Si ocurre una excepción (el archivo no existe o no se puede leer)
    print("No existe el archivo.")
    sys.exit(0)  # Imprime un mensaje y finaliza el programa


# Divide el contenido del archivo en líneas y almacénalas en una lista llamada 'lista'
lista = f.split("\n")

# Divide la primera línea (encabezados de las columnas) en elementos individuales usando ',' como separador
columnas = lista.pop(0).split(",")
# Agrega la columna "Promedio" a la lista de encabezados
columnas.append("Promedio")

estudiantes = []  # Crea una lista vacía llamada 'estudiantes' para almacenar la información de los estudiantes

# Itera a través de cada línea en la lista 'lista' (cada línea contiene información de un estudiante)
for x in lista:
    if (len(x) > 0):
        # Divide la línea en elementos usando ',' como separador y agrega la lista resultante a 'estudiantes'
        estudiante_data = x.split(",")
        notas = [int(nota) for nota in estudiante_data[2:]]
        estudiante_data[2:] = notas
        promedio = sum(notas)/len(notas)
        estudiante_data.append(promedio)
        estudiantes.append(estudiante_data)
# Ordena a los estudiantes de acuerdo a su promedio (de mayor a menor: reverse=True)
# estudiantes = sorted(estudiantes, key=lambda x: x[7], reverse=True)
# Ordena a los estudiantes usando la primera columna x[0]
estudiantes.sort()
materias = list(set([x[1] for x in estudiantes]))
materias.sort()

opcion = ""
while (opcion != "0"):
    clear_cls()
    opcion = input(f"""\tListados de estudiantes\n\
        \n1.{dicc['sobresalientes']}\
        \n2.{dicc['aprobados']}\
        \n3.{dicc['reprobados']}\
        \n4.{dicc['promedio']}\
        \n5.Listados por Materia\
        \n6.Promedio Por Materia\
        \n7.Promedio General\
        \n8.Nota máxima\
        \n9.Nota mínima\
        \n0.Salir del Sistema\n\
        \n\tEscoja una opción: """)
    if opcion == "1":
        listado("sobresalientes", estudiantes)
    elif opcion == "2":
        listado("aprobados", estudiantes)
    elif opcion == "3":
        listado("reprobados", estudiantes)
    elif opcion == "4":
        listado("promedio", estudiantes)
    elif opcion == "5":
        opcion_materia = ""
        while (opcion_materia != "0"):
            clear_cls()
            print("\tListados de estudiantes por Materia\n")
            imprime_materias(materias)
            opcion_materia = input(
                "\n0. Volver al Menú Anterior.\n\n\tEscoja una opción: ")
            try:
                clear_cls()
                if int(opcion_materia)-1 < len(materias) and not int(opcion_materia)-1 < 0:
                    opcion_materia_clave_listado = ""
                    estudiantes_materia = list(
                        filter(lambda x: x[1] == materias[int(opcion_materia)-1], estudiantes))
                    while (opcion_materia_clave_listado != "0"):
                        clear_cls()
                        opcion_materia_clave_listado = input(f"""\tListados de estudiantes de {materias[int(opcion_materia)-1]} \n\
                                                            \n1.{dicc['sobresalientes']}\
                                                            \n2.{dicc['aprobados']}\
                                                            \n3.{dicc['reprobados']}\n\
                                                            \n0.Volver al Menú anterior\n\
                                                            \n\tEscoja una opción: """)
                        if (opcion_materia_clave_listado == "1"):
                            listado("sobresalientes", estudiantes_materia,
                                    f" {dicc['sobresalientes']} en {materias[int(opcion_materia)-1]}\n")
                        elif (opcion_materia_clave_listado == "2"):
                            listado("aprobados", estudiantes_materia,
                                    f" {dicc['aprobados']} en {materias[int(opcion_materia)-1]}\n")
                        elif (opcion_materia_clave_listado == "3"):
                            listado("reprobados", estudiantes_materia,
                                    f" {dicc['reprobados']} de {materias[int(opcion_materia)-1]}\n")
            except:
                print("error")
                opcion_materia = ""
                input()
    elif opcion == "6":
        clear_cls()
        print("\tPromedio por Materia\n")
        buff_materias = materias[0:]
        for i in range(len(buff_materias)):
            notas_materia = [int(x[7])
                             for x in estudiantes if x[1] == buff_materias[i]]
            promedio_materia = int(sum(notas_materia) / len(notas_materia))
            buff_materias[i] = [buff_materias[i], promedio_materia]
        for x in range(len(buff_materias)):
            print(str(x+1)+".", buff_materias[x][0], buff_materias[x][1])
        input("\t")
    elif opcion == "7":
        clear_cls()
        promedios = [int(x[7]) for x in estudiantes]
        print(f"Promedio General: {sum(promedios)/len(promedios)} ")
        input("\t")
    elif opcion == "8":
        clear_cls()
        print("\tNota máxima\n")
        max = float("-inf")
        for i in range(len(estudiantes)):
            for j in range(2, len(estudiantes[i])-1):
                if estudiantes[i][j] > max:
                    max = estudiantes[i][j]
        for i in range(len(estudiantes)):
            if max in estudiantes[i][:7]:
                print(
                    f" {estudiantes[i][0]} - Nota {estudiantes[i].index(max)}: {max} - {estudiantes[i][1]}")
        input()
    elif opcion == "9":
        clear_cls()
        print("\tNota mínima\n")
        min = float("inf")
        for i in range(len(estudiantes)):
            for j in range(2, len(estudiantes[i])-1):
                if estudiantes[i][j] < min:
                    min = estudiantes[i][j]
        for i in range(len(estudiantes)):
            if min in estudiantes[i][:7]:
                print(
                    f" {estudiantes[i][0]} - Nota {estudiantes[i].index(min)}: {min} - {estudiantes[i][1]}")
        input()
    else:
        clear_cls()
