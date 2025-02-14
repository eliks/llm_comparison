# **Exploring Trends in Text-Generation Models on HuggingFace**  

This project investigates the evolution and adoption of text-generation models available on [Hugging Face](https://huggingface.co/). By analyzing model metadata, we uncover key trends related to model creation, storage usage, popularity, and adoption over time, particularly before and after the release of ChatGPT.  

## **Project Overview**  

With the growing interest in large language models, this study aims to explore how text-generation models have evolved in terms of quantity, usage, and popularity. Using the Hugging Face API, we collected data on over **183,000 models**, filtering for relevant metadata such as **downloads, likes, storage size, and creation date**.  

## **Methodology**  

The analysis was divided into five key tasks:  

1. **Data Collection:**  
   - The Hugging Face API was used to fetch text-generation models.  
   - Data was saved as a CSV file (`data/huggingface_models_data.csv`).  

2. **Model Creation Trends:**  
   - A time-series analysis of models created weekly and cumulatively.  
   - Visualized in `charts/weekly_and_cumulative_models.png`.  

3. **Storage vs. Spaces (Colored by Likes):**  
   - Relationship between model storage size and number of Hugging Face Spaces.  
   - Outliers were filtered for better visualization.  
   - Chart saved as `charts/used_storage_vs_spaces_colored_by_likes.png`.  

4. **Downloads vs. Created At (Colored by Likes):**  
   - Analyzed how model downloads evolved over time.  
   - Chart saved as `charts/downloads_vs_created_at_colored_by_likes.png`.  

5. **Distribution of Models by Downloads:**  
   - Categorized models based on popularity using download counts.  
   - Chart saved as `charts/model_downloads.png`.  

## **Results & Insights**  

- Model creation increased steadily but saw a **sharp rise six months after ChatGPT’s launch**.  
- Smaller models are **more popular** in terms of usage and engagement.  
- **Recent models receive more downloads** compared to earlier models.  
- Models can be categorized into **Not Popular (<40 downloads), Popular (40–999), and Very Popular (≥1000)**.  

## **How to Use**  

### **1. Install Dependencies**  

Ensure you have `virtualenv` installed for environment management. To install required packages:  

```bash
pip install -r requirements.txt
```

### **2. Run the Analysis**  

Each task is implemented in a separate script:  

```bash
python task_1_fetch_and_store_models_data.py  
python task_2_model_created_at_line_chart.py  
python task_3_used_storage_vs_spaces.py  
python task_4_downloads_vs_created_at.py  
python task_5_model_downloads.py  
```

## **Data & Code Availability**  

- **Data:** The dataset used in this study is periodically updated and will be available on **GitHub**.  
- **Code:** All scripts used for data collection and visualization are included in this repository.  

## **Contact**  

For questions or contributions, feel free to reach out via GitHub issues.  