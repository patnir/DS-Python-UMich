import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

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


def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe s‰hould have 67 columns, and 10,730 rows.
    '''

    df = pd.read_csv("City_Zhvi_AllHomes.csv")
    ndf = df[["State","RegionName"]]
    quarter = 0
    for col in range(53, 6 + len(df.columns[6:]), 3):
        quarter_name = df.columns[col][:4] + "q" + str((quarter % 4) + 1)
        quarter += 1

        ndf[quarter_name] = df[df.columns[col]] + df[df.columns[col - 1]] + df[df.columns[col - 2]]
    colsToDrop = range(70, len(ndf.columns))
    print(ndf.columns[colsToDrop])
    ndf = ndf.drop(ndf.columns[colsToDrop].tolist(), axis=1)
    ndf = ndf.set_index(["State","RegionName"])
    return ndf


def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values,
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence.

    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''

    unitowns = get_list_of_university_towns()
    bottom = get_recession_bottom()
    start = get_recession_start()
    hdata = convert_housing_data_to_quarters()
    bstart = hdata.columns[hdata.columns.get_loc(start) - 1]

    hdata['ratio'] = hdata[bstart] - hdata[bottom]
    hdata = hdata[[bottom, bstart, 'ratio']]
    hdata = hdata.reset_index()

    unitowns_hdata = pd.merge(hdata, unitowns, how='inner', on=['State', 'RegionName'])
    unitowns_hdata['uni'] = True
    hdata2 = pd.merge(hdata, unitowns_hdata, how='outer', on=['State', 'RegionName', bottom, bstart, 'ratio'])
    hdata2['uni'] = hdata2['uni'].fillna(False)

    ut = hdata2[hdata2['uni'] == True]
    nut = hdata2[hdata2['uni'] == False]

    t, p = ttest_ind(ut['ratio'].dropna(), nut['ratio'].dropna())

    different = True if p < 0.01 else False
    better = "university town" if ut['ratio'].mean() < nut['ratio'].mean() else "non-university town"

    return different, p, better


print(run_ttest())
