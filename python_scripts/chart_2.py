import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
file_path = r'C:\Users\olafe\Desktop\2_top_paying_job_skills.csv'
data = pd.read_csv(file_path)

# Podsumowanie i podliczenie danych dla każdej umiejętności
skills_counts = data['skills'].value_counts().nlargest(10)

# Utworzenie wykresu
plt.figure(figsize=(10, 6))

# Ustawienie palety kolorów na gradację zielonego
colors = sns.color_palette("Greens_r", len(skills_counts))

# Stworzenie wykresu słupkowego
skills_counts.plot(kind='barh', color=colors, width=0.8)

plt.xlabel('Liczba wystąpień')
plt.ylabel('')
plt.title('Liczba umiejętności dla Top 10 najlepiej płatnych stanowisk analityka danych w 2023 r.')
plt.gca().invert_yaxis()  # Odwrócenie osi y, aby najwyższa umiejętność była na górze
plt.grid(axis='x', linestyle='--')  # Linie siatki pionowe
plt.gca().set_facecolor('lightgrey')  # Ustawienie szarego tła wykresu
plt.gcf().patch.set_facecolor('lightgrey')  # Ustawienie szarego tła poza wykresem
plt.tight_layout()  # Dopasowanie wykresu
plt.show()