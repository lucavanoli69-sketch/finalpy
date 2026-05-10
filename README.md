# 🚗 BlogAutos

> Blog automotor moderno construido con Django 4.2 — diseño oscuro premium, CRUD completo, mensajería entre usuarios y editor enriquecido.

---

## 📋 Tabla de Contenidos

- [Tecnologías](#tecnologías)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Comandos](#comandos)
- [Funcionalidades](#funcionalidades)
- [Credenciales Admin](#credenciales-admin)

---

## 🛠 Tecnologías

| Tecnología | Versión |
|---|---|
| Python | 3.10+ |
| Django | 4.2.7 |
| django-ckeditor | 6.7.0 |
| Pillow | 10.1.0 |
| Bootstrap | 5.3.2 (CDN) |

---

## 📁 Estructura del Proyecto

```
BlogAutos/
│
├── BlogAutos/              # Configuración principal
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── blog/                   # App principal del blog
│   ├── models.py           # Modelo Post
│   ├── views.py            # CRUD (CBV + decoradores)
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── accounts/               # Autenticación y perfiles
│   ├── models.py           # Modelo Profile
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── mensajes/               # Mensajería entre usuarios
│   ├── models.py           # Modelo Mensaje
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── templates/              # Templates con herencia
│   ├── base.html           # Template padre
│   ├── blog/
│   ├── accounts/
│   └── mensajes/
│
├── static/                 # Archivos estáticos
├── media/                  # Archivos subidos (ignorado en git)
├── requirements.txt
└── .gitignore
```

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repo>
cd BlogAutos
```

### 2. Crear y activar entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario

```bash
python manage.py createsuperuser
```

### 6. Colectar archivos estáticos (opcional para desarrollo)

```bash
python manage.py collectstatic
```

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

Abrí tu navegador en **http://127.0.0.1:8000**

---

## ⚙️ Comandos

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Servidor de desarrollo
python manage.py runserver

# Shell de Django
python manage.py shell
```

---

## ✅ Funcionalidades

### Blog
- ✅ Home con listado de posts y paginación
- ✅ Detalle de post con contenido enriquecido (CKEditor)
- ✅ Crear, editar y eliminar posts (solo logueados)
- ✅ Botón "Leer más" en cada tarjeta
- ✅ Imagen destacada por post
- ✅ Mensaje "No hay páginas aún" cuando no hay posts
- ✅ Página About

### Autenticación
- ✅ Login / Logout
- ✅ Registro con username, email y contraseña
- ✅ Redirección tras login/logout

### Perfil
- ✅ Vista de perfil público
- ✅ Editar avatar y bio
- ✅ Cambio de contraseña
- ✅ Posts del usuario en el perfil

### Mensajes
- ✅ Bandeja de entrada (inbox)
- ✅ Mensajes enviados
- ✅ Enviar mensaje a cualquier usuario
- ✅ Precarga destinatario desde perfil de usuario

### Técnico
- ✅ Herencia de templates (`base.html`)
- ✅ CBV: `ListView`, `DetailView`, `CreateView`, `UpdateView`
- ✅ Mixin: `LoginRequiredMixin`
- ✅ Decorador: `@login_required`
- ✅ Admin registrado para todos los modelos
- ✅ Archivos media configurados
- ✅ CKEditor con uploader
- ✅ Bootstrap 5

---

## 🔐 Admin

Accedé al panel de administración en **http://127.0.0.1:8000/admin** con las credenciales del superusuario creado.

Desde el admin podés gestionar: **Posts**, **Perfiles** y **Mensajes**.

---

## 📄 Licencia

Proyecto académico — BlogAutos © 2024
