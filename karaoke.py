#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import sys
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import os
if __name__ == "__main__":
    multimedia = []
    try:
        fichero = sys.argv[1]
    except IndexError:
        print 'Usage: python karaoke.py src_file.smil'
        sys.exit()
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open(fichero))
    lista = sHandler.get_tags()
    for linea in lista:
        elemento = linea[0]
        print elemento, (10 - len(elemento)) * " ",
        atributos = str(linea[1])
        atributos = atributos[1:-1]
        atributos = atributos.split(",")
        iteraciones = 0
        for atributo in atributos:
            iteraciones = iteraciones + 1
            campos = atributo.split(": ")
            clave = campos[0]
            if iteraciones == 1:
                clave = clave[1:-1]
            else:
                clave = clave[2:-1]
                valor = campos[1]
                valor = valor[1:-1]
                sentencia = clave + "=" + '"' + valor + '"'
                print ('\t'), sentencia,
            print ('\n'),
    for url in multimedia:
        os.system("wget ­-q " + url)
    locales = []
    for valor in multimedia:
        locales.append(valor.split("/")[-1])
