#!/usr/bin/env python3
"""
Módulo Instituto: Clase principal (modelo).

Proyecto de ejemplo - Paradigmas de la Programación
"""


class Instituto:
    """Estructuras de Institutos"""

    def __init__(self, nombre, codigo):
        """Constructor: Inicializa propiedades de instancia."""
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        """Cadena de representación."""
        return "{}: {}".format(self.nombre, self.codigo)


def main():
    """Función principal (ejemplo de uso)."""
    instituto = {}

    instituto["carlos"] = Instituto("carlos", "222-333")
    instituto["sergio"] = Instituto("sergio", "444-555")
    instituto["estela"] = Instituto("estela", "666-777")

    for clave in instituto:
        print(instituto[clave])


if __name__ == "__main__":
    main()
