# 🐾 PARCIAL FINAL

> **Jueves, 12 de Junio, 2025**

## 📖 Descripción

**Enunciado** Bienvenido al equipo sigmotoa dev, una empresa con presencia en varios países y diversidad de clientes. En esta ocasión se ha asignado el proyecto "sigmotoaFligths" un desarrollo en asociación con una de las aereolínea que pretende llevar mascotas en vuelos. Se ha solicitado construir un desarrollo funcional que permita a los usuarios reservar y comprar vuelos en los que sus mascotas son lo principal. Cualquier usuario debe poder conectarse al sistema, ver vuelos disponibles y hacer reservas para viajar con su mascota y finalizar la compra. También se debe poder consultar la cantidad de mascotas que ya tienen un boleto comprado en un vuelo.

### ✨ Características Principales

- 🏠 **Identidad del desarrollo en el modelo web**
- 📱 **Desplegable**
- 🖼️ **Diagrama de casos de uso y clases**
- 🗃️ **Registro de usuaios**
- 🐕 **Registro de mascotas**
- 🔄 **Gestiones de usuario y mascotas**
- 📊 **Conexión a bases de datos**
- 🗂️️ **Repositorio GitHUb**

### ✨ Modelado de las entidades 📚
```mermaid
classDiagram
    class Flights {
        id: Optional[int]
        origen: str
        destino: str
        fecha: str
    }

    class Pets {
        id: Optional[int]
        id_vuelo: int
        nombre: str
        edad: int
        raza: str
    }

    class Users {
        id: Optional[int]
        id_vuelo: int
        nombre: str
        nombre_mascota: str
    }

```

### ✨ Diagrama de casos de uso 🗒️

### Casos de Uso📊
1. **Gestionar Vuelos ✈️**:
   - Crear vuelo.
   - Consultar vuelos.
   - Consultar vuelo específico.
   - Actualizar vuelo.
   - Eliminar vuelo.

2. **Gestionar Mascotas 🐶**:
   - Crear mascota asociada a un vuelo.
   - Consultar mascotas.
   - Consultar mascota específica.
   - Actualizar datos de una mascota.
   - Eliminar mascota.
   - 
3. **Gestionar Usuarios 👥**:
   - Crear usuario.
   - Consultar usuarios.
   - Consultar usuario específica.
   - Actualizar usuario.
   - Eliminar usuario.
     
  **Este diseño de casos de uso** organiza la funcionalidad del sistema en relación con la gestión de vuelos, mascotas y usuarios. Cada operación está diseñada para garantizar la conexión entre las entidades principales del sistema, manteniendo la trazabilidad entre los vuelos y las entidades relacionadas (usuarios y mascotas).
  
### ✨ Diagrama de clases 🗒📋
**✈️ Diagrama de vuelos ✈️**


![imagen](https://github.com/user-attachments/assets/97b851ad-07e4-4f81-93b5-e2461565b420)


**🐶 Diagrama de mascotas 🐶**


![imagen](https://github.com/user-attachments/assets/08ff31d9-8058-4c26-b569-701f9046eb0c)


**👥 Diagrama de usuarios 👥**


![imagen](https://github.com/user-attachments/assets/56580bca-5706-42fc-90ce-7317b04a13f4)


  



## 🌐 Para ver el despliege puedes ir a los siguientes enlaces

- Repositorio: https://github.com/JuanLozanooo/ParcialFinal.git
- Despligue: https://parcialfinal-s68k.onrender.com
