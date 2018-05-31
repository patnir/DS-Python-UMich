import pandas as pd
import numpy as np


def get_energy_df():
    energy = pd.read_excel("Energy Indicators.xls", skiprows=17).iloc[:227]
    energy.columns = ['a', 'b', 'Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy = energy.drop(["a", "b"], 1)

    energy['Energy Supply'] *= 1000000

    energy['Country'] = energy['Country'].str.replace('\d+', '')
    energy['Country'] = energy['Country'].str.replace(' *\(.*\)', '')

    energy.replace(to_replace="United States of America", value='United States', inplace=True)
    energy.replace(to_replace="Republic of Korea", value='South Korea', inplace=True)
    energy.replace(to_replace="United Kingdom of Great Britain and Northern Ireland", value="United Kingdom",
                   inplace=True)
    energy.replace(to_replace="China, Hong Kong Special Administrative Region", value='Hong Kong', inplace=True)
    energy["Energy Supply per Capita"] = energy["Energy Supply per Capita"].replace("...", np.NaN)
    return energy


def get_GDP_df():
    GDP = pd.read_csv("gdp.csv", skiprows=3)
    GDP = GDP.drop(["2016", "2017", "Unnamed: 62"], 1)
    GDP = GDP.fillna(np.NaN)
    GDP.replace(to_replace="Korea, Rep.", value="South Korea", inplace=True)
    GDP.replace(to_replace="Iran, Islamic Rep.", value="Iran", inplace=True)
    GDP.replace(to_replace="Hong Kong SAR, China", value="Hong Kong", inplace=True)
    GDP['Country Name'] = GDP['Country Name'].str.replace('\d+', '')
    GDP['Country Name'] = GDP['Country Name'].str.replace(', .*', '')
    GDP['Country Name'] = GDP['Country Name'].str.replace(' *\(.*\)', '')
    GDP = GDP.rename(columns={'Country Name': 'Country'})
    return GDP


def get_ScimEn_df():
    ScimEn = pd.read_excel("scimagojr.xlsx").iloc[:16]
    # ScimEn = ScimEn.set_index("Rank")
    return ScimEn


energy = get_energy_df()
GDP = get_GDP_df()
ScimEn = get_ScimEn_df()


newdf = pd.merge(energy, ScimEn, how="inner", left_on='Country', right_on='Country')
print(len(energy.iloc[0]))
print(len(ScimEn.iloc[0]))
print(len(newdf.iloc[0]))

newdf2 = pd.merge(newdf, GDP, how="inner", left_on='Country', right_on='Country')

newdf2 = newdf2[["Country", 'Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
newdf2 = newdf2.set_index("Country").sort_values(by=['Rank'], ascending=True)
print(newdf2)

