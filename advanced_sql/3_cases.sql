/* 
Oznaczenie nowej kolumny w następujący sposób na podstawie job_location:
- 'Anywhere' jobs jako 'Remote'
- Lokalizacja „Nowy Jork, NY” jako „Local"
- W przeciwnym razie „Onsite"
*/

SELECT 
	COUNT(job_id) AS number_of_jobs,
    CASE
        WHEN job_location = 'Anywhere' THEN 'Remote'
        WHEN job_location = 'New York, NY' THEN 'Local'
        ELSE 'Onsite'
    END AS location_category
FROM 
    job_postings_fact
WHERE
    job_title_short = 'Data Analyst'
GROUP BY
    location_category
ORDER BY    
    number_of_jobs DESC;

