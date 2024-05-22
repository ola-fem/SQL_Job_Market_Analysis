import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych z pliku CSV
file_path = r'C:/Users/olafe/Desktop/1_top_paying_jobs.csv'
data = pd.read_csv(file_path)

# Wyświetlenie pierwszych kilku wierszy danych, aby sprawdzić poprawność wczytania
print(data.head())

# Dane
job_titles = data['job_title']
avg_salaries = data['salary_year_avg']



# Ustawienie palety kolorów na fioletową gradację
colors = sns.color_palette("Purples_r", len(job_titles))  # "_r" odwraca kolejność kolorów

# Tworzenie wykresu 
plt.figure(figsize=(10, 8))
plt.barh(job_titles, avg_salaries, color=colors)
plt.xlabel('Średnie wynagrodzenie ($)')
plt.title('Średnie wynagrodzenia dla Top 10 stanowisk analityków danych w 2023 roku')
plt.gca().invert_yaxis()  # Odwrócenie osi y, aby pierwsze stanowisko było na górze
plt.grid(axis='x', linestyle='--')  # Linie siatki pionowe
plt.gca().set_facecolor('lightgrey')  # Ustawienie szarego tła wykresu
plt.gcf().patch.set_facecolor('lightgrey')  # Ustawienie szarego tła poza wykresem
plt.tight_layout()  # Dopasowanie wykresu
plt.show()