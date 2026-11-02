import pandas as pd

from notebook.simulaciones.simular_usuario import generar_datos_limpios, ensuciar

from notebook.exportaciones.exportar_usuario import exportar_usuarios_crudos, exportar_usuarios_limpios

#1. Activando la simulacion
print("************ SIMULACIONES DE USUARIO ************")
usuarios_df=pd.DataFrame(generar_datos_limpios())
usuarios_sucios_df=ensuciar(usuarios_df)

#2. Exportando los datos
print("************ EXPORTACIONES DE USUARIO ************")
rutas_crudas=exportar_usuarios_crudos(usuarios_sucios_df)