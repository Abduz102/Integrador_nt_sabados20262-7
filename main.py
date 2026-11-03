import pandas as pd

from notebook.simulaciones.simular_usuario import generar_datos_limpios, ensuciar

from notebook.exportaciones.exportar_usuario import exportar_usuarios_crudos, exportar_usuarios_limpios

from notebook.limpiezas.limpiar_usuario import limpiar_usuarios, resumen_nulos

#1. Activando la simulacion
print("************ SIMULACIONES DE USUARIO ************")
usuarios_df=pd.DataFrame(generar_datos_limpios())
usuarios_sucios_df=ensuciar(usuarios_df)

#2. Exportando los datos crudos
print("************ EXPORTACIONES DE USUARIO ************")
rutas_crudas=exportar_usuarios_crudos(usuarios_sucios_df)
for ruta in rutas_crudas:
    print("Crudo:",ruta)

#3. Limpiando los datos
print("************ LIMPIEZA DE USUARIO ************")
usuarios_limpios_df=limpiar_usuarios(usuarios_sucios_df)
print(f"Filas antes: {len(usuarios_sucios_df)} | Filas despues: {len(usuarios_limpios_df)}")
print("Nulos por columna despues de limpiar:")
print(resumen_nulos(usuarios_limpios_df))

#4. Exportando los datos limpios
print("************ EXPORTACIONES DE USUARIO LIMPIOS ************")
rutas_limpias=exportar_usuarios_limpios(usuarios_limpios_df)
for ruta in rutas_limpias:
    print("Limpio:",ruta)


# ============================================================
#                      TABLA RETOS
# ============================================================
from notebook.exportaciones.exportar_reto import exportar_retos_sucios
from notebook.limpiezas.limpiar_reto import main as limpiar_retos
from notebook.consultas.consultas_reto import main as consultas_retos

print("\n************ EXPORTACIONES DE RETO (SUCIOS) ************")
exportar_retos_sucios()

print("\n************ LIMPIEZA DE RETO ************")
limpiar_retos()

print("\n************ CONSULTAS DE RETO ************")
consultas_retos()