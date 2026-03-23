# 🛹 ChangoSkate

Aplicación web desarrollada con **Django** orientada a un e-commerce (tienda en línea) con funcionalidades de catálogo, carrito de compras y gestión básica.

---

## 📦 Requisitos

* Python 3.10+
* pip
* Git

---

## 📥 Clonar el repositorio

```bash
git clone git@github.com:Beca0999/ChangoSkate.git
cd ChangoSkate
```

---

## 🧪 Crear y activar entorno virtual

### Linux (Fish shell)

```bash
python3 -m venv venv
source venv/bin/activate.fish
```

### Linux / Bash

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 📦 Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ⚠️ Importante (estructura del proyecto)

El archivo `manage.py` **no está en la raíz**, sino dentro de la carpeta:

```bash
ecommers/
```

---

## ▶️ Ejecutar el proyecto

Primero entra a la carpeta correcta:

```bash
cd ecommers
```

Luego ejecuta:

```bash
python3 manage.py runserver
```

Abrir en navegador:

```
http://127.0.0.1:8000/
```

---

## 🗄️ Base de datos

* Se utiliza SQLite (`db.sqlite3`)
* Ya viene incluida para desarrollo

Si necesitas aplicar migraciones:

```bash
python3 manage.py migrate
```

---

## 📁 Estructura del proyecto

```
ChangoSkate/
├── ecommers/
│   ├── cart/          # Carrito de compras
│   ├── store/         # Lógica principal de tienda
│   ├── ecommers/      # Configuración Django
│   ├── static/        # Archivos estáticos
│   ├── media/         # Archivos subidos (imágenes)
│   ├── manage.py
│   └── db.sqlite3
├── requirements.txt
├── README.md
└── venv/ (no se sube al repo)
```

---

## 🧩 Funcionalidades

* Catálogo de productos
* Carrito de compras
* Manejo de imágenes de productos
* Templates con Django

---

## ⚠️ Notas

* La carpeta `media/` contiene archivos subidos (no recomendada para producción)
* `db.sqlite3` es solo para desarrollo
* Asegúrate de activar el entorno virtual antes de ejecutar el proyecto

---

## 👥 Autores

* Equipo ChangoSkate

---

## 📄 Licencia

Proyecto académico.
