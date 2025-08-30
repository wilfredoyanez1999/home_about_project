# HomeAbout Django Project

Este proyecto es una aplicación web construida con Django que incluye páginas de inicio y acerca de.

## Estructura del proyecto
- `manage.py`: Script principal para la gestión del proyecto Django.
- `db.sqlite3`: Base de datos SQLite utilizada por Django.
- `django_base/`: Configuración principal del proyecto (settings, urls, wsgi, asgi).
- `pages/`: Aplicación Django que gestiona las vistas, modelos y URLs de las páginas.
- `templates/`: Archivos HTML para las vistas (`home.html`, `about.html`, `_base.html`).
- `requirements.txt`: Dependencias necesarias para ejecutar el proyecto.

## Instalación
1. Clona el repositorio:
   ```powershell
   git clone <URL-del-repositorio>
   cd homeabout
   ```
2. Instala las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
3. Realiza las migraciones:
   ```powershell
   python manage.py migrate
   ```
4. Ejecuta el servidor de desarrollo:
   ```powershell
   python manage.py runserver
   ```

## Uso
- Accede a la página principal en `http://localhost:8000/`.
- Accede a la página "Acerca de" en `http://localhost:8000/about/`.

## Licencia
Este proyecto está bajo la licencia MIT.
