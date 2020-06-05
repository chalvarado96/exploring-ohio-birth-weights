# -*- coding: utf-8 -*-
"""Defining functions and classes for analysis on Ohio birth weights.

The contents of this module define functions and classes for data cleaning
and visualization of Ohio Health Department data on low birth weights in
Ohio from 2006-2017.

Explore this repository at:
    https://github.com/chance-alvarado/exploring-ohio-birth-weights

Author:
    Chance Alvarado
        LinkedIn: https://www.linkedin.com/in/chance-alvarado/
        Github: https://github.com/chance-alvarado/
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff


class _Themes():
    """Document-wide color themes."""

    background_color = '#e4ecf7'

    normal_color = '#B3E9FF'
    low_color = '#2A037D'
    color_list = [low_color, normal_color]

    low_colorscale = ['#B3E9FF', '#A5D2F2', '#97BBE5',
                      '#89A4D8', '#7C8DCB', '#6E76BE',
                      '#605FB2', '#5348A4', '#453197',
                      '#371A8A', '#2A037D'
                      ]

    race_colorscale = ['#B3E9FF', '#ef331a', '#14ee11',
                       '#11eed5', '#d7f132', '#2A037D'
                       ]


class _Lists():
    """Relevant lists necessary for plot creation."""

    # List of all years from 2006-2017.
    all_years = list(range(2006, 2018))

    # List of all age ranges represented in data.
    all_ages = ['Less than 15', '15 to 17', '18 to 19', '20 to 24',
                '25 to 29', '30 to 34', '35 to 39', '40 to 44',
                '45 and older', 'Unknown']

    # List of all races represented in data.
    all_races = ['White', 'African American', 'Asian', 'Native American',
                 'Pacific Islander', 'Unknown'
                 ]


def age_data_cleaning(age_path):
    """Clean and relabel birth data based on mother's age."""
    # Read in CSV.
    age_df = pd.read_csv(age_path, na_values='*', engine='python')

    # Fill na values with 0.
    age_df.fillna(value=0, inplace=True)

    # Drop default sort column.
    age_df.drop(labels='sort', axis=1, inplace=True)

    # Rename columns for ease of access.
    age_df.rename(columns={'age group desc': 'age',
                           'birth count': 'birth_count',
                           'birth count_pct': 'birth_percentage',
                           'county name': 'county',
                           'low birth weight ind desc': 'weight_indicator',
                           'year desc': 'year'
                           },
                  inplace=True
                  )

    # Rename specific values for ease of access.
    age_df.replace(to_replace=['2017 **', 'Low birth weight (<2500g)',
                               'Normal birth weight (2500g+)'
                               ],
                   value=[2017, 'low', 'normal'],
                   inplace=True
                   )

    # Clear irrelevant rows.
    age_df = age_df[age_df.weight_indicator != 'Total']
    age_df = age_df[age_df.year != 'Total']
    age_df = age_df[age_df.county != 'Unknown']
    age_df = age_df[age_df.county != 'NonOH']

    # Convert years to numbers for ease of access.
    age_df.year = pd.to_numeric(age_df.year)

    return age_df


def race_data_cleaning(race_ethnicity_path):
    """Clean and relabel birth data based on race/ ethnicity."""
    # Read in CSV.
    race_df = pd.read_csv(race_ethnicity_path, na_values='*', engine='python')

    # Fill na values with 0.
    race_df.fillna(value=0, inplace=True)

    # Drop default sort column.
    race_df.drop(labels='sort', axis=1, inplace=True)

    # Rename columns for ease of access.
    race_df.rename(columns={'birth count': 'birth_count',
                            'birth count_pct': 'birth_percentage',
                            'county name': 'county',
                            'ethnicity desc': 'ethnicity',
                            'low birth weight ind desc': 'weight_indicator',
                            'race catg desc': 'race',
                            'year desc': 'year'
                            },
                   inplace=True
                   )

    # Rename specific values for ease of access.
    race_df.replace(to_replace=['2017 **',
                                'Low birth weight (<2500g)',
                                'Normal birth weight (2500g+)',
                                'African American  (Black)',
                                'Pacific Islander/Hawaiian',
                                'Unknown/Not Reported'
                                ],
                    value=[2017, 'low', 'normal',
                           'African American', 'Pacific Islander',
                           'Unknown'
                           ],
                    inplace=True
                    )

    # Clear irrelevant rows.
    race_df = race_df[race_df.weight_indicator != 'Total']
    race_df = race_df[race_df.year != 'Total']

    # Convert years to numbers for ease of access.
    race_df.year = pd.to_numeric(race_df.year)

    return race_df


