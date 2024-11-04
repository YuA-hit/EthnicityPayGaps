import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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


races = df["Data Type"].unique()


colors = sns.color_palette("husl", n_colors=len(races))


for i, race in enumerate(races):

    plt.figure(figsize=(15, 8))

    data = df[df["Data Type"] == race]

    data = data.sort_values("Average Weekly Earnings", ascending=False)

    plt.scatter(
        data["State"],
        data["Average Weekly Earnings"],
        alpha=0.6,
        c=[colors[i]],
        label=race,
        s=100,
    )

    mean_earnings = data["Average Weekly Earnings"].mean()
    plt.axhline(
        y=mean_earnings,
        color="red",
        linestyle="--",
        alpha=0.5,
        label=f"Mean: ${mean_earnings:.2f}",
    )

    stats_text = f"Statistical Summary:\n"
    stats_text += f"Mean: ${mean_earnings:.2f}\n"
    stats_text += f"Max: ${data['Average Weekly Earnings'].max():.2f}\n"
    stats_text += f"Min: ${data['Average Weekly Earnings'].min():.2f}\n"
    stats_text += f"Std: ${data['Average Weekly Earnings'].std():.2f}\n"
    stats_text += f"Top 3 States:\n"

    top_3 = data.nlargest(3, "Average Weekly Earnings")
    for _, row in top_3.iterrows():
        stats_text += f"  {row['State']}: ${row['Average Weekly Earnings']:.2f}\n"

    plt.text(
        0.02,
        0.02,
        stats_text,
        transform=plt.gca().transAxes,
        verticalalignment="bottom",
        horizontalalignment="left",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
    )

    plt.title(f"{race} Weekly Earnings by State", fontsize=14, pad=20)
    plt.xlabel("State", fontsize=12)
    plt.ylabel("Weekly Earnings ($)", fontsize=12)

    plt.ylim(300, 1700)

    plt.xticks(rotation=45, ha="right")

    plt.yticks(np.arange(300, 1701, 100))

    plt.grid(True, linestyle="--", alpha=0.7)

    plt.legend()

    plt.tight_layout()


plt.show()


print("\n詳細な統計分析:")
for race in races:
    data = df[df["Data Type"] == race]
    print(f"\n{race}の分析:")
    print(f"平均給与: ${data['Average Weekly Earnings'].mean():.2f}")
    print(
        f"最高給与州: {data.loc[data['Average Weekly Earnings'].idxmax(), 'State']}"
        + f" (${data['Average Weekly Earnings'].max():.2f})"
    )
    print(
        f"最低給与州: {data.loc[data['Average Weekly Earnings'].idxmin(), 'State']}"
        + f" (${data['Average Weekly Earnings'].min():.2f})"
    )
    print(
        f"州間の給与格差: ${data['Average Weekly Earnings'].max() - data['Average Weekly Earnings'].min():.2f}"
    )
    print(f"給与の標準偏差: ${data['Average Weekly Earnings'].std():.2f}")
    print(f"州の数: {len(data)}")
