import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('datos_.csv')

# 1. Distribución de Gastos Médicos
plt.figure(figsize=(10, 6))
sns.histplot(df['expenses'], kde=True)
plt.title('Distribución de los Gastos Médicos')
plt.xlabel('Gastos Médicos')
plt.ylabel('Frecuencia')
plt.show()

# 2. Gastos Médicos por Edad
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='expenses', data=df)
plt.title('Gastos Médicos por Edad')
plt.xlabel('Edad')
plt.ylabel('Gastos Médicos')
plt.show()

# 3. Gastos Médicos por Índice de Masa Corporal (BMI)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bmi', y='expenses', data=df)
plt.title('Gastos Médicos por Índice de Masa Corporal (BMI)')
plt.xlabel('BMI')
plt.ylabel('Gastos Médicos')
plt.show()

# 4. Gastos Médicos por Sexo
plt.figure(figsize=(10, 6))
sns.boxplot(x='sex', y='expenses', data=df)
plt.title('Gastos Médicos por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Gastos Médicos')
plt.show()

# 5. Gastos Médicos por Región
plt.figure(figsize=(10, 6))
sns.boxplot(x='region', y='expenses', data=df)
plt.title('Gastos Médicos por Región')
plt.xlabel('Región')
plt.ylabel('Gastos Médicos')
plt.show()

# 6. Relación entre Edad, BMI y Gastos Médicos diferenciando por Fumador
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='expenses', hue='bmi', size='smoker', data=df)
plt.title('Relación entre Edad, BMI y Gastos Médicos (Fumador/No Fumador)')
plt.xlabel('Edad')
plt.ylabel('Gastos Médicos')
plt.show()