def county_data_cleaning(county_path):
    """Clean and relabel county data."""
    county_df = pd.read_csv(county_path, index_col='county')

    return county_df


def age_pivot_table(age_df):
    """Construct example pivot table for mother's age data."""
    # Group by heiarchical sorting.
    age_pivot_ser = age_df.groupby(by=['year', 'county', 'age',
                                       'weight_indicator'
                                       ]
                                   ).birth_count.sum()

    # Unstack Series to create DataFrame.
    age_pivot_df = age_pivot_ser.unstack()

    return age_pivot_df


def race_pivot_table(race_df):
    """Construct example pivot table for race/ ethnicity data."""
    # Group by heiarchical sorting.
    race_pivot_ser = race_df.groupby(by=['year', 'county', 'race',
                                         'ethnicity', 'weight_indicator'
                                         ]
                                     ).birth_count.sum()

    # Unstack Series to create DataFrame.
    race_pivot_df = race_pivot_ser.unstack()

    return race_pivot_df

    # Unstack Series to create DataFrame.
    race_pivot_df = race_pivot_ser.unstack()

    return race_pivot_df


def total_age_bar(age_df):
    """Bar graph of birth weights per age range relative to total births."""
    # Group births by age.
    age_ser = age_df.groupby(by=['age', 'weight_indicator']).birth_count.sum()
    age_sort_df = age_ser.unstack()

    # Reindex for readability.
    age_sort_df = age_sort_df.reindex(_Lists.all_ages)

    # Plot creation.
    ax = age_sort_df.plot.bar(title='Birth Weight Relative to Age of Mother',
                              fontsize=12, color=_Themes.color_list, rot=45
                              )

    # Plot enhancement.
    ax.title.set_size(14)
    ax.grid(color='k', alpha=0.05)
    ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    ax.set_yticks(np.linspace(0, max(age_sort_df.normal), 10))
    ax.set_xlabel('Age of Mother', fontsize=12)
    ax.set_ylabel('Births (in 100,000s)', fontsize=12)

    # Show plot.
    plt.show()


def relative_age_bar(age_df):
    """Bar graph of birth weights relative to total births per age range."""
    # Group births by age.
    age_ser = age_df.groupby(by=['age', 'weight_indicator']).birth_count.sum()
    age_sort_df = age_ser.unstack()

    # Reindex for readability.
    age_sort_df = age_sort_df.reindex(_Lists.all_ages)

    # Reformat so numbers are relative to total births in that category.
    total_births = (age_sort_df.low + age_sort_df.normal)
    age_sort_df.low = age_sort_df.low / total_births
    age_sort_df.normal = age_sort_df.normal / total_births

    # Plot creation.
    ax = age_sort_df.plot.bar(stacked=True,
                              title='Birth Weight Relative to Age of Mother',
                              fontsize=12, color=_Themes.color_list, rot=45
                              )

    # Plot enhancement.
    ax.title.set_size(14)
    ax.grid(color='k', alpha=0.05)
    ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    ax.set_yticks(np.linspace(0, 1, 11))
    ax.set_xlabel('Age of Mother', fontsize=12)
    ax.set_ylabel('Fraction of Total Births in Age Range', fontsize=12)

    # Show plot.
    plt.show()


def total_race_bar(race_df):
    """Bar graph of birth weights per race relative to total births."""
    # Group births by race.
    race_ser = race_df.groupby(by=['race', 'weight_indicator']
                               ).birth_count.sum()
    race_sort_df = race_ser.unstack()

    # Reindex for readability.
    race_sort_df = race_sort_df.reindex(_Lists.all_races[::-1])

    # Plot creation.
    ax = race_sort_df.plot.barh(title='Birth Weight Relative to Race',
                                fontsize=12, color=_Themes.color_list, rot=45
                                )

    # Plot enhancement.
    ax.title.set_size(14)
    ax.grid(color='k', alpha=0.05)
    ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
    ax.set_xlabel('Births (in 100,000s)', fontsize=12)
    ax.set_ylabel('Race', fontsize=12)
    ax.legend(loc='lower right')

    # Show plot.
    plt.show()


