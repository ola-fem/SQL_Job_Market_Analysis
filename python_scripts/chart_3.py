import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
file_path = r'C:\Users\olafe\Desktop\3_top_demanded_skills.csv'
data = pd.read_csv(file_path)

# Utworzenie wykresu
plt.figure(figsize=(10, 8))  # Rozmiar wykresu (szerokość, wysokość)

# Ustawienie palety kolorów na gradację niebieskiego, z najciemniejszym kolorem na górze
colors = sns.color_palette("Blues_r", len(data))

# Stworzenie wykresu słupkowego pionowego
plt.bar(data['skills'], data['demand_count'], color=colors)
plt.xlabel('')
plt.ylabel('Liczba wystąpień')
plt.title('Top 5 najbardziej pożądanych umiejętności w ofertach pracy dla analityków danych')
plt.grid(axis='y', linestyle='--')  # Dodanie linii siatki poziomej
plt.gca().set_facecolor('lightgrey')  # Ustawienie szarego tła wykresu
plt.gcf().patch.set_facecolor('lightgrey')  # Ustawienie szarego tła poza wykresem
plt.tight_layout()  # Dopasowanie wykresu
plt.show()
