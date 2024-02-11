# Comic Investment Analysis Project

## By Adam Meyer

## Project Start Date 2/8/2024

Welcome to the Comic Investment Analysis project! The aim of this project is to explore which comics offer the best investment opportunities for the future.

## Project Overview

Throughout this project, I will explore comic book investments to discern patterns and trends. My aim is to determine whether certain grades are better to invest in due to the interest in the series' name or if investing exclusively in the highest graded comics yields better returns.

I will begin by scraping data on comics, spanning from the golden age to the modern age. Notably, classics like Action Comics #1, the inaugural appearance of Superman, have seen significant value appreciation over time. Most recently, an Action Comics #1 which was originally sold for 10 cents and is now graded at a 6.0/10.0 grade sold for $3,180,000 on January 16th, 2022, while another copy graded 2.0/10.0 sold for $175,000 back in 2012 (based on gocollect.com). By the project's conclusion, I aim to provide insights into the investment potential of different comic book grades within popular series.

To streamline this analysis, I will concentrate solely on various comic series from Marvel and DC. The vast number of comics released over the last 86 years since the first release of Action Comics #1 necessitates this focused approach. Consequently, the conclusions drawn from this project will be specific to these series. However, it's important to note that focusing solely on Marvel and DC comics may introduce bias towards more well-known and inherently valuable comics. As a result, the conclusions drawn may not capture insights into the investment potential of lesser-known series or back issues. Therefore, the conclusions drawn from this project will offer valuable insights into which grades might be better to invest in based on the value of other grades within popular comic book series.

## Next Task
2/10 - collect DC series using data scraping methods. I need to load all the html to scrape all the names but the page makes the user scroll through the page to load. 

## Data Collection

I intend to gather grade sales data from gocollect.com utilizing Python's data scraping methods. Additionally to find data on each series from Marvel and DC to randomly choose a series to investigate, I will scrape the list of series from Marvel (https://www.marvel.com/comics/series) and DC (https://www.dcuniverseinfinite.com/browse/comics?sort=eyJkZWZhdWx0Ijp0cnVlLCJkaXJlY3Rpb24iOiJkZXNjIiwiZmllbGQiOiJmaXJzdF9yZWxlYXNlZCJ9&category=W10%3D&page=5&series).

## Comic Book Grading Scale

Understanding the grading scale is crucial for evaluating the condition and value of comic books accurately. Below is a breakdown of the grading scale commonly used in the comic book industry:

- Gem Mint 10: The highest grade assigned. The collectible must have no evidence of any manufacturing or handling defects.

- Mint 9.9: The collectible is nearly indistinguishable from a 10.0 but will have a very minor manufacturing defect. It will not have any evidence of handling defects.

- Near Mint/Mint (NM/M) 9.8: A nearly perfect collectible with negligible handling or manufacturing defects.

- Near Mint Plus (NM+) 9.6: A very well-preserved collectible with several minor manufacturing or handling defects.

- Near Mint (NM) 9.4: A very well-preserved collectible with minor wear and small manufacturing or handling defects.

- Near Mint Minus (NM-) 9.2: A very well-preserved collectible with some wear and small manufacturing or handling defects.

- Very Fine/Near Mint (VF/NM) 9.0: A very well-preserved collectible with good eye appeal. There will be a number of minor handling and/or manufacturing defects.

- Very Fine Plus (VF+) 8.5: An attractive collectible with a moderate defect or a number of small defects.

- Very Fine (VF) 8.0: An attractive collectible with a moderate defect or an accumulation of small defects.

- Very Fine Minus (VF-) 7.5: An above-average collectible with a moderate defect or an accumulation of small defects.

- Fine/Very Fine (FN/VF) 7.0: An above-average collectible with a major defect or an accumulation of small defects.

- Fine Plus (FN+) 6.5: An above-average collectible with a major defect and some smaller defects, or a significant accumulation of small defects.

- Fine (FN) 6.0: A slightly above-average collectible with a major defect and some smaller defects, or a significant accumulation of small defects.

- Fine Minus (FN-) 5.5: A slightly above-average collectible with several moderate defects.

- Very Good/Fine (VG/FN) 5.0: An average collectible with several moderate defects.

- Very Good Plus (VG+) 4.5: A slightly below-average collectible with multiple moderate defects.

- Very Good (VG) 4.0: A below-average collectible with multiple moderate defects.

- Very Good Minus (VG-) 3.5: A below-average collectible with several major defects or an accumulation of multiple moderate defects.

- Good/Very Good (G/VG) 3.0: A collectible that shows significant evidence of handling with several moderate-to-major defects.

- Good (G) 2.5: A collectible that shows extensive evidence of handling with multiple moderate-to-major defects.

- Good Minus (G-) 2.0: A collectible that shows extensive evidence of handling with numerous moderate-to-major defects.

- Fair/Good (Fa/G) 1.5: A collectible that shows extensive evidence of handling with a heavy accumulation of major defects.

- Fair (Fa) 1.0: A very poorly handled collectible with a heavy accumulation of major defects.

- Poor 0.5: A heavily defaced collectible with a number of major defects. Some pieces will also be missing.

Understanding the nuances of the grading scale is essential for collectors and investors to make informed decisions when buying, selling, and valuing comic books. Always carefully inspect each comic and consider its grade when assessing its market value and investment potential.

## Get Involved

Your input is valuable! If you have any questions, comments, or suggestions regarding the project, please don't hesitate to reach out. I'll keep you informed of the project's progress and welcome any insights you may have.