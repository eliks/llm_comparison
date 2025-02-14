import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

metadata_df = pd.read_csv("data/huggingface_models_data.csv")

metadata_df['Used Storage'] = pd.to_numeric(metadata_df['Used Storage'], errors='coerce')
metadata_df['Spaces'] = pd.to_numeric(metadata_df['Spaces'], errors='coerce')
metadata_df['Likes'] = pd.to_numeric(metadata_df['Likes'], errors='coerce')

metadata_df = metadata_df.dropna(subset=['Used Storage', 'Spaces', 'Likes'])

# Plot
plt.figure(figsize=(14, 6))
scatter = sns.scatterplot(
    data=metadata_df, 
    x='Used Storage', 
    y='Spaces', 
    hue='Likes', 
    palette="viridis", 
    size='Likes',
    sizes=(20, 200),
    alpha=0.7 
)

norm = plt.Normalize(metadata_df['Likes'].min(), metadata_df['Likes'].max())
sm = plt.cm.ScalarMappable(cmap="viridis", norm=norm)
sm.set_array([])

cbar = plt.colorbar(sm, ax=plt.gca(), label="Likes")

plt.xlabel("Used Storage (Bites)")
plt.ylabel("Spaces")
plt.title("Used Storage vs. Spaces (Colored by Likes)")
plt.grid(True)

plt.savefig("charts/used_storage_vs_spaces_colored_by_likes.png", bbox_inches="tight")
# plt.show()

