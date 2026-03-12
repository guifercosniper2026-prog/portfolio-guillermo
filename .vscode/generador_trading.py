import pandas as pd
import matplotlib.pyplot as plt

# 1. Creamos datos profesionales de ejemplo (EUR/USD)
data = {
    'Sesion': ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'],
    'Precio_Cierre': [1.0850, 1.0920, 1.0890, 1.0950, 1.1010],
    'Analisis': ['SMC - Liquidity Sweep', 'Turtle Soup', 'Range Theory', 'BOS Invalidate', 'Expansion NY']
}
df = pd.DataFrame(data)

# 2. Guardamos el archivo de Excel (CSV) para el botón verde
df.to_csv('reporte_profesional_trading.csv', index=False)
print("✅ Manzana 1: Archivo CSV creado con éxito.")

# 3. Creamos el gráfico azul para la web
plt.figure(figsize=(10,6))
plt.bar(df['Sesion'], df['Precio_Cierre'], color='#007AFF')
plt.title('Analisis Profesional EUR/USD - Guillermo')
plt.savefig('grafico_trading.png')
print("✅ Manzana 2: Gráfico PNG creado con éxito.")