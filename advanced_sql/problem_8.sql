/*
Wyszukanie ofert pracy z pierwszego kwartału, w których wynagrodzenie przekracza 70 tys. dolarów
- Połączone tabele ogłoszeń o pracę z pierwszego kwartału 2023 (styczeń-marzec)
- Oferty pracy ze średnim rocznym wynagrodzeniem > 70 000 USD
- Filtrowanie ofert pracy dla analityka danych i uporządkowane według wynagrodzenia
*/

SELECT
	job_title_short,
	job_location,
	job_via,
	job_posted_date::DATE,
    salary_year_avg
FROM (
    SELECT *
    FROM january_jobs
    UNION ALL
    SELECT *
    FROM february_jobs
    UNION ALL
    SELECT *
    FROM march_jobs
) AS quarter1_job_postings
WHERE
    salary_year_avg > 70000 AND
    job_title_short = 'Data Analyst'
ORDER BY
    salary_year_avg DESC