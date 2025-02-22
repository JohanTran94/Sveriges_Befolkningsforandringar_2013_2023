import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. (Johan) Läs in och förbered data
file_path = 'processed_data_befolkningsförändringar.csv'  # Ange sökvägen till filen
data = pd.read_csv(file_path)  # Läs in filen
data.sort_values(by='år', ascending=True, inplace=True)  # Sortera värdena efter år

# 2. Beräkningar och analys
# (fayaz) Beräkna procentuell förändring
data['procentuell_ökning'] = data['folkmängd'].pct_change() * 100 

# Beräkna födelsetal, dödstal och naturlig befolkningstillväxt
data['Födelsetal (%)'] = (data['födda'] / data['folkmängd']) * 100
\data['Dödstal (%)'] = (data['döda'] / data['folkmängd']) * 100
\data['Naturlig befolkningstillväxt (%)'] = (data['födelseöverskott'] / data['folkmängd']) * 100

print(data[['år', 'Födelsetal (%)', 'Dödstal (%)', 'Naturlig befolkningstillväxt (%)']].head(10))

# 3. Visualiseringar
# (fayaz) Visualisera procentuell förändring av folkmängden
plt.figure(figsize=(10, 6))
plt.fill_between(data['år'], data['procentuell_ökning'], color='skyblue', alpha=0.5, label='Procentuell förändring')
plt.plot(data['år'], data['procentuell_ökning'], color='blue', linewidth=2, label='Trendlinje')
plt.title('Procentuell förändring av folkmängden per år')
plt.xlabel('År')
plt.ylabel('Procentuell förändring (%)')
plt.grid(True, linestyle='--', alpha=0.9)
plt.axhline(0, color='red', linestyle='--', linewidth=0.9, label='Ingen förändring')
plt.legend()
plt.xticks(data['år'])
plt.tight_layout()
plt.show()

# (Anmol) Visualisera relation mellan födda och döda
plt.figure(figsize=(12, 6))
bar_width = 0.35
index = range(len(data['år']))
plt.bar(index, data['födda'], bar_width, label='Födda', color='skyblue', edgecolor='black')
plt.bar([i + bar_width for i in index], data['döda'], bar_width, label='Döda', color='salmon', edgecolor='black')
plt.title('Relation mellan födda och döda per år')
plt.xlabel('År')
plt.ylabel('Antal personer')
plt.xticks([i + bar_width / 2 for i in index], data['år'])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# (Johan) Visualisera födelsetal, dödstal och naturlig befolkningstillväxt
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.25
index = np.arange(len(data))
ax.bar(index - bar_width, data['Födelsetal (%)'], bar_width, label='Födelsetal (%)', color='lightblue')
ax.bar(index, data['Dödstal (%)'], bar_width, label='Dödstal (%)', color='salmon')
ax.bar(index + bar_width, data['Naturlig befolkningstillväxt (%)'], bar_width, label='Naturlig befolkningstillväxt (%)', color='lightgreen')
ax.set_xticks(index)
ax.set_xticklabels(data['år'])
ax.set_xlabel('År')
ax.set_ylabel('Procent (%)')
ax.set_title('Befolkningstillväxt: Födelsetal, Dödstal & Naturlig Tillväxt')
ax.legend()
plt.xticks(rotation=45)
plt.show()

# 4. Regression och framtida prognoser
# Förbered data för regression
X = data[['år']]
y = data['tillväxttakt']

# Skapa och träna modellen
model = LinearRegression()
model.fit(X, y)

# Generera framtida år och förutsägelser
future_years = pd.DataFrame({'år': range(data['år'].max() + 1, data['år'].max() + 11)})
future_predictions = model.predict(future_years)

# Visualisera förutsägelser av befolkningstillväxt
plt.figure(figsize=(10, 6))
plt.plot(data['år'], data['tillväxttakt'], color='blue', marker="o", label='Historiska data')
plt.plot(data['år'], model.predict(X), color='green', label='Trend')
plt.plot(future_years, future_predictions, color='red', linestyle='--', label='Förutsägelser')
plt.xlabel('År', fontsize=12)
plt.ylabel('Tillväxttakt (%)', fontsize=12)
plt.title('Förutsägelse av Befolkningstillväxt', fontsize=16)
plt.xticks(range(data['år'].min(), future_years['år'].max() + 1), rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# (Viktoria) Visualisera invandring och utvandring
plt.figure(figsize=(10, 6))
plt.plot(data['år'], data['invandringar'], label='Invandring', marker='o')
plt.plot(data['år'], data['utvandringar'], label='Utvandring', marker='o')
plt.title('Invandring vs Utvandring per år', fontsize=16)
plt.xlabel('År', fontsize=12)
plt.ylabel('Antal personer', fontsize=12)
plt.xticks(data['år'])
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
