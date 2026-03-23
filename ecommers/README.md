# 🛹 ChangoSkate - E-commerce Oficial

¡Bienvenidos al repositorio de **ChangoSkate**! Este es un proyecto de comercio electrónico desarrollado con **Django**, enfocado en la venta de equipo de skate y optimizado con estándares de **Accesibilidad Web (WCAG)** y **Seguridad**.

---

## 🚀 Guía de Instalación Local

Sigue estos pasos detallados para levantar el proyecto en tu computadora:

### 1. Clonar el repositorio
Abre tu terminal y descarga el proyecto:
\`\`\`bash
git clone https://github.com/Beca0999/ChangoSkate-Oficial.git
cd ChangoSkate-Oficial
\`\`\`

### 2. Configurar el Entorno Virtual (venv)
Es fundamental crear un entorno limpio para que las librerías no choquen con tu sistema:
\`\`\`bash
# Crear el entorno
python3 -m venv venv

# Activar en Linux/Mac:
source venv/bin/activate

# Activar en Windows:
# venv\Scripts\activate
\`\`\`

### 3. Instalación de Django y Dependencias
Una vez activado el entorno, instala las librerías necesarias que mencionamos en el audio:
\`\`\`bash
# Instalamos Django y Pillow (necesario para manejar las imágenes de los productos)
pip install django pillow

# O instalar todo desde el archivo de requerimientos:
pip install -r requirements.txt
\`\`\`

### 4. Preparar la Base de Datos
Para que se creen las tablas de productos y usuarios:
\`\`\`bash
python manage.py makemigrations
python manage.py migrate
\`\`\`

### 5. Crear acceso de Administrador
Para poder subir productos desde el panel de control:
\`\`\`bash
python manage.py createsuperuser
\`\`\`

### 6. Ejecutar el servidor
\`\`\`bash
python manage.py runserver
\`\`\`
Ahora entra a: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠️ Tareas Pendientes (Ver pestaña de Issues)
Hemos dividido el trabajo en **Issues** dentro de GitHub. Por favor, revisa tu tarea asignada:
1. **Accesibilidad:** Implementación de Modo Nocturno, Texto 200% y Guía de Voz.
2. **Seguridad:** Hashing de contraseñas con Bcrypt y prevención de SQL Injection.
3. **UI/UX:** Ajuste del Sticky Footer y vista responsiva de detalles.
4. **Multimedia:** Video promocional con subtítulos .VTT.

---

## ⚠️ Reglas del Repositorio
* **No subir el `venv/`**: Ya está en el `.gitignore`.
* **Ramas:** No trabajen directo en `main`. Creen una rama con su nombre: \`git checkout -b feature-mi-tarea\`.
* **Imágenes:** Todo producto nuevo debe tener una descripción de texto alternativo.

**Desarrollado por el equipo de ChangoSkate - 2026**
