#!/usr/bin/env python3
"""
Módulo Main: Programa principal (controlador).

Proyecto de Instituto - Nombre de Alumno
Ejecute "ayuda" para más información
"""
from Modelo.instituto import Instituto
from estante import Estante
from Vista.repl import REPL
from Vista.repl import strip


class Main:
    """Clase principal."""

    def __init__(self):
        """Constructor: Inicializa propiedades de instancia y ciclo REPL."""
        self.comandos = {
            "agregar": self.agregar,
            "borrar": self.borrar,
            "mostrar": self.mostrar,
            "listar": self.listar,
            "buscar": self.buscar,
            "ayuda": self.ayuda,
            "salir": self.salir
        }
        archivo = "institutos.db"
        introduccion = strip(__doc__)
        self.varinstitutos = Estante(archivo)
        if not self.varinstitutos.esarchivo():
            introduccion += '\nError: No se pudo abrir "{}"'.format(archivo)
        REPL(self.comandos, introduccion).ciclo()

    def agregar(self, nombre, codigo):
        """
        Agrega un instituto  con su codigo.

        Ingrese: agregar "nombre de Instituto"  "Nro de Instituto"
        """
        self.varinstitutos[nombre] = Instituto(nombre, codigo)

    def borrar(self, nombre):
        """
        Borra un Instituto.

        Ingrese: borrar "nombre de instituto"
        """
        del self.varinstitutos[nombre]

    def mostrar(self, nombre):
        """
        Retorna una Instituto

          Ingrese: mostrar "nombre de su Instituto"
        """
        return self.varinstitutos[nombre]

    def listar(self):
        """
        Retorna todos sus Instituto

        Este comando no requiere de parámetros.
        """
        return (self.varinstitutos[nombre]
                for nombre in sorted(self.varinstitutos))

    def buscar(self, cadena):
        """
        Retorna un Instituto.

          Ingrese: buscar "nombre de su Instituto"
        """
        return (self.varinstitutos[nombre]
                for nombre in sorted(self.varinstitutos)
                if cadena in nombre)

    def ayuda(self, comando=None):
        """
        Retorna la lista de comandos disponibles.

        comando -- Comando del que se desea obtener ayuda (opcional).
        """
        if comando in self.comandos:
            salida = strip(self.comandos[comando].__doc__)
        else:
            salida = "Sintaxis: comando [parámetro1] [parámetro2] [..]\n" + \
                     "Comandos: " + \
                     ", ".join(sorted(self.comandos.keys()))
        return salida

    def salir(self):
        """
        Salir de la aplicación.

        Este comando no requiere de parámetros.
        """
        quit()


if __name__ == "__main__":
    Main()
