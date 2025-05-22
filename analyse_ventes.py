# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Génération d'un jeu de données fictif de ventes
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Produit': np.random.choice(['Produit A', 'Produit B', 'Produit C'], size=100),
    'Quantité': np.random.randint(1, 20, size=100),
    'Prix Unitaire': np.random.randint(10, 100, size=100),
}

# Création du DataFrame
df = pd.DataFrame(data)

# Calcul du chiffre d'affaire
df['Chiffre d’Affaire'] = df['Quantité'] * df['Prix Unitaire']

# Affichage des premières lignes du DataFrame
print(df.head())

# Analyse des ventes totales par produit
ventes_par_produit = df.groupby('Produit')['Chiffre d’Affaire'].sum().sort_values(ascending=False)
print(ventes_par_produit)

# Visualisation des ventes par produit
plt.figure(figsize=(8, 5))
sns.barplot(x=ventes_par_produit.index, y=ventes_par_produit.values, palette='viridis')
plt.title('Ventes totales par produit')
plt.xlabel('Produit')
plt.ylabel('Chiffre d’Affaire')
plt.show()

# Analyse des tendances des ventes au fil du temps
ventes_par_date = df.groupby('Date')['Chiffre d’Affaire'].sum()

# Visualisation des tendances des ventes
plt.figure(figsize=(10, 6))
plt.plot(ventes_par_date.index, ventes_par_date.values, label='Chiffre d’Affaire', color='b')
plt.title('Tendance des ventes au fil du temps')
plt.xlabel('Date')
plt.ylabel('Chiffre d’Affaire')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()
