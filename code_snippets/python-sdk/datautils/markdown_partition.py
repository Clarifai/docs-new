from clarifai_datautils.multimodal import Pipeline, MarkdownPartition  
from clarifai.client import Dataset  
import os  

# Set the Clarifai Personal Access Token (PAT) for authentication
os.environ["CLARIFAI_PAT"] = "YOUR_PAT_HERE"

# Define the processing pipeline
pipeline = Pipeline(
    name="pipeline-1",  
    transformations=[        
        MarkdownPartition(chunking_strategy="by_title", max_characters=1024)  
    ]
)

LOCAL_MD_PATH = "YOUR_LOCAL_PDF_PATH_HERE" # Example: "./assets/multimodal/DA-1p.md"

# Initialize dataset object for ingesting data
dataset = Dataset(user_id="YOUR_USER_ID_HERE", app_id="YOUR_APP_ID_HERE", dataset_id="YOUR_DATASET_ID_HERE")

# Alternative: Initialize the dataset using a dataset URL (commented out)
# dataset = Dataset("DATASET_URL_HERE")

# Use Python SDK to upload the processed text chunks to Clarifai
dataset.upload_dataset(pipeline.run(files=LOCAL_MD_PATH, loader=True))
