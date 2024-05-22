import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
file_path = r'C:\Users\olafe\Desktop\5_optimal_skills.csv'
data = pd.read_csv(file_path)

# Utworzenie wykresu punktowego
plt.figure(figsize=(10, 8))  # Rozmiar wykresu (szerokość, wysokość)

# Generowanie własnej palety kolorów z gradacją
num_colors = len(data['skills'].unique())
colors = sns.color_palette("viridis", num_colors)

# Stworzenie wykresu punktowego
sns.scatterplot(data=data, x='demand_count', y='avg_salary', hue='skills', palette=colors)

plt.xlabel('Liczba wystąpień')
plt.ylabel('Średnie wynagrodzenie')
plt.title('Zależność między liczbą wystąpień a średnim wynagrodzeniem dla umiejętności')
plt.grid(True)  # Dodanie siatki na wykresie
plt.gcf().patch.set_facecolor('lightgrey')  # Ustawienie szarego tła poza wykresem
plt.gca().set_facecolor('lightgrey')  # Ustawienie szarego tła wykresu

# Ustawienie legendy po prawej stronie
plt.legend(title='Umiejętność', bbox_to_anchor=(1.02, 1), loc='upper left')

# Zaktualizowanie tła legendy na jasnoszare
plt.legend(title='Umiejętność', bbox_to_anchor=(1.02, 1), loc='upper left', facecolor='lightgrey')

plt.tight_layout()  # Dopasowanie wykresu
plt.show()
