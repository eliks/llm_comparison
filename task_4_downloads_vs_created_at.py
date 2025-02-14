import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

metadata_df = pd.read_csv("data/huggingface_models_data.csv")

metadata_df['Created At'] = pd.to_datetime(metadata_df['Created At'], errors='coerce')
metadata_df = metadata_df[metadata_df['Downloads'] <= 4000000]
# print(metadata_df['Downloads'].value_counts())
mean_spaces = metadata_df['Downloads'].mean()
min_spaces = metadata_df['Downloads'].min()
max_spaces = metadata_df['Downloads'].max()
count_spaces = metadata_df['Downloads'].count()

print(f"Mean: {mean_spaces}")
print(f"Min: {min_spaces}")
print(f"Max: {max_spaces}")
print(f"Count: {count_spaces}")

metadata_df['Downloads'] = pd.to_numeric(metadata_df['Downloads'], errors='coerce')
metadata_df['Likes'] = pd.to_numeric(metadata_df['Likes'], errors='coerce')

metadata_df = metadata_df.dropna(subset=['Downloads', 'Created At', 'Likes'])

# Plot
plt.figure(figsize=(10, 20))
scatter = sns.scatterplot(
    data=metadata_df, 
    x='Created At', 
    y='Downloads', 
    hue='Likes', 
    palette="viridis", 
    size='Likes',
    sizes=(20, 200),
    alpha=0.7 
)

# Labels and title
plt.xlabel("Created At")
plt.ylabel("Downloads")
plt.title("Downloads vs Created At (Colored by Likes)")
plt.grid(True)

plt.xticks(rotation=45)

# Save plot
plt.savefig("charts/downloads_vs_created_at_colored_by_likes.png", bbox_inches="tight")
plt.show()
