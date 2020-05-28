# exploring-ohio-birth-weights

Data exploration on Ohio birth weights from 2006-2017.

---

## Introduction

Low birth weight infants can experience critical medical complications. Investigating and identifying potential maternal and environmental risk factors could aid in making informed decisions on intervention methods. In this notebook, initial data exploration using popular Python packages is preformed.

---

## Emphasis

The notebook emphasizes the following skills:
  * Reading in data and creating DataFrames with _Pandas_.
  * Cleaning, relabelling, and organizing data for presentation with _Pandas_ and _NumPy_.
  * Creating and fine-tuning various plots using _Matplotlib_.
  * Representing geographical data through _Plotly_.
  * Inferring and drawing conclusions from data.

---

## Prerequisites

The following interface/ packages are reccomended for proper function:

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

- `ohio_department_of_health__0e4c79bc_1ac0_4c88_a85f_425400be5d0d`
  - Births are classified by the age range of the mother.
  
- `ohio_department_of_health__e870fd77_dee8_4109_b62d_054843fa3bd5`
  - Births are classificed by race and ethnicity. 

County-specific data can be found in the following csv file:

- `ohio_county_data`
  - FIPS codes for Ohio counties - used for plotting county-specific data. 
  
Both Department of Health datasets classify births as either **low birth weight** (<2500g) or **normal birth weight** (2500g+) and are further separated by year and county name.

Further information about the birth data used in this notebook can be found [here](https://discovery.smartcolumbusos.com/?q=health). The use and redistribution of this data is allowable under _Creative Commons Attribution License_ (cc-by). There is no affiliation with the _Ohio Department of Health_.

FIPS codes used in `ohio_county_data` can be found [here](https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697). The use and redistribution of this data is allowable under the _Freedom of Information Act_ (FOIA).There is no affiliation with the _U.S. Department of Agriculture_.

---

## Cloning

Clone this repo to your computer [here](https://github.com/chalvarado96/exploring-ohio-birth-weights/).

---

## Author

- **Chance Alvarado** 
    - [LinkedIn](https://www.linkedin.com/in/chance-alvarado/)
    - [Github](https://github.com/chalvarado96/)

---    

## License

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
