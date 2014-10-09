#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import sys
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import os


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):

        self.locales = []
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fichero))
        self.lista = sHandler.get_tags()

    def __str__(self):
        for index in self.lista:
            print index[0],
            contenido = index[1]
            for elemento in contenido:
                if contenido[elemento] != "":
                    print '\t', elemento, '=', contenido[elemento],
            print

    def do_local(self):
        for index in self.lista:
            contenido = index[1]
            for elemento in contenido:
                if contenido[elemento] != "":
                    if elemento == "src":
                        if contenido[elemento]:
                            sources = contenido[elemento]
                            os.system("wget -q " + sources)
                            nombre = sources.split('/')
                            nombre = nombre[-1]
                            contenido[elemento] = nombre

        print

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except IndexError:
        print 'Usage: python karaoke.py src_file.smil'
        sys.exit()
    KaraokeLocal(fichero).__str__()
    KaraokeLocal(fichero).do_local()
    KaraokeLocal(fichero).__str__()
