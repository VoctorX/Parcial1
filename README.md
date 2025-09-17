# Agenda de Contactos – Python (Tkinter)
**Aplicación funcional y completa para la gestión eficiente de contactos telefónicos.**

Esta aplicación corresponde a una **Agenda de Contactos** desarrollada en **Python** utilizando la librería **Tkinter** para la interfaz gráfica.

---

## Descripción del Proyecto 📱

Se desarrolló una aplicación completa de gestión de contactos con las siguientes características:

### Funcionalidades Principales ⚡
- **Agregar Contacto**: Permite registrar nuevos contactos con nombre y número telefónico.
- **Editar Contacto**: Busca un contacto por nombre y actualiza su número telefónico.
- **Borrar Contacto**: Elimina contactos existentes de la agenda.
- **Visualización en Tiempo Real**: Los contactos se muestran dinámicamente en el panel derecho.

### Características de la Interfaz 🎨
- **Diseño de Dos Paneles**: Panel izquierdo con opciones y panel derecho para visualizar contactos.
- **Ventanas Emergentes**: Modales específicas para cada operación (agregar, editar, borrar).
- **Barra de Menú Completa**: 
  - **Menú Inicio**: Acceso a todas las funciones principales + opción de salir
  - **Menú Ayuda**: Tutorial de uso y información "Acerca de"
- **Logo Personalizado**: Icono de celular (`celular.ico`) en la barra de título.
- **Validaciones**: Control de entradas vacías y manejo de errores.
- **Mensajes Informativos**: Confirmaciones y advertencias mediante `messagebox`.

### Detalles Técnicos 🔧
- **Gestión de Estado**: Lista global `contactos[]` para almacenar la información.
- **Búsqueda Inteligente**: Sistema de búsqueda por coincidencia de nombre.
- **Interfaz Responsiva**: Frames que se adaptan al tamaño de la ventana.
- **Manejo de Errores**: Control de excepciones para la carga del icono.

**ACLARACIÓN IMPORTANTE** ⚠️
- Si desea ver el logo correctamente, es importante que el archivo `celular.ico` esté en la misma carpeta que el Python.
- Esto no afecta la funcionalidad del código, simplemente es un detalle visual para la correcta visualización del logo.

---

### Instalación 🔧

1. Clona el repositorio:
```bash
git clone https://github.com/VoctorX/Parcial1.git
```

2. Abre la carpeta del repositorio en tu editor de código.
3. Asegúrate de tener el archivo `celular.ico` en la misma carpeta.
4. Ejecuta el archivo principal:
```bash
python parcial.py
```

## Autor ✒️
* **Victor Cordoba** - *Creador y desarrollador principal* - [VoctorX](https://github.com/VoctorX)

## Fecha 📆
*Septiembre 17 del 2025*

## Construido con 🛠️
_Herramientas y lenguajes utilizados en este proyecto:_

* [Python](https://www.python.org/) - Lenguaje de programación ![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
* [Git](https://git-scm.com/) - Control de versiones ![GitHub](https://img.shields.io/badge/GitHub-actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
* [Visual Studio Code](https://code.visualstudio.com/) - Editor de código

