/*
 Pytanie: Jakie są najbardziej pożądane umiejętności analityków danych (praca zdalna)?
*/


SELECT 
  skills,
  COUNT(skills_job_dim.job_id) AS demand_count
FROM job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE
  job_title_short = 'Data Analyst' AND
  job_work_from_home = TRUE
GROUP BY
  skills
ORDER BY
  demand_count DESC
LIMIT 5


/*

Oto zestawienie najbardziej poszukiwanych umiejętności analityków danych w 2023 r:
SQL i Excel pozostają podstawą, podkreślając potrzebę posiadania silnych, podstawowych umiejętności w zakresie 
przetwarzania danych i manipulowania arkuszami kalkulacyjnymi.
Narzędzia do programowania i wizualizacji, takie jak Python, Tableau i Power BI, 
są niezbędne, co wskazuje na rosnące znaczenie umiejętności technicznych w opowiadaniu historii o danych i wspieraniu decyzji.

[
  {
    "skill_id": 0,
    "skill_name": "sql",
    "skill_count": "7291"
  },
  {
    "skill_id": 181,
    "skill_name": "excel",
    "skill_count": "4611"
  },
  {
    "skill_id": 1,
    "skill_name": "python",
    "skill_count": "4330"
  },
  {
    "skill_id": 182,
    "skill_name": "tableau",
    "skill_count": "3745"
  },
  {
    "skill_id": 183,
    "skill_name": "power bi",
    "skill_count": "2609"
  }
]
*/