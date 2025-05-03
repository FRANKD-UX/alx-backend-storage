-- Lists all bands with Glam rock as main style, ranked by longevity
-- Column names: band_name and lifespan (in years until 2022)

SELECT band_name, 
       CASE 
           WHEN split IS NULL THEN (2022 - formed)
           ELSE (split - formed)
       END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
