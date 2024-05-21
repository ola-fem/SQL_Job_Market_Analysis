/*
Sprawdzenie firm, które nie wymagają dyplomu(stopnia naukowego) 
- Wymagania dotyczące stopnia naukowego znajdują się w tabeli job_posting_fact.
- Użycie podzapytania, aby przefiltrować to w tabeli company_dim dla company_names
- uporządkowane alfabetycznie według nazwy firmy
*/

SELECT
    company_id,
    name AS company_name 
FROM 
    company_dim
WHERE company_id IN (
    SELECT 
            company_id
    FROM 
            job_postings_fact 
    WHERE 
            job_no_degree_mention = true
    ORDER BY
            company_id
)
ORDER BY
    name ASC

/*
Znalezienie firm, które mają najwięcej ofert pracy. 
- Uzyskanie całkowitej liczby ofert pracy według identyfikatora firmy (job_posting_fact)
- Zwrócenie całkowitej liczby ofert pracy z nazwą firmy (company_dim)
*/

WITH company_job_count AS (
    SELECT 
            company_id,
            COUNT(*) AS total_jobs
    FROM 
            job_postings_fact 
    GROUP BY
            company_id
)

SELECT 
    company_dim.name AS company_name,
    company_job_count.total_jobs
FROM 
    company_dim
LEFT JOIN company_job_count ON company_job_count.company_id = company_dim.company_id
ORDER BY
    total_jobs DESC