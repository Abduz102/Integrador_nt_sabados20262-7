#Alistamiento para ejecutar rutina de limpieza
import pandas as pd 
from notebook.exportaciones.exportar_usuario import CARPETA_CRUDOS, NOMBRE_ENTIDAD

#Definiendo los datos correctos
ROLES=["ADMIN","EMPRESA","PARTICIPANTE"]


#Definiendo funciones base
def verificar_dato_vacio(dato):
    return pd.isna(dato) or dato.strip()=="" 

#Funciones basicas de limpeiza por dato
 
#nombre (texto)
def limpiar_nombre(nombre):
    if verificar_dato_vacio(nombre):
        return None
    nombre=nombre.strip()
    return nombre.title()

#correo (texto)
def limpiar_correo(correo):
    if verificar_dato_vacio(correo):
        return None
    correo=correo.strip()
    return correo.lower()

#contrasena_hash (texto)
def limpiar_contrasena(contrasena):
    if verificar_dato_vacio(contrasena):
        return None
    contrasena=contrasena.strip()
    return contrasena.title()

#rol (texto)
def limpiar_rol(rol):
    if verificar_dato_vacio(rol):
        return None 
    if rol not in ROLES:
        return None
    return rol 


#activo (booleano)
def limpiar_activos(activo):
    if verificar_dato_vacio(activo):
        return None 
    if activo in ["Si","SI","sí","si","1"]:
        return True
    if activo in ["No","NO","no","0"]:
        return False
    return None
#fecha_registro (fecha y hora)