
import pandas as pd

df = pd.read_csv('data/living.csv')

num_filas, num_columnas = df.shape

# Costo de vida promedio
costo_promedio = df['Cost of living, 2017'].mean()

# País con costo de vida más alto
pais_mas_caro = df.loc[df['Cost of living, 2017'].idxmax(), 'Countries']

# País con costo de vida más bajo
pais_mas_barato = df.loc[df['Cost of living, 2017'].idxmin(), 'Countries']

# Costo de vida y ranking de Perú
peru = df[df['Countries'] == 'Peru']
costo_peru = peru['Cost of living, 2017'].values[0]
ranking_peru = peru['Global rank'].values[0]

print(f"Nro. de Filas: {num_filas}")
print(f"Nro. de Columnas: {num_columnas}")
print(f"Costo de vida promedio: {costo_promedio:.2f}")
print(f"País con costo de vida más alto: {pais_mas_caro}")
print(f"País con costo de vida más bajo: {pais_mas_barato}")
print(f"Costo de Vida en Perú: {costo_peru}")
print(f"Ranking de Perú: {ranking_peru}")