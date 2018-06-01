import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

df = pd.read_csv("City_Zhvi_AllHomes.csv")
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def get_list_of_university_towns():
    university_towns = pd.read_csv("university_towns.txt", sep="\n", header=None)
    university_towns.columns = ["Names"]
    university_towns["Names"] = university_towns["Names"].str.replace('\[.*\]', '')
    university_towns = university_towns["Names"].str.replace(' *\(.*\)', '')

    university_towns_states = pd.DataFrame(columns=["State", "RegionName"])

    state = university_towns[0]

    for town in university_towns[1:]:
        if town in states.values():
            state = town
        else:
            university_towns_states = university_towns_states.append({"State": state, "RegionName": town},
                                                                     ignore_index=True)

    return university_towns_states


def get_recession_start():
    gdplev = pd.read_excel("gdplev.xlsx", skiprows= 5, parse_cols= [4,5,6])
    gdplev.rename(columns={'Unnamed: 0': 'Quarter'}, inplace=True)
    gdplev = gdplev.drop(gdplev.index[range(0, 214)])
    gdplev = gdplev.set_index(["Quarter"])
    for i in range(2, len(gdplev)):
        prev_name = gdplev.iloc[i-2].name
        curr_year = gdplev.iloc[i][0]
        last_year = gdplev.iloc[i-1][0]
        prev_year = gdplev.iloc[i-2][0]
        if ((prev_year - last_year > 0) and (last_year - curr_year > 0)):
            return prev_name
    return gdplev


def get_recession_end():
    start = get_recession_start()
    gdplev = pd.read_excel("gdplev.xlsx", skiprows=5, parse_cols=[4, 5, 6])
    gdplev.rename(columns={'Unnamed: 0': 'Quarter'}, inplace=True)
    gdplev = gdplev.drop(gdplev.index[range(0, 214)])
    gdplev =  gdplev.reset_index()
    # print(gdplev)
    start_index = gdplev[gdplev['Quarter'] == start].index[0]
    gdplev = gdplev.set_index(["Quarter"])
    gdplev = gdplev.drop(["index"], axis=1)
    for i in range(start_index + 2, len(gdplev) - 1):
        prev_name = gdplev.iloc[i - 2].name
        curr_year = gdplev.iloc[i][0]
        last_year = gdplev.iloc[i - 1][0]
        prev_year = gdplev.iloc[i - 2][0]
        # print(curr_year, last_year, prev_year)
        if (last_year - prev_year > 0) and (curr_year - last_year > 0):
            return prev_name
    return start_index


def get_recession_bottom():
    start = get_recession_start()
    gdplev = pd.read_excel("gdplev.xlsx", skiprows=5, parse_cols=[4, 5, 6])
    gdplev.rename(columns={'Unnamed: 0': 'Quarter'}, inplace=True)
    gdplev = gdplev.drop(gdplev.index[range(0, 214)])
    gdplev =  gdplev.reset_index()
    # print(gdplev)
    start_index = gdplev[gdplev['Quarter'] == start].index[0]
    gdplev = gdplev.set_index(["Quarter"])
    gdplev = gdplev.drop(["index"], axis=1)
    return gdplev["GDP in billions of current dollars"][start_index:].idxmin()


print(get_recession_bottom())