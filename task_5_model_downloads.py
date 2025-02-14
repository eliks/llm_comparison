import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
metadata_df = pd.read_csv("data/huggingface_models_data.csv")

# Convert 'Downloads' to numeric and apply log transformation
metadata_df['Downloads'] = np.log(pd.to_numeric(metadata_df['Downloads'], errors='coerce') + 1)

# Create bins and count occurrences
bin_counts, bin_edges = np.histogram(metadata_df["Downloads"], bins=100)

# Convert bin edges to meaningful labels (>1000, >2000, ...)
x_labels = [f">{int(np.exp(edge) - 1):,}" for edge in bin_edges[:-1]]  # Reverse log transformation

# Plot the histogram
plt.figure(figsize=(20, 6))
plt.bar(x_labels[:60], bin_counts[:60], color='skyblue')

# Formatting
plt.xlabel('Downloads Range')
plt.ylabel('Number of Models')
plt.title('Distribution of Models by Downloads')
plt.xticks(rotation=45, ha='right')
plt.grid(True)

# Save the plot
plt.savefig("charts/model_downloads.png", bbox_inches="tight")
# plt.show()
