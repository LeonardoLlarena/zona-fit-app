# 🏋️ Zona Fit App: Un Sistema Sencillo para tu Gimnasio

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-lightgray?style=flat-square&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=flat-square&logo=mysql&logoColor=white)
![Licencia MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📄 ¿De qué se trata este proyecto?

Este es un programa de computadora sencillo, hecho en **Python**, para ayudarte a manejar la lista de clientes de un gimnasio. Usa una ventana interactiva (GUI) para que sea fácil de usar. Su función principal es ayudarte a **administrar tus clientes**: puedes agregarlos, verlos en una lista, cambiar su información o eliminarlos.

---

## ✨ Lo que puedes hacer con esta aplicación

* **Administrar Clientes (Crear, Leer, Actualizar, Eliminar):**
    * **Registrar nuevos clientes:** Agrega a los nuevos socios con su nombre, apellido y el número de membresía.
    * **Ver la lista de clientes:** Todos los clientes que agregues aparecerán en una tabla, fácil de revisar.
    * **Actualizar información:** Si un cliente cambia de datos, puedes seleccionarlo en la tabla y actualizar su información.
    * **Eliminar clientes:** Si un cliente se va, puedes borrarlo del sistema. La aplicación te pedirá confirmación para evitar que borres a alguien sin querer.
* **Validaciones inteligentes:** El programa verifica que la información que ingresas sea correcta, por ejemplo, que la membresía sea un número.
* **Diseño fácil de usar:**
    * Los botones como "Eliminar" o "Limpiar" se activan y desactivan solos. Esto te ayuda a saber qué acciones puedes realizar en cada momento.
    * La lista de clientes se actualiza de forma eficiente, para que la aplicación siempre funcione rápido y sin interrupciones.
    * Los mensajes en pantalla son claros y te informan si algo salió bien o si hay algún problema.
* **Guarda tus datos:** La aplicación usa una base de datos **MySQL** para guardar toda la información de tus clientes de forma segura y permanente.

---

## 🛠️ ¿Qué tecnologías usé para crearla?

* **Python 3.12 o más nuevo:** Es el lenguaje principal del programa.
* **Tkinter:** Una herramienta de Python para crear las ventanas y botones del programa.
* **`mysql-connector-python`:** Una librería que permite a Python "hablar" con la base de datos MySQL.
* **MySQL Server:** Es el sistema donde se guardan los datos.
* **Git y GitHub:** Usé estas herramientas para controlar los cambios en el código y guardar el proyecto en línea.

---

## 🚀 ¿Cómo puedo hacer que funcione en mi computadora?

Sigue estos pasos para poner en marcha la aplicación en tu propio equipo:

### 1. **Lo que necesitas tener instalado antes (Requisitos Previos)**

Asegúrate de que ya tienes instaladas estas cosas en tu computadora:

* **Python 3.12 o una versión más reciente:** Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
* **MySQL Server:** Es la base de datos. Puedes descargarla e instalarla desde [dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/).
* **Git:** Es la herramienta para manejar el código. Si no lo tienes, descárgalo desde [git-scm.com/downloads](https://git-scm.com/downloads).

* 

### 2. **Descargar el programa (Clonar el Repositorio)**

Abre la `Terminal` o el `Símbolo del Sistema` (CMD en Windows) en tu computadora. Luego, escribe este comando y presiona `Enter`:

git clone https://github.com/LeonardoLlarena/zona-fit-app.git



### 3. **Preparar la Base de Datos MySQL**

Este paso es muy importante para que el programa pueda guardar y leer los datos de tus clientes:
-Abre tu programa para manejar bases de datos MySQL (puede ser MySQL Workbench o simplemente la línea de comandos de MySQL).
-Crea una nueva base de datos y llámala zona_fit_db. Puedes usar este comando si estás en la terminal:

CREATE DATABASE zona_fit_db;
USE zona_fit_db;

-Dentro de la base de datos zona_fit_db, crea una tabla llamada clientes con esta estructura. Puedes copiar y pegar este código SQL:

CREATE TABLE `clientes` (
  `id_cliente` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `membresia` INT NOT NULL,
  PRIMARY KEY (`id_cliente`)
);

-Detalle Importante: En tu programa, hay un archivo llamado cliente_dao.py (lo encuentras dentro de la carpeta zona_fit_gui/). Asegúrate de que en ese archivo estén las credenciales correctas para que el programa se conecte a tu base de datos (tu nombre de usuario de MySQL, la contraseña que usas para MySQL y el host, que generalmente es localhost).

***4. Instalar lo que el programa necesita (Dependencias de Python) ***
Ahora, ve a la carpeta principal de tu proyecto en la terminal (donde descargaste el programa, por ejemplo, zona-fit-app):

cd zona-fit-app

-Es una buena práctica crear un "entorno virtual" para este proyecto. Esto mantiene las librerías de este programa separadas de otras librerías de Python en tu computadora:

python -m venv venv

Luego, "activa" este entorno virtual:

-Si usas Windows:

.\venv\Scripts\activate

-Si usas macOS o Linux:

source venv/bin/activate

Una vez que tu entorno virtual esté activo (verás (venv) al inicio de tu línea de comandos), instala la librería que el programa necesita para conectarse a MySQL:

pip install mysql-connector-python

***5. Iniciar la Aplicación ***

Con el entorno virtual aún activo, ejecuta el archivo principal del programa:

python zona_fit_app.py

Si tu archivo principal tiene un nombre diferente a zona_fit_app.py, cámbialo por el nombre correcto en el comando.

🤝 ¿Quieres mejorar el programa?
¡Tus ideas y ayuda son siempre bienvenidas! Si encuentras algún error (bug), tienes sugerencias para hacer el programa mejor o quieres agregar nuevas funciones, puedes:

Abrir un "Issue" (reportar un problema) en este mismo repositorio de GitHub.
Enviar un "Pull Request" (sugerir cambios directamente en el código).

📄 ¿Qué licencia tiene? (Licencia)
Este proyecto usa la Licencia MIT. Esto significa que puedes usar, modificar y distribuir el código libremente, siempre y cuando se incluya una copia de la licencia original. Puedes encontrar más detalles en el archivo LICENSE dentro de este repositorio.

👤 ¿Quién lo hizo?
Leonardo Llarena
github.com/LeonardoLlarena
linkedin.com/in/leonardo-llarena-9b247534a

---

## 👋 Agradecimientos

Este proyecto fue desarrollado como parte de mi proceso de aprendizaje en la Universidad Python en Udemy. Agradezco al  Ing. Ubaldo Acosta de GLobal Mentoring por los conocimientos y la guía proporcionados.

---
