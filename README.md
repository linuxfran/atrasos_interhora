1. Descripción del proyecto

Smart Attendance es una aplicación web diseñada para mejorar el registro y control de los atrasos escolares. Actualmente, los inspectores registran la información manualmente y la guardan en documentos, lo que demora el proceso y dificulta informar a profesores y apoderados a tiempo.

Nuestra aplicación permite registrar los atrasos de los estudiantes, guardar la información en una base de datos y detectar a quienes llegan tarde frecuentemente. El objetivo es reducir el trabajo manual, organizar los registros y facilitar el seguimiento de los atrasos.

## 2. Tecnologías utilizadas

- Python: procesamiento de la información.
- Flask: creación y funcionamiento de la aplicación web.
- HTML: estructura de las páginas.
- CSS: diseño visual.
- SQLite o la base de datos configurada en el proyecto: almacenamiento de los registros.
- Git y GitHub: control de versiones y trabajo en equipo.

## 3. Cómo ejecutar el proyecto

### Requisitos

- Python instalado.
- Visual Studio Code.
- Git Bash o una terminal compatible.

### Instalación

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Abrir una terminal.
3. Crear un entorno virtual si todavía no existe:

   ```bash
   python -m venv venv
   ```

4. Activar el entorno virtual en Git Bash:

   ```bash
   source venv/Scripts/activate
   ```

5. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

6. Ejecutar la aplicación:

   ```bash
   python app.py
   ```

7. Abrir en el navegador la dirección local que muestre la terminal, normalmente `http://127.0.0.1:5000`.

## 4. Rutas del proyecto

Las rutas deben coincidir con las definidas en el código de Flask.

| Ruta | Función |
|---|---|
| `/` | Página principal del sistema. |
| Ruta de registro | Recibe y guarda los datos del atraso. |
| Otras rutas | Consultar `app/routes.py` para ver las rutas implementadas. |

## 5. Estructura del proyecto

- `app.py`: inicia la aplicación.
- `app/`: contiene la configuración, las rutas, los modelos y la lógica del sistema.
- `static/css/style.css`: contiene los estilos visuales.
- `templates/index.html`: página principal.
- `requirements.txt`: dependencias necesarias.
- `README.md`: documentación del proyecto.
- `.gitignore`: archivos que Git no debe incluir en el repositorio.

## 6. Base de datos

La base de datos almacena los registros de atrasos para poder consultarlos posteriormente.

Cada registro puede incluir:

- Nombre del estudiante.
- Curso.
- Fecha del atraso.
- Minutos de atraso.

La conexión y las operaciones con la base de datos deben revisarse en `app/database.py` y `app/models.py`. El motor utilizado debe indicarse según la configuración real del proyecto.

## 7. Funcionalidades

- Registrar los atrasos de los estudiantes.
- Guardar y consultar la información.
- Organizar los registros por estudiante y curso.
- Detectar estudiantes con atrasos repetidos.
- Mostrar alertas cuando se alcanza el límite definido, si está implementado.

El envío automático de mensajes a los apoderados requiere que el servicio de mensajería esté configurado.

## 8. Integrantes

- Integrante 1: [Nombre completo]
- Integrante 2: [Nombre completo]
- Integrante 3: [Nombre completo]
- Integrante 4: [Nombre completo]

## 9. Captura de pantalla de la página principal

La captura debe mostrar la aplicación funcionando en el navegador.

Guardar la imagen en `docs/captura-inicio.png` y comprobar que la carpeta `docs` exista.

![Página principal de Smart Attendance](docs/captura-inicio.png)
