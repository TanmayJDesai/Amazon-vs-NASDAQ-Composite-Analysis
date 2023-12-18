import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

class State:
    def __init__(self, name, median_income, demographics):
        self.name = name
        self.median_income = median_income
        self.demographics = demographics

class StateDataset:
    def __init__(self):
        self.states = {}

    def add_state(self, state):
        self.states[state.name] = state

    def get_state_data_frame(self):
        data = {
            'State': [],
            'Median Income': [],
            'Density (per sq.mi)': [],
            'Population (2023)': [],
            'Population (2022)': [],
            'Population (2020)': [],
            'Population (2019)': [],
            'Population (2010)': [],
            'Growth Rate': [],
            'Growth': [],
            'Growth Since 2010': [],
            'Pet Ownership (% of Households)': [],
            'Pet Ownership (% of Dogs)': [],
            'Avg. Num Dogs': [],
            'Pet Ownership (% of Cats)': [],
            'Avg. Num Cats': [],
            'Dog Devotion Score': [],
            'Stayed at Job for Dog (%)': [],
            'Would Spend $4k to Save Dog (%)': [],
        }

        for state_name, state_info in self.states.items():
            data['State'].append(state_info.name)
            data['Median Income'].append(state_info.median_income)
            data['Density (per sq.mi)'].append(state_info.demographics.get('density', None))
            data['Population (2023)'].append(state_info.demographics.get('pop2023', None))
            data['Population (2022)'].append(state_info.demographics.get('pop2022', None))
            data['Population (2020)'].append(state_info.demographics.get('pop2020', None))
            data['Population (2019)'].append(state_info.demographics.get('pop2019', None))
            data['Population (2010)'].append(state_info.demographics.get('pop2010', None))
            data['Growth Rate'].append(state_info.demographics.get('growthRate', None))
            data['Growth'].append(state_info.demographics.get('growth', None))
            data['Growth Since 2010'].append(state_info.demographics.get('growthSince2010', None))
            data['Pet Ownership (% of Households)'].append(state_info.demographics.get('PetOwnershipTotalHouseoldsPerc', None))
            data['Pet Ownership (% of Dogs)'].append(state_info.demographics.get('PetOwnershipDogsPerc', None))
            data['Avg. Num Dogs'].append(state_info.demographics.get('PetOwnershipAvgNumDogs', None))
            data['Pet Ownership (% of Cats)'].append(state_info.demographics.get('PetOwnershipCatsPerc', None))
            data['Avg. Num Cats'].append(state_info.demographics.get('PetOwnershipAvgNumCats', None))
            data['Dog Devotion Score'].append(state_info.demographics.get('PetOwnershipDogDevotionScore', None))
            data['Stayed at Job for Dog (%)'].append(state_info.demographics.get('PetOwnershipStayedAtAJobTheyDislikedForDogPerc', None))
            data['Would Spend $4k to Save Dog (%)'].append(state_info.demographics.get('PetOwnershipWhoWouldSpend4kToSaveDogPerc', None))

        return pd.DataFrame(data)

    def print_average_income_and_pet_stats(self):
        for state_name, state_info in self.states.items():
            avg_income = state_info.median_income
            pet_stats = {
                'Pet Ownership (% of Households)': state_info.demographics.get('PetOwnershipTotalHouseoldsPerc', None),
                'Pet Ownership (% of Dogs)': state_info.demographics.get('PetOwnershipDogsPerc', None),
                'Avg. Num Dogs': state_info.demographics.get('PetOwnershipAvgNumDogs', None),
                'Pet Ownership (% of Cats)': state_info.demographics.get('PetOwnershipCatsPerc', None),
                'Avg. Num Cats': state_info.demographics.get('PetOwnershipAvgNumCats', None),
                'Dog Devotion Score': state_info.demographics.get('PetOwnershipDogDevotionScore', None),
                'Stayed at Job for Dog (%)': state_info.demographics.get('PetOwnershipStayedAtAJobTheyDislikedForDogPerc', None),
                'Would Spend $4k to Save Dog (%)': state_info.demographics.get('PetOwnershipWhoWouldSpend4kToSaveDogPerc', None),
            }

            print(f"\n{state_name}:")
            print(f"Median Income: {avg_income}")
            print("Pet Ownership Statistics:")
            for stat_name, stat_value in pet_stats.items():
                print(f"{stat_name}: {stat_value}")

def get_median_income_by_state():
    url = "https://api.census.gov/data/2019/acs/acs1/profile"
    params = {
        "get": "NAME,DP03_0062E",  # DP03_0062E is the code for median income
        "for": "state:*",
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Extracting data from the response
    states_data = {}
    for entry in data[1:]:
        state_name = entry[0]
        median_income = int(entry[1])
        states_data[state_name] = median_income

    return states_data

# Load pet ownership statistics from CSV file into a dictionary
csv_file_path = "/Users/tanmaydesai/Downloads/pet-ownership-statistics-by-state-2023.csv"
pet_stats_df = pd.read_csv(csv_file_path)
pet_stats_dict = pet_stats_df.set_index('state').to_dict(orient='index')

# Sample dataset
state_dataset = StateDataset()

# Fetch median income data
median_income_data = get_median_income_by_state()

# Populate the StateDataset with data from the CSV file
for state_name, median_income in median_income_data.items():
    if state_name in pet_stats_dict:
        demographics_data = pet_stats_dict[state_name]
        state_dataset.add_state(State(state_name, median_income, demographics_data))

# Analyze the data
state_data_frame = state_dataset.get_state_data_frame()
print(state_data_frame)

# Print average income and pet statistics for each state
state_dataset.print_average_income_and_pet_stats()

map_data = state_dataset.get_state_data_frame()

map_data['Dog Devotion Score'] = pd.to_numeric(map_data['Dog Devotion Score'], errors='coerce')

map_data['Dog Devotion Score'] = pd.to_numeric(map_data['Dog Devotion Score'], errors='coerce')

# Convert 'Dog Devotion Score' to numeric, handling errors
map_data['Dog Devotion Score'] = pd.to_numeric(map_data['Dog Devotion Score'], errors='coerce')

# Convert 'Dog Devotion Score' to numeric, handling errors
map_data['Dog Devotion Score'] = pd.to_numeric(map_data['Dog Devotion Score'], errors='coerce')

# Convert 'Dog Devotion Score' to numeric, handling errors
map_data['Dog Devotion Score'] = pd.to_numeric(map_data['Dog Devotion Score'], errors='coerce')


import plotly.express as px

# Sample class or structure representing state information
class StateInfo:
    def __init__(self, demographics):
        self.demographics = demographics

# Sample data for additional information (replace this with your actual data)
state_infos = {
    "AL": StateInfo({"PetOwnershipTotalHouseoldsPerc": 59.8, "PetOwnershipDogsPerc": 46.9, "PetOwnershipAvgNumDogs": 1.9,
                     "PetOwnershipCatsPerc": 26.1, "PetOwnershipAvgNumCats": 1.7, "PetOwnershipDogDevotionScore": 70.24,
                     "PetOwnershipStayedAtAJobTheyDislikedForDogPerc": 5.5, "PetOwnershipWhoWouldSpend4kToSaveDogPerc": 34}),
    # Add information for other states
}

# Data for dog devotion scores
state_codes = [
    "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "ID", "IL", "IN", "IA", "KS",
    "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
    "VT", "VA", "WA", "WV", "WI", "WY"
]

dog_devotion_scores = [
    70.24, 40.03, 80.97, 66.31, 100, 34.74, 71.15,
    22.05, 92.45, 32.33, 59.82, 32.02, 13.6, 25.68,
    29.46, 43.5, 1.96, 61.18, 65.41, 9.06, 51.21, 42.45,
    8.91, 1.06, 10.12, 87.92, 48.19, 59.21, 54.83, 62.39,
    32.78, 43.2, 32.48, 16.92, 70.69, 0, 68.43, 19.49, 31.27,
    28.85, 81.42, 44.86, 38.07, 94.41, 80.97, 53.47, 59.82, 25.53
]

# Create a dictionary to store data
data = {
    "State": [],
    "Devotion Score": [],
    "PetOwnershipTotalHouseoldsPerc": [],
    "PetOwnershipDogsPerc": [],
    "PetOwnershipAvgNumDogs": [],
    "PetOwnershipCatsPerc": [],
    "PetOwnershipAvgNumCats": [],
    "PetOwnershipDogDevotionScore": [],
    "PetOwnershipStayedAtAJobTheyDislikedForDogPerc": [],
    "PetOwnershipWhoWouldSpend4kToSaveDogPerc": [],
}

# Populate the data dictionary
for state_code in state_codes:
    state_info = state_infos.get(state_code, StateInfo({}))
    data["State"].append(state_code)
    data["Devotion Score"].append(dog_devotion_scores[state_codes.index(state_code)])
    data["PetOwnershipTotalHouseoldsPerc"].append(state_info.demographics.get('PetOwnershipTotalHouseoldsPerc', None))
    data["PetOwnershipDogsPerc"].append(state_info.demographics.get('PetOwnershipDogsPerc', None))
    data["PetOwnershipAvgNumDogs"].append(state_info.demographics.get('PetOwnershipAvgNumDogs', None))
    data["PetOwnershipCatsPerc"].append(state_info.demographics.get('PetOwnershipCatsPerc', None))
    data["PetOwnershipAvgNumCats"].append(state_info.demographics.get('PetOwnershipAvgNumCats', None))
    data["PetOwnershipDogDevotionScore"].append(state_info.demographics.get('PetOwnershipDogDevotionScore', None))
    data["PetOwnershipStayedAtAJobTheyDislikedForDogPerc"].append(state_info.demographics.get('PetOwnershipStayedAtAJobTheyDislikedForDogPerc', None))
    data["PetOwnershipWhoWouldSpend4kToSaveDogPerc"].append(state_info.demographics.get('PetOwnershipWhoWouldSpend4kToSaveDogPerc', None))

# Create DataFrame
df = pd.DataFrame(data)

# Create Choropleth Map with Hover Data
fig = px.choropleth(
    df,
    locations="State",
    locationmode="USA-states",
    color="Devotion Score",
    color_continuous_scale="Viridis",
    range_color=(0, 100),
    scope="usa",
    title="Dog Devotion Scores and Additional Information by State",
    labels={"Devotion Score": "Dog Devotion Score"},
    hover_name="State",
    hover_data={
        "Devotion Score": True,

    }
)

# Show the map
fig.show()

import pandas as pd
import requests
import plotly.graph_objects as go

# Read the CSV file
file_path = '/Users/tanmaydesai/Downloads/pet-ownership-statistics-by-state-2023.csv'
df = pd.read_csv(file_path)

# Function to get median income by state
def get_median_income_by_state():
    url = "https://api.census.gov/data/2019/acs/acs1/profile"
    params = {
        "get": "NAME,DP03_0062E",  # DP03_0062E is the code for median income
        "for": "state:*",
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Extracting data from the response
    states_data = {}
    for entry in data[1:]:
        state_name = entry[0]
        median_income = int(entry[1])
        states_data[state_name] = median_income

    return states_data

# Get median income data
median_income_data = get_median_income_by_state()

# Add a new column for median income to the DataFrame
df['MedianIncome'] = df['state'].map(median_income_data)

# Rename columns for better clarity
column_mapping = {
    'state': 'State',
    'densityMi': 'Density (per sq.mi)',
    'pop2023': 'Population (2023)',
    'pop2022': 'Population (2022)',
    'pop2020': 'Population (2020)',
    'pop2019': 'Population (2019)',
    'pop2010': 'Population (2010)',
    'growthRate': 'Growth Rate',
    'growth': 'Growth',
    'growthSince2010': 'Growth Since 2010',
    'PetOwnershipTotalHouseoldsPerc': 'Pet Ownership (% of Households)',
    'PetOwnershipDogsPerc': 'Pet Ownership (% of Dogs)',
    'PetOwnershipAvgNumDogs': 'Avg. Num Dogs',
    'PetOwnershipCatsPerc': 'Pet Ownership (% of Cats)',
    'PetOwnershipAvgNumCats': 'Avg. Num Cats',
    'PetOwnershipDogDevotionScore': 'Dog Devotion Score',
    'PetOwnershipStayedAtAJobTheyDislikedForDogPerc': 'Stayed at Job for Dog (%)',
    'PetOwnershipWhoWouldSpend4kToSaveDogPerc': 'Would Spend $4k to Save Dog (%)',
    'MedianIncome': 'Median Income'
}

df = df.rename(columns=column_mapping)

# Create a Plotly table
fig = go.Figure(data=[go.Table(
    header=dict(values=df.columns),
    cells=dict(values=df.transpose().values.tolist())
)])

# Show the table
fig.show()

'''
Based on the Dog Devotion Rates, SniffSpot should target (top 5): 
    1. Colorado    --> MI: 77127  --> Devotion: 100
    2. Virginia    --> MI: 76456  --> Devotion: 94.41
    3. Georgia     --> MI: 61980  --> Devotion: 92.45
    4. Nevada      --> MI: 63276  --> Devotion: 87.92
    5. Washington  --> MI: 78687  --> Devotion: 80.97
    
    Washington and Colorado would be the two best locations to target next because of the land density + median income
    + dog devotion rates:
    
    Best locations in these states to target will be: 
        1. Affluent Residential Neighborhoods
        2. Pet-Friendly Communities
        3. Urban and Suburban Areas
        4. Family-Friendly Communities
        5. Dog-Friendly Cities
        6. Parks and Recreation Areas
        7. Areas with Limited Green Spaces
    Best Ways to market in these areas: 
        1. Online Presence:
            Website
            Social Media
        2. Local SEO:
            Optimize Website for Local SEO
            Google My Business Listing
            Encourage Customer Reviews
        3. Community Partnerships:
            Partner with Local Businesses
        4. Hosted Events:
            Organize Public Events
            Distribute Promotional Materials
        5. Influencer Collaborations:
            Partner with Local Pet Influencers
            Sponsored Content, Reviews, Giveaways
        6. Referral Programs:
            Implement Referral Program
        7. Local Advertising:
            Targeted Local Advertising
            Highlight Unique Aspects and Offers
        8. Testimonials and Reviews:
            Encourage Customer Reviews
            Build Trust and Credibility
        9. Exclusive Offers and Discounts:
            Introduce Limited-Time Offers
            Attract First-Time Customers
        10. Educational Content:
            Share Dog Care Tips
            Highlight Benefits of Private Dog Parks
            Provide Local Regulations and Guidelines
        11. Mobile-Friendly Marketing:
            Ensure Mobile-Friendly Materials
        12. Collaborate with Local Authorities:
            Work with Animal Control Offices
            Ensure Regulatory Compliance

'''



