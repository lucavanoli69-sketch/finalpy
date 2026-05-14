# BlogAutos

Blog automotor desarrollado con Django. Permite la publicación de artículos con un editor de texto enriquecido, incluye un sistema de autenticación de usuarios, gestión de perfiles y mensajería interna entre los usuarios registrados.

## Tecnologías

| Tecnología | Versión |
| --- | --- |
| Python | 3.10+ |
| Django | 4.2.7 |
| django-ckeditor | 6.7.0 |
| Pillow | 10.1.0 |

## Funcionalidades Principales

* **Blog**: Listado de publicaciones con paginación y detalle de cada artículo. Creación, edición y eliminación de publicaciones (CRUD) para usuarios autenticados.
* **Autenticación y Perfiles**: Registro, inicio y cierre de sesión. Cada usuario tiene un perfil público donde puede editar su biografía, foto de perfil y visualizar sus publicaciones.
* **Mensajería**: Sistema de mensajes privados entre usuarios registrados, con bandeja de entrada y mensajes enviados.

## Estructura del Proyecto

```text
BlogAutos/
├── BlogAutos/         # Configuración principal del proyecto
├── accounts/          # Aplicación de autenticación y perfiles
├── blog/              # Aplicación principal (publicaciones)
├── mensajes/          # Aplicación de mensajería interna
├── static/            # Archivos estáticos
├── templates/         # Plantillas HTML globales y por aplicación
├── requirements.txt   # Dependencias del proyecto
└── manage.py          # Script de gestión de Django
```

*Nota: La base de datos local (`db.sqlite3`) y los archivos subidos por los usuarios (`media/`) no se incluyen en el repositorio.*

## Instalación

1. Clonar el repositorio y acceder al directorio:
   ```bash
   git clone <url-del-repo>
   cd BlogAutos
   ```

2. Crear y activar un entorno virtual:
   * **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * **Linux/macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplicar las migraciones a la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Ejecución

Para iniciar el servidor de desarrollo, ejecutar el siguiente comando:

```bash
python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000`.

## Panel de Administración

Para gestionar la aplicación desde el panel de administrador, es necesario crear un superusuario:

```bash
python manage.py createsuperuser
```

Una vez creado, acceder a `http://127.0.0.1:8000/admin` e ingresar las credenciales. Desde este panel se pueden gestionar los usuarios, perfiles, publicaciones y mensajes.

## Autor

Proyecto desarrollado por Luca Vanoli.
