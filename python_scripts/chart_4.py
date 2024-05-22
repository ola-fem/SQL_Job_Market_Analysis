import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
file_path = r'C:\Users\olafe\Desktop\4_top_paying_skills.csv'
data = pd.read_csv(file_path)

#  10 umiejętności z najwyższym średnim wynagrodzeniem
top_10_skills = data.nlargest(10, 'avg_salary')

# Utworzenie wykresu
plt.figure(figsize=(10, 6))  # Rozmiar wykresu (szerokość, wysokość)

# Ustawienie palety kolorów na gradację pomarańczowego
colors = sns.color_palette("Oranges_r", len(top_10_skills))

# Stworzenie wykresu słupkowego poziomego
plt.barh(top_10_skills['skills'], top_10_skills['avg_salary'], color=colors)

plt.xlabel('Średnie wynagrodzenie ($)')
plt.ylabel('')
plt.title('Średnie wynagrodzenia dla 10 najlepiej płatnych umiejętności dla analityków danych')
plt.gca().invert_yaxis()  # Odwrócenie osi y, aby najwyższe wynagrodzenie było na górze
plt.grid(axis='x', linestyle='--')  # Dodanie linii siatki pionowej
plt.gca().set_facecolor('lightgrey')  # Ustawienie szarego tła wykresu
plt.gcf().patch.set_facecolor('lightgrey')  # Ustawienie szarego tła poza wykresem
plt.tight_layout()  # Dopasowanie wykresu
plt.show()
