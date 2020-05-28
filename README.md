# ohio-birth-weights

Data exploration on Ohio birth weights from 2006 - 2017.

Low birth weight infants can experience critical medical complications. Investigating and identifying potential maternal and environmental risk factors could aid in making informed decisions on intervention methods.

## Purpose / Emphasis

The notebook emphasizes the following skills:
  * Reading in data and creating dataframes with Pandas.
  * Cleaning, relabelling, and organizing data for presentation.
  * Creating and fine-tuning various plots using Matplotlib.
  * Representing geographical data through Plotly.
  * Inferring and drawing conclusions from data.

Code is written with the intention of notebook cells to run without dependency on previous cells after initial dataframe construction. This is in hopes of users copying and modifying plot attributes for their own projects without much hassle.

---

## Prerequisites

The following interface / packages are neccessary for proper function:

Requirement | Version
------------|--------
[Jupyter Notebook](https://jupyter-notebook.readthedocs.io/) | 6.0.3
[Pandas](https://pandas.pydata.org/) | 1.0.1
[Matplotlib](https://matplotlib.org/) | 3.1.3
[NumPy](https://numpy.org/) | 1.18.1
[Plotly](https://plotly.com/python/getting-started/) | 4.5.0

Installation instructions for these modules can be found through their respective documentation.

---

## Data

 Ohio birth weight data is divided among two csv files:

- ohio_department_of_health__0e4c79bc_1ac0_4c88_a85f_425400be5d0d
  - Births are classified by the age range of the mother.
  
- ohio_department_of_health__e870fd77_dee8_4109_b62d_054843fa3bd5
  - Births are classificed by race and ethnicity. 

County-specific data can be found in the following csv file:

- ohio_county_data
  - FIPS codes for Ohio counties - used for plotting county-specific data. 
  
Both Department of Health datasets classify births as either **low birth weight** (<2500g) or **normal birth weight** (2500g+) and are further seperated by year and county name.

Further information about the birth data used in this notebook can be found [here](https://discovery.smartcolumbusos.com/?q=health). The use and redistribution of this data is allowable under Creative Commons Attribution License (cc-by). There is no affiliation with the Ohio Department of Health.

FIPS codes used in ohio_county_data can be found [here](https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697). The use and redistribution of this data is allowable under theFreedom of Information Act (FOIA).There is no affiliation with U.S. Department of Agriculture.

---

## Cloning

Clone this repo to your computer with https://github.com/chalvarado96/ohio-birth-weights/.

---

## Author

- **Chance Alvarado** 
    - [LinkedIn]()
    - [Github]()

---    

## License

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
