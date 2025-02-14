import os
import evaluate
import pandas as pd
import torch
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from dotenv import load_dotenv
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset
from huggingface_hub import list_models, model_info, login
from datetime import datetime

os.makedirs("charts", exist_ok=True)

load_dotenv()
login(os.getenv("HF_TOKEN"))

limit = 200000
page = 0

all_models = list_models(filter="text-generation", limit=limit, sort="downloads")

# Data storage
counts_distribution = {}
model_metadata = []
popular_models = []
likes_list = []
creation_years = []
private_counts = {"Public": 0, "Private": 0}
gated_counts = {"Gated": 0, "Non-Gated": 0}
library_counts = {}


for model in all_models:
    try:
        model_details = model_info(model.id)
        # print(model_details.created_at)
        created_at = model_details.created_at if model_details.created_at else "Unknown"

        model_data = {
            "Model ID": model.id,
            "Author": getattr(model_details, "author", "Unknown"),
            "Likes": getattr(model_details, "likes", 0) or 0,
            "Downloads": getattr(model_details, "downloads", 0) or 0,
            "Created At": created_at,
            "Private": getattr(model_details, "private", False),
            "Gated": getattr(model_details, "gated", False),
            "Library": getattr(model_details, "library_name", "Unknown"),
            "Used Storage": getattr(model_details, "usedStorage", 0),
            "Spaces": len(getattr(model_details, "spaces", []))
        }

        model_metadata.append(model_data)
        likes_list.append(model_data["Likes"])
        creation_years.append(created_at)
        private_counts["Private" if model_data["Private"] else "Public"] += 1
        gated_counts["Gated" if model_data["Gated"] else "Non-Gated"] += 1
        library_counts[model_data["Library"]] = library_counts.get(model_data["Library"], 0) + 1

        if model_data["Likes"] > 1000:
            popular_models.append(model.id)

    except Exception as e:
        print(f"Error fetching metadata for {model.id}: {e}")

metadata_df = pd.DataFrame(model_metadata)

metadata_df.to_csv(f"data/huggingface_models_data.csv", index=False)