def relative_race_bar(race_df):
    """Bar graph of birth weights relative to total births per race."""
    # Group births by race.
    race_ser = race_df.groupby(by=['race', 'weight_indicator']
                               ).birth_count.sum()
    race_sort_df = race_ser.unstack()

    # Reindex for readability.
    all_races_2 = _Lists.all_races.copy()
    all_races_2.append(all_races_2.pop(-2))
    race_sort_df = race_sort_df.reindex(all_races_2[::-1])

    # Reformat so numbers are relative to total births in that category.
    total_births = race_sort_df.low + race_sort_df.normal
    race_sort_df.low = race_sort_df.low / total_births
    race_sort_df.normal = race_sort_df.normal / total_births

    # Plot creation.
    ax = race_sort_df.plot.barh(stacked=True,
                                title='Birth Weight Relative to Race',
                                color=_Themes.color_list, rot=45
                                )

    # Plot enhancement.
    ax.title.set_size(14)
    ax.grid(color='k', alpha=0.05)
    ax.set_xticks(np.linspace(0, 1, 11))
    ax.set_xlabel('Fraction of Total Births per Race', fontsize=12)
    ax.set_ylabel('Race', fontsize=12)
    ax.legend(loc='lower right')

    # Show plot.
    plt.show()


def ethnicity_pie(race_df):
    """Pie chart of relative number of low birth weights by ethnicity."""
    # Group births by ethnicity.
    race_ser = race_df.groupby(by=['ethnicity', 'weight_indicator']
                               ).birth_count.sum()
    race_sort_df = race_ser.unstack()

    # Plot creation.
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
    fig.suptitle('Percentage of Low Birth Weights per Ethnicity', fontsize=16)

    axs[0].pie(race_sort_df.loc['Hispanic'].tolist(),
               colors=_Themes.color_list, explode=(0, 0.25),
               shadow=True, autopct='%1.1f%%', pctdistance=1.25,
               )

    ttl_0 = axs[0].set_title('Hispanic', fontsize=14)
    ttl_0.set_position([.45, .95])

    axs[1].pie(race_sort_df.loc['Non-Hispanic'].tolist(),
               colors=_Themes.color_list, explode=(0, 0.25),
               shadow=True, autopct='%1.1f%%', pctdistance=1.25
               )

    ttl_1 = axs[1].set_title('Non-Hispanic', fontsize=14)
    ttl_1.set_position([.45, .95])

    axs[1].legend(['low ', 'normal'], loc=4)

    # Show plot.
    plt.show()


def county_breakdown_plot(age_df, county_df):
    """Geographical plot of county average of low birth weights."""
    # County FIPS codes.
    county_fips = county_df.FIPS.tolist()

    # Sort birth weights by county.
    age_sort_df = age_df.groupby(by=['county', 'weight_indicator']
                                 ).birth_count.sum()
    age_sort_df = age_sort_df.unstack()

    # Reformat so numbers are relative to total births in that category.
    total_births = age_sort_df.low + age_sort_df.normal
    age_sort_df.low = age_sort_df.low / total_births
    age_sort_df.normal = age_sort_df.normal / total_births

    # Convert to percent out of 100.
    percent_low = [val * 100 for val in age_sort_df.low.tolist()]

    # Create bins.
    low_bins = list(range(5, 55, 5))

    # Plot creation.
    fig = ff.create_choropleth(fips=county_fips, values=percent_low,
                               scope=['OH'], binning_endpoints=low_bins,
                               colorscale=_Themes.low_colorscale,
                               legend_title='% of county births', asp=3,
                               show_hover=True, width=800, height=400,
                               county_outline={'color': 'rgb(255,255,255)',
                                               'width': 0.5
                                               }
                               )

    # Plot enhancement.
    fig.update_layout(title={'text': 'Ohio Low Birth Weights by County',
                             'y': .96, 'x': 0.5, 'xanchor': 'center',
                             'yanchor': 'top'
                             }
                      )
    fig.layout.plot_bgcolor = '#FFFFFF'

    # Show plot.
    fig.show()


def annual_low_births_line(age_df):
    """Line plot of annual low birth weights."""
    # Group data by year.
    age_ser = age_df.groupby(by=['year', 'weight_indicator']
                             ).birth_count.sum()
    age_sort_df = age_ser.unstack()

    # Reformat so numbers are relative to total births in that category.
    total_births = age_sort_df.low + age_sort_df.normal
    age_sort_df.low = age_sort_df.low / total_births
    age_sort_df.normal = age_sort_df.normal / total_births

    # Plot creation.
    ax = age_sort_df.low.plot(title='Percentage of Low Birth Weights per Year',
                              fontsize=12, rot=45, linewidth='5',
                              linestyle='--', color=_Themes.low_color,
                              )
    # Plot enhancement.
    ax.title.set_size(14)
    ax.set_yticks([round(val, 2) for val in np.linspace(0.1, 0.18, 9)])
    ax.set_xticks(_Lists.all_years)
    ax.set_ylabel('Fraction of Annual Births', fontsize=12)
    ax.set_xlabel('Year', fontsize=12)
    ax.grid(color='k', alpha=0.05)
    ax.margins(x=0)

    # Show plot.
    plt.show()


