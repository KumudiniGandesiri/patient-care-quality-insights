-- Patient Wait Time Analysis
SELECT 
    Department,
    AVG(Wait_Time_Minutes) AS Avg_Wait_Time,
    MAX(Wait_Time_Minutes) AS Max_Wait_Time,
    MIN(Wait_Time_Minutes) AS Min_Wait_Time
FROM Patient_Visits
GROUP BY Department
ORDER BY Avg_Wait_Time DESC;

-- Provider Performance: Delay Analysis
SELECT 
    Provider_Name,
    AVG(Actual_Duration - Scheduled_Duration) AS Avg_Delay,
    COUNT(*) AS Total_Visits
FROM Patient_Visits
GROUP BY Provider_Name
ORDER BY Avg_Delay DESC;

-- No-Show Rate by Department
SELECT 
    Department,
    SUM(CASE WHEN Visit_Status = 'No-Show' THEN 1 END) * 100.0 / COUNT(*) AS NoShowRate
FROM Patient_Visits
GROUP BY Department
ORDER BY NoShowRate DESC;

-- Satisfaction Score Trends
SELECT 
    Department,
    AVG(Satisfaction_Score) AS Avg_Satisfaction,
    COUNT(*) AS Total_Responses
FROM Patient_Visits
WHERE Satisfaction_Score IS NOT NULL
GROUP BY Department
ORDER BY Avg_Satisfaction ASC;

-- Wait Time vs Satisfaction Correlation
SELECT 
    Wait_Time_Minutes,
    AVG(Satisfaction_Score) AS Avg_Satisfaction
FROM Patient_Visits
GROUP BY Wait_Time_Minutes
ORDER BY Wait_Time_Minutes;
