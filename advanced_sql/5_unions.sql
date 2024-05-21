-- Oferty pracy i  nazwy firm ze stycznia
SELECT 
	job_title_short,
	company_id,
	job_location
FROM
	january_jobs

UNION ALL

-- Oferty pracy i  nazwy firm z lutego
SELECT 
	job_title_short,
	company_id,
	job_location
FROM
	february_jobs

UNION ALL -- połączenie kolejnej tabeli

-- Oferty pracy i  nazwy firm z marca
SELECT 
	job_title_short,
	company_id,
	job_location
FROM
	march_jobs