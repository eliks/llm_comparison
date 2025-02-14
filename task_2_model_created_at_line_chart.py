import pandas as pd
import matplotlib.pyplot as plt

metadata_df = pd.read_csv("data/huggingface_models_data.csv")

metadata_df = metadata_df[metadata_df["Created At"] != "Unknown"]

metadata_df["Created At"] = pd.to_datetime(metadata_df["Created At"])

metadata_df = metadata_df.sort_values("Created At")

weekly_counts = metadata_df.groupby(pd.Grouper(key="Created At", freq="W-MON")).size()
# print(weekly_counts)

cumulative_counts = weekly_counts.cumsum()

fig, ax1 = plt.subplots(figsize=(12, 6))

line1, = ax1.plot(weekly_counts.index, weekly_counts.values, marker='o', linestyle='-', 
                   color='tab:blue', markersize=4, label="Weekly Models")
ax1.set_xlabel("Creation Date (Weekly)")
ax1.set_ylabel("Weekly Number of Models", color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create second y-axis for cumulative count
ax2 = ax1.twinx()
line2, = ax2.plot(cumulative_counts.index, cumulative_counts.values, marker='o', linestyle='-', 
                   color='tab:red', markersize=3, label="Cumulative Models")
ax2.set_ylabel("Cumulative Number of Models", color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Mark ChatGPT release date and 6 months later
chatgpt_release = pd.Timestamp("2022-11-30")
four_months_later = pd.Timestamp("2023-05-30")

line3 = ax1.axvline(chatgpt_release, color="black", linestyle="--", linewidth=1, label="ChatGPT Release")
line4 = ax1.axvline(four_months_later, color="gray", linestyle="--", linewidth=1, label="6 Months After ChatGPT Release")

# Title and grid
plt.title("Weekly and Cumulative Number of Models Over Time")
fig.tight_layout()

# Rotate x-axis labels
plt.xticks(rotation=45, ha="right")

# Combine all legends into one and position it at the top-middle
lines = [line1, line2, line3, line4]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper center", bbox_to_anchor=(0.55, 0.9), ncol=2, frameon=True)

plt.savefig("charts/weekly_and_cumulative_models.png", bbox_inches="tight")
# plt.show()
