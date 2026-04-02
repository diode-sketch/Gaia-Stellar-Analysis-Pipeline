import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1. Load real data from ESA
try:
    df = pd.read_csv('Datos_de_ESA.csv')
    print("--- SUCCESSFUL CONNECTION WITH GAIA ---")
    
    # 2. Quick diagnosis: What do we have?
    print(f"Total stars analyzed: {len(df)}")
    print("\nFirst 5 stars and their distances (parallax):")
    print(df[['source_id', 'parallax', 'phot_g_mean_mag']].head())

    # 3. X-Factor: Finding the brightest star in the set
    brightest = df.loc[df['phot_g_mean_mag'].idxmin()]
    print(f"\nBRIGHTEST STAR IDENTIFIED:")
    print(f"ID: {brightest['source_id']} | Magnitude: {brightest['phot_g_mean_mag']}")

except FileNotFoundError:
    print("ERROR: The file 'estrellas_gaia.csv' was not found in the MyPyScripts folder.")

# 1. Create the plot
plt.figure(figsize=(10, 8))

# 2. Plot Color (bp_rp) vs Brightness (phot_g_mean_mag)
# We invert the Y-axis because in astronomy, lower magnitudes represent brighter objects
plt.scatter(df['bp_rp'], df['phot_g_mean_mag'], c=df['bp_rp'], cmap='RdYlBu_r', s=50)

plt.gca().invert_yaxis() 
plt.xlabel('Star Color (BP - RP)')
plt.ylabel('Brightness (G Magnitude)')
plt.title('My First HR Diagram with Real Gaia Data')
plt.grid(True, linestyle='--', alpha=0.6)
