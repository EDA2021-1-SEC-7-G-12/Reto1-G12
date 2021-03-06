﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
# Hola

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


def printResults(ord_videos, mostrardos):
    size = lt.size(ord_videos)
    if size >= mostrardos:
        print("Los primeros ", mostrardos, " videos ordenados son:")
        i = 1
        while i <= mostrardos:
            video = lt.getElement(ord_videos, i)
            print('Trending date: ' + video['trending_date'] + ' Title: ' +
                  video['title'] + ' Channel title: ' + video['channel_title']
                  + ' Publish time: ' + video['publish_time'] + ' Views: ' +
                  video['views'] + ' Likes: ' + video['likes'] + ' Dislikes: '
                  + video['dislikes'])
            i += 1


def printResultsLikes(ord_videos, mostrardos):
    size = lt.size(ord_videos)
    listaid = []
    if size >= mostrardos:
        print("Los ", mostrardos, " videos con mas likes son:")
        i = 1
        j = 1
        while i <= mostrardos:
            video = lt.getElement(ord_videos, j)
            if not video["video_id"] in listaid:
                listaid.append(video["video_id"])
                print(' Title: ' +
                  video['title'] + ' Channel title: ' + video['channel_title']
                  + ' Publish time: ' + video['publish_time'] + ' Views: ' +
                  video['views'] + ' Likes: ' + video['likes'] + ' Dislikes: '
                  + video['dislikes'] + ' tags: '
                  + video['tags'])
                i += 1
            j += 1

def printResultPais(video, dias):
    print(' Title: ' +
                  video['title'] + ' Channel title: ' + video['channel_title']
                  + ' Country: ' + video['country'] + ' Dias: ' +
                  str(dias))
def printResultCateg(video, dias):
    print(' Title: ' +
                  video['title'] + ' Channel title: ' + video['channel_title']
                  + ' category_id: ' + video['category_id'] + ' Dias: ' +
                  str(dias))

def printMenu():
    print("Bienvenido")
    print("1- Cargar datos de videos")
    print("2- Consultar los videos con más visitas en una categoría y país específicos")
    print("3- Consultar el video que ha sido trending más días en un país específico")
    print("4- Consultar el video que ha sido trending más días en una categoría específica")
    print("5- Consultar los videos con más likes en un país y tag específicos")
    print("0- Salir de la aplicacion")


def loadData(catalog):
    return controller.loadData(catalog)


def initCatalog():
    return controller.initCatalog()


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        datos = loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categorias'])))
        print('Estos son los datos del primer video cargado. ' + str(catalog["videos"]["elements"][0]))
        print("Tiempo [ms]: ", f"{datos[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{datos[0]:.3f}")
    elif int(inputs[0]) == 2:
        categ = input("Escriba una categoría: ")
        pais = input("Escriba un país: ")
        size = input("Indique el numero de videos que quiere consultar: ")
        print("Sorteando videos ....")
        result = controller.sortVideos(catalog, int(size), pais, categ)
        if not (result is None):
            print("Para la muestra de ", size, " elementos, el tiempo (mseg) es: ",
                                            str(result[0][0]))
            printResults(result[0][1], int(size))
        print("Tiempo [ms]: ", f"{result[2]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{result[1]:.3f}")
    elif int(inputs[0]) == 3:
        pais = input("Escriba un país: ")
        print("Cargando información del video ....")
        resultado = controller.topdiastrendingporpais(catalog, pais)
        printResultPais(resultado[0][0], resultado[0][1])
        print("Tiempo [ms]: ", f"{resultado[2]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{resultado[1]:.3f}")
    elif int(inputs[0]) == 4:
        categ = input("Escriba una categoría: ")
        print("Cargando información del video ....")
        resultado = controller.topdiastrendingporcateg(catalog, categ)
        printResultCateg(resultado[0][0], resultado[0][1])
        print("Tiempo [ms]: ", f"{resultado[2]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{resultado[1]:.3f}")
    elif int(inputs[0]) == 5:
        size = input("Indique el numero de videos que quiere consultar: ")
        tag = input("Escriba un tag: ")
        pais = input("Escriba un pais: ")
        print("Cargando información de los videos ....")
        result = controller.sortVideosLikes(catalog, int(size), tag, pais)
        printResultsLikes(result[0][1], int(size))
        print("Tiempo [ms]: ", f"{result[2]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{result[1]:.3f}")
    else:
        sys.exit(0)
sys.exit(0)
