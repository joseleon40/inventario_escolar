 🏫 Gestión de Inventario Escolar

Aplicación desarrollada con **Django** para gestionar equipos tecnológicos del Colegio Andes del Sur.  
Permite registrar, consultar y administrar equipos a través del **Django Admin**.

---

## 🚀 Instalación y ejecución

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tuusuario/inventario_escolar.git
   cd inventario_escolar
   ```

2. **Instalar dependencias:**

   ```bash
   pip install django
   ```

3. **Aplicar migraciones:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Crear superusuario:**

   ```bash
   python manage.py createsuperuser
   ```

5. **Ejecutar el servidor:**

   ```bash
   python manage.py runserver
   ```

6. **Acceder al panel de administración:**

   ```
   http://127.0.0.1:8000/admin
   ```

---

## 🧱 Modelo principal

**Equipo**

| Campo         | Tipo       | Ejemplo         |
|----------------|------------|-----------------|
| nombre         | CharField  | Notebook HP     |
| categoria      | CharField  | Notebook        |
| estado         | CharField  | Operativo       |
| fecha_ingreso  | DateField  | 2024-03-12      |
| ubicacion      | CharField  | Laboratorio 3   |

---


