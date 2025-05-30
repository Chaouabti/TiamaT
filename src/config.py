# Configuration file

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Project info ---
PROJECT_NAME = os.getenv("PROJECT_NAME", "project")
LS_PORT = int(os.getenv("LS_PORT", 8080))

# --- Folder paths ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

PROJECT_DIR = os.path.join(BASE_DIR, PROJECT_NAME)
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# --- Training-specific folders ---
TRAINING_FOLDER = os.path.join(DATA_DIR, PROJECT_NAME)

IMG_DATASET_FOLDER = os.getenv("img_dataset_folder", os.path.join(PROJECT_DIR, "image_inputs", "ground_truth_images"))
MODEL_FOLDER = os.getenv("model_folder", os.path.join(OUTPUT_DIR, "runs", "train", "MODEL_NAME"))
PRETRAINED_MODEL = os.getenv("pretrained_model", os.path.join(MODEL_FOLDER, "weights", "best.pt"))
INTERRUPED_MODEL = os.getenv("interrupted_model_folder", os.path.join(MODEL_FOLDER, "weights", "last.pt"))

# --- Utility: display config if needed ---
def show_config():
    print(f"PROJECT_NAME: {PROJECT_NAME}")
    print(f"PROJECT_DIR: {PROJECT_DIR}")
    print(f"DATA_DIR: {DATA_DIR}")
    print(f"OUTPUT_DIR: {OUTPUT_DIR}")
    print(f"TRAINING_FOLDER: {TRAINING_FOLDER}")
    print(f"IMG_DATASET_FOLDER: {IMG_DATASET_FOLDER}")
    print(f"MODEL_FOLDER: {MODEL_FOLDER}")
    print(f"PRETRAINED_MODEL: {PRETRAINED_MODEL}")


if __name__ == "__main__":
    show_config()
