<style>
table { width: 100%; table-layout: fixed; font-size: 9pt; }
td, th { word-wrap: break-word; overflow-wrap: anywhere; vertical-align: top; }
td code { white-space: normal; word-break: break-all; font-size: 8pt; }
th:nth-child(1), th:nth-child(2) { width: 9%; }
</style>
##### Project Check-In Report - Troy Chin, Mohammed Khalaf, Daniel Boynton
## Modeling and Forecasting COVID-19 Dynamics in the United States Using Logistic Growth Models
### Application and Dataset

During the COVID pandemic, health officials, hospitals and governments had to make decisions with incomplete information, like how many hospital beds and staff to prepare or when to tighten or relax restrictions. Using mathematical models, we can measure how case counts grow so we can predict the trajectory of an outbreak in the short-term. Logistic growth models are one such prediction model. If this model fits well with existing COVID-19 data, it could help forecast how an ongoing wave will play out and make those important regulatory decisions be much more substantive and accurate. 

Our World in Data (OWID) is a nonprofit online research publication that compiles high-quality global datasets on more than 120 topics such as "poverty, CO2 emissions and climate change, migration, democracy, global health...and more". [1] During the pandemic it maintained one of the most widely used COVID-19 datasets, which collects case, death, testing and vaccination figures for every country in a consistent format. [2]

We use two files from OWID's COVID-19 dataset: `total_cases.csv` (cumulative confirmed COVID-19 cases) and `total_deaths.csv` (cumulative confirmed COVID-19 deaths). Each file has a `date` column plus one column for each of 246 locations: 234 countries and territories, and 12 aggregate regions. The rows cover January 5, 2020 to August 4, 2024 and are measured in weekly counts. After cleaning, the U.S. data has 237 weekly observations.

OWID uses the World Health Organization's COVID-19 data, adds regional and income-group totals, and republishes them. [3]

There are some reporting limitations such as confirmed case counts depending on testing availability, reporting practices, and surveillance systems. Testing was very limited in early 2020, and from 2022 onward, many people used at-home rapid tests not reporting their results. US reporting also ended in 2023 while deaths were reported through August 2024, and a few countries have small downward corrections to their totals for various reasons.

### Progress Made So Far

Our team has collected the COVID-19 cases and deaths datasets, cleaned the data, and organized our GitHub repository. We have also created a Python notebook that imports and processes the data, along with preliminary graphs showing how COVID-19 cases and deaths changed over time in the United States. Our next steps are to analyze individual COVID-19 waves, calculate deaths per reported case, and evaluate how accurately logistic growth models can predict future cases.

### Goal and EDA Questions
**Goal:** Can classical continuous logistic growth models describe the progression of cumulative reported COVID-19 cases in the United States, and how effectively can the continuous logistic model forecast short-term changes in reported cases?

**Concrete Questions EDA can answer and the plans to answer them:**

1. What is the data's quality and structure, and what limits does it place on the analysis?
    - *(Completed in `data_cleaning.ipynb`)* We checked both files for missing values, gaps between dates, and whether their dates and columns matched. Then we checked which weekdays the cumulative counts changed on, finding they update only on Sundays. We checked for any decrease in cumulative totals and found there were a handful of countries with revisions present. Finally, we found the last week with new U.S. cases and flagged later weeks with a new column.
2. How did U.S. weekly new cases and deaths change over time?
    - *(Completed in `data_cleaning.ipynb`)* We rescaled the counts with `.assign()`, reshaped them into one `measure` column with `.melt()`, and plotted them as line graphs. The plots show distinct waves, a uniquely large spike in January 2022, and a different pattern for deaths.
3. When does each epidemic wave start, peak and end, and does cumulative cases within each wave follow an S-shape?
    - Using the weekly new cases plot from question 2, we will record each wave's start week, peak week and end week, and add a `wave` column to the U.S. table. Using `groupby("wave")`, we will summarize each wave's length in weeks, peak weekly cases and total cases in a table. We will then compute cumulative cases since each wave's start and plot them as line graphs with `facet_wrap(facets="wave", scales="free")` to check whether each wave follows the S-shape the logistic model assumes.
4. Within each wave, does the growth rate slow down the way the logistic model predicts, falling in a straight line as cumulative cases increase?
    - Within each wave, we will compute the weekly growth rate as new cases divided by cumulative cases since the wave began. We will make scatter plots of growth rate against cumulative cases with `geom_point`, faceted by wave, and fit a simple linear regression for each wave.
5. How did the number of deaths per reported case differ between waves?
    - Using the `wave` column from question 3, we will compute a weekly deaths-per-case ratio with `.assign()`, dividing weekly new deaths by weekly new cases, using only weeks before May 2023, when both series were reported. We will compare waves with side-by-side box plots. We will also use `groupby("wave")` to make a table of each wave's total deaths divided by total cases.
