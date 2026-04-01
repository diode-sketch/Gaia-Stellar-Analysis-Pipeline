import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

# 1. Cargar los datos reales de la ESA
try:
    df = pd.read_csv('Datos_de_ESA.csv')
    print("--- CONEXIÓN CON GAIA EXITOSA ---")
    
    # 2. Diagnóstico rápido: ¿Qué tenemos?
    print(f"Total de estrellas analizadas: {len(df)}")
    print("\nPrimeras 5 estrellas y sus distancias (parallax):")
    print(df[['source_id', 'parallax', 'phot_g_mean_mag']].head())

    # 3. Factor X: Encontrar la estrella más brillante del set
    mas_brillante = df.loc[df['phot_g_mean_mag'].idxmin()]
    print(f"\nESTRELLA MÁS BRILLANTE IDENTIFICADA:")
    print(f"ID: {mas_brillante['source_id']} | Magnitud: {mas_brillante['phot_g_mean_mag']}")

except FileNotFoundError:
    print("ERROR: El archivo 'estrellas_gaia.csv' no está en la carpeta MyPyScripts.")

# 1. Crear el gráfico
plt.figure(figsize=(10, 8))

# 2. Graficar Color (bp_rp) vs Brillo (phot_g_mean_mag)
# Invertimos el eje Y porque en astronomía las magnitudes más bajas son más brillantes
plt.scatter(df['bp_rp'], df['phot_g_mean_mag'], c=df['bp_rp'], cmap='RdYlBu_r', s=50)

plt.gca().invert_yaxis() 
plt.xlabel('Color de la Estrella (BP - RP)')
plt.ylabel('Brillo (Magnitud G)')
plt.title('Mi Primer Diagrama HR con Datos Reales de Gaia')
plt.grid(True, linestyle='--', alpha=0.6)
plt.colorbar(label='Índice de Color')

# 3. Mostrar el resultado
plt.show()