def high_risk_ages_stacked(age_df):
    """Stacked bar plot of annual change in births for high-risk mothers."""
    # Group data by year and age range.
    age_ser = age_df.groupby(by=['year', 'age', 'weight_indicator']
                             ).birth_count.sum()
    age_sort_df = age_ser.unstack()

    # Data list construction for plotting.
    teen_low = []
    teen_normal = []
    teen_total = []

    older_low = []
    older_normal = []
    older_total = []

    # Populate lists.
    for year in _Lists.all_years:
        teen_ser = age_sort_df.loc[year].loc['15 to 17'] \
                 + age_sort_df.loc[year].loc['Less than 15']

        older_ser = age_sort_df.loc[year].loc['45 and older']

        teen_low.append(teen_ser.low)
        teen_normal.append(teen_ser.normal)
        teen_total.append(teen_ser.low + teen_ser.normal)

        older_low.append(older_ser.low)
        older_normal.append(older_ser.normal)
        older_total.append(older_ser.low + older_ser.normal)

    # Plot creation
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
    fig.suptitle('Annual Change in Births from High Risk Age Groups',
                 fontsize=16
                 )
    fig.subplots_adjust(top=0.85)

    axs[0].stackplot(_Lists.all_years, [teen_low, teen_normal],
                     colors=_Themes.color_list
                     )

    axs[1].stackplot(_Lists.all_years, [older_low, older_normal],
                     colors=_Themes.color_list)

    # Plot enhancement.
    axs[0].set_title('Teen Births', fontsize=14)
    axs[1].set_title('Older Births', fontsize=14)
    axs[1].legend(['low', 'normal'])

    for i in (0, 1):
        axs[i].set_xticks(_Lists.all_years)
        axs[i].set_xticklabels(_Lists.all_years, rotation=45)
        axs[i].set_xlabel('Year', fontsize=12)
        axs[i].set_ylabel('Births', fontsize=12)
        axs[i].grid(color='k', alpha=0.05)
        axs[i].margins(x=0)

    # Show plot.
    plt.show()


def race_breakdown_plot_stacked(race_df):
    """Stacked bar plot of annual change in race breakdown for all births."""
    # Group data by year and race.
    race_ser = race_df.groupby(by=['year', 'race', 'weight_indicator']
                               ).birth_count.sum()
    race_sort_df = race_ser.unstack()

    # Create total column for each race.
    race_sort_df['total'] = race_sort_df.low + race_sort_df.normal

    # Data list construction for plotting.
    asian_total = []
    african_american_total = []
    native_american_total = []
    pacific_islander_total = []
    white_total = []
    unknown_total = []

    # Populate lists.
    for year in _Lists.all_years:
        asian_total.append(race_sort_df.loc[year].loc['Asian']['total'])
        african_american_total.append(race_sort_df.loc[year]
                                      .loc['African American']['total'])
        native_american_total.append(race_sort_df.loc[year]
                                     .loc['Native American']['total'])
        pacific_islander_total.append(race_sort_df.loc[year]
                                      .loc['Pacific Islander']['total'])
        white_total.append(race_sort_df.loc[year]
                           .loc['White']['total'])
        unknown_total.append(race_sort_df.loc[year]
                             .loc['Unknown']['total'])

    # Plot creation.
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.stackplot(_Lists.all_years, [white_total, african_american_total,
                                    asian_total, native_american_total,
                                    pacific_islander_total, unknown_total,
                                    ],
                 colors=_Themes.race_colorscale,
                 alpha=0.9
                 )

    # Plot enhancement.
    ax.set_title('Change in Race of all Births', fontsize=14)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_xticks(_Lists.all_years)
    ax.set_xticklabels(_Lists.all_years, rotation=45)
    ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    ax.set_ylabel('Births (in 10,000s)', fontsize=12)
    ax.grid(color='k', alpha=0.05)
    ax.legend(_Lists.all_races, loc=4)

    ax.margins(x=0)

    # Show plot.
    plt.show()
