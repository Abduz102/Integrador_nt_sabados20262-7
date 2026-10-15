# Rutina para generar archivos en diferentes formatos con Python
from pathlib import Path

# 1. Configuracion general de las rutas 
NOMBRE_ENTIDAD = "usuario"
CARPETA_PROYECTO=Path(__file__).resolve().parents[2]
CARPETA_CRUDOS=CARPETA_PROYECTO/"datos"/"crudos"
CARPETA_LIMPIOS=CARPETA_PROYECTO/"datos"/"limpios"
CARPETA_REPORTES=CARPETA_PROYECTO/"reportes"

# 2. Funciones genericas para crear los archivos
def preparar_carpeta(carpeta):
    carpeta.mkdir(parents=True, exist_ok=True)
    return carpeta

def exportar_csv(datos_df, carperta,nombre_archivo):
    ruta=preparar_carpeta(carpeta)/f"{nombre_archivo}.csv"
    datos_df.to_csv(ruta, sep=";")
    return ruta

def exportar_json(datos_df, carperta,nombre_archivo):
    ruta=preparar_carpeta(carpeta)/f"{nombre_archivo}.json"
    datos_df.to_json(ruta, orient="records", ident=2)
    return ruta

def exportar_excel(datos_df, carperta,nombre_archivo):
    ruta=preparar_carpeta(carpeta)/f"{nombre_archivo}.xlsx"
    datos_df.to_excel(ruta, engine="openpyxl")
    return ruta

# 3. LLamar las funciones para generar los archivos
def exportar_usuario_crudos(datos_df):
    return [
        exportar_csv(datos_df, CARPETA_CRUDOS, f"{NOMBRE_ENTIDAD}_crudos"),
        exportar_json(datos_df, CARPETA_CRUDOS, f"{NOMBRE_ENTIDAD}_crudos"),
        exportar_excel(datos_df, CARPETA_CRUDOS, f"{NOMBRE_ENTIDAD}_crudos")
    ]