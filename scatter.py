import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

state_dict = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming",
    "DC": "District of Columbia",
}

df = pd.read_excel("Earnings Disparity Race and Ethnicity Data.xlsx")

df = df[df["State"] != "NATIONAL"]

df["State"] = df["State"].map(state_dict)

sns.set_style("whitegrid")

plt.figure(figsize=(20, 10))

colors = sns.color_palette("husl", n_colors=len(df["Data Type"].unique()))
races = df["Data Type"].unique()

for i, race in enumerate(races):
    data = df[df["Data Type"] == race]
    plt.scatter(
        data["State"],
        data["Average Weekly Earnings"],
        label=race,
        alpha=0.6,
        c=[colors[i]],
    )


plt.xticks(rotation=45, ha="right")
plt.xlabel("State")
plt.ylabel("Average Weekly Earnings ($)")
plt.title("Weekly Earnings Distribution by Race Across States")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")


plt.tight_layout()


plt.show()