### Model Plan
We will fit the continuous logistic growth model, N(t) = K / (1 + A*e^(-rt)), to each wave identified by Question 3 using nonlinear least squares with `scipy.optimize.curve_fit`. Here t is weeks since the wave's start and K is the wave's fitted upper limit; initial guesses for K and r come from Question 4. To avoid training on future data, each wave is split chronologically: the model is trained up to a cutoff week and forecasts cumulative cases 1, 2 and 4 weeks ahead. Forecasts will be evaluated with MAE, RMSE and R^2, and compared against a naive baseline to test whether the logistic model adds forecasting value. Results appear in Figures 5-6 and Table 4. Implementing a discrete logistic model is an extra goal if we have time.
### Figures and Tables
Each figure will have a descriptive title, labeled axes with units, and a legend where color or facets encode a variable.
#### EDA Questions
- **Table 1: Data Quality summary** (Question 1, completed)
- **Figure 1: U.S. cumulative cases, weekly new cases, and weekly new deaths** (Question 2, completed).
- **Table 2: Wave summary** (Question 3 and Question 5)
- **Figure 2: Cumulative cases within each wave** (Question 3)
- **Table 3: Growth rate vs. cumulative cases, by wave** (Question 4)
- **Figure 3: Growth-rate regression results by wave** (Question 4)
- **Figure 4: Weekly deaths per case, by wave** (Question 5)
#### Model
- **Figure 5: Logistic fits vs. observed cumulative cases, by wave**
- **Figure 6: Forecasts vs. actual cumulative cases**
- **Table 4: Forecast error metrics**
### Timeline and Team Split
| Week | Dates | Troy | Mohammed | Daniel |
|---|-----|-----|-----|-----|
| Wk 1 | 11/9 - 11/15 | design model plan, file structure, create repo<br>Deliverables: `README.md`, `exploratory_data_analysis.ipynb`  | Write report sections<br>Deliverables: sections of `reports/checkin_report.pdf`| Q1-Q2, Table 1, Figure 1, <br>Deliverables: `notebooks/data_cleaning.ipynb`, `data/processed/us_covid_clean.csv`, `figures/fig1_us_cases_deaths.png`, `reports/checkin_report.pdf` |
| Wk 2 | 11/16 - 11/22 | build the logistic fitting pipeline with `curve_fit` on one test wave, including the chronological train/forecast split<br>Deliverables: `Python/continuous_logistic_model.py`, `notebooks/logistic_model_fitting.ipynb` (test wave) | Q5, compute weekly deaths per case, box plots by wave<br>Deliverables: `notebooks/deaths_per_case.ipynb`, `figures/fig4_deaths_per_case.png`, deaths columns of `results/table2_wave_summary.csv` | Q3: define waves and add the `wave` column<br>Deliverables: `notebooks/wave_analysis.ipynb`, `data/processed/us_covid_waves.csv`, `results/table2_wave_summary.csv`, `figures/fig2_wave_cumulative.png` |
| Wk 3 | 11/23 - 11/29 | fit the logistic model to every wave; save the fitted parameters<br>Deliverables: `notebooks/logistic_model_fitting.ipynb` (all waves), `results/estimated_parameters.csv`,`figures/fig5_logistic_fits.png` | Code the naive baseline and the MAE/RMSE/R^2 evaluation<br>Deliverables: `Python/model_evaluation.py` | Q4: growth-rate regressions by wave; send K and r initial guesses to Troy<br>Deliverables: `notebooks/growth_rate_analysis.ipynb`, `figures/fig3_growth_rate.png`, `results/table3_growth_regression.csv` |
| Wk 4 | 11/30 - 12/6 | Run 1/2/4-week forecasts; write the Model and Results sections of the report<br>Deliverables: `Python/forecasting.py`, `results/forecast_predictions.csv`, `figures/fig6_forecasts.png`, Model and Results sections of `reports/final_report.pdf` | Compare logistic vs. baseline metrics; make sure every notebook runs top to bottom; write the final README<br>Deliverables: `results/model_metrics.csv` (Table 4), cleaned-up `notebooks/`, final `README.md` | Write the EDA sections (Q1-Q5 results and figure captions); assemble the full report draft<br>Deliverables: EDA sections and full draft of `reports/final_report.pdf` |
| Wk 5 | 12/7 - 12/8 | Review the report and slides; make and present the model slides; submit everything <br>Deliverables: model slides in `reports/final_presentation.pdf`, submitted zip and github link of the repo | Review the report and slides; make and present the deaths/data slides<br>Deliverables: EDA slides in `reports/final_presentation.pdf` | Final edits and formatting; make and present the wave/growth slides<br>Deliverables: final `reports/final_report.pdf`, `reports/final_presentation.pdf` |

### Citations
[1] Max Roser, “About,” Our World in Data, 2015. https://ourworldindata.org/about.

[2] E. Mathieu et al., “COVID-19 pandemic,” Our World in Data. https://ourworldindata.org/coronavirus.

[3] World Health Organization, "WHO COVID-19 Dashboard," Geneva: World Health Organization, 2020. https://data.who.int/dashboards/covid19.
