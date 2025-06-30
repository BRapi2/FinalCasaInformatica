
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/living.csv')

# 10 países con el costo de vida más alto
top10 = df.nlargest(10, 'Cost of living, 2017')
plt.figure(figsize=(10,6))
sns.barplot(x='Cost of living, 2017', y='Countries', data=top10, palette='Reds_r')
plt.title('Top 10 países con mayor costo de vida')
plt.xlabel('Costo de vida (2017)')
plt.ylabel('País')
plt.tight_layout()
plt.show()

# 10 países con el costo de vida más bajo
bottom10 = df.nsmallest(10, 'Cost of living, 2017')
plt.figure(figsize=(10,6))
sns.barplot(x='Cost of living, 2017', y='Countries', data=bottom10, palette='Greens')
plt.title('Top 10 países con menor costo de vida')
plt.xlabel('Costo de vida (2017)')
plt.ylabel('País')
plt.tight_layout()
plt.show()

# Costo de vida en países de América
america = df[df['Continent'] == 'America'].sort_values('Cost of living, 2017', ascending=False)
plt.figure(figsize=(10,8))
sns.barplot(x='Cost of living, 2017', y='Countries', data=america, palette='Blues_r')
plt.title('Costo de vida en países de América')
plt.xlabel('Costo de vida (2017)')
plt.ylabel('País')
plt.tight_layout()
plt.show()