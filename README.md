<p align="center">
  <img src="https://github.com/Chaouabti/TiamaT/blob/main/Dingir.png" alt="TiamaT Logo" width="100"/>
</p>

# 🧠 TiamaT – Toolkit for Integrated Annotation and Machine-learning Assisted Training

*A complete annotation-to-training pipeline designed for modular reusability.*

**TiamaT** is a modular pipeline for image annotation, dataset preparation, training, evaluation, and post-processing using [Label Studio](https://labelstud.io/) and YOLOv8.

> The name is also a nod to [**Tiamat**](https://en.wikipedia.org/wiki/Tiamat), the Mesopotamian goddess of the ocean and chaos — an appropriate symbol for transforming raw, unstructured data into structured, annotated datasets ready for machine learning.

---

## Table of Contents

- [📌 Workflow Overview](#-workflow-overview)
- [⚙️ Installation](#️-installation)
  - [🧱 Label Studio Environment](#-label-studio-environment)
  - [🧠 Tiamat Environment](#-tiamat-environment)
- [📁 Project Folder Structure](#-project-folder-structure)
- [🚀 Usage](#-usage)
  - [📋 Notebook Execution Order](#-notebook-execution-order)
  - [🔄 Iterative Workflow](#-iterative-workflow)
  - [🧾 Shared Variables Across Notebooks](#-shared-variables-across-notebooks)
- [🧰 Requirements](#-requirements)
- [📜 License & Attribution](#-license--attribution)

---

## 📌 Workflow Overview

Each step of the pipeline is handled in a dedicated Jupyter notebook.  
They are numbered to reflect their recommended execution order:

---
### 🐉 `0_Launching_LS.ipynb` – *Start Label Studio (Optional)*

- Launches a local Label Studio server from within Jupyter.
- Allows multi-user configuration by customizing the port (default: 8080).
- Useful if you don't already have Label Studio running elsewhere.

⚠️ Optional, but required if:
- You want to annotate your own data from scratch.
- You need to correct model predictions interactively as part of the iterative loop (steps 5 & 6).

🔗 For manual installation and kernel setup, see the Installation section.

---

### 🐉 `1_Get_training_data.ipynb` – *Extract Annotated Training Data*

- Converts raw annotations from Label Studio (JSON format) into YOLO-compatible training data.
- Extracts only annotated images from the input directory.
- Generates:
  - an `images/` folder with **only** annotated images
  - a `labels/` folder with YOLO-format `.txt` files
  - a `labels.txt` file listing only the **used** annotation classes

📁 Folder names are expected to follow the structure described in the [Project Folder Structure](#project-folder-structure) section.

⚠️ **Do not run** this notebook if you're using corrected files from step 6 (`6_Generate_new_ground_truth.ipynb`).

---

### 🐉 `2_Statistics_for_training_data.ipynb` – *Explore Dataset*

- Computes descriptive statistics to assess the quality and consistency of your dataset.
- Processes image and label files (YOLO format) that share the same filename.
- Helps identify dataset imbalances or label coverage issues.

📌 Requires a `labels.txt` file listing the annotation classes in the following format:
```python
'0': 'class_name0',
'1': 'class_name1',
'2': 'class_name2'
```

---

### 🐉 `3_Data_preparation_and_training.ipynb` – *Data Augmentation & Training*

- Prepares and augments the dataset using image perspective transformations.
- All transformations are applied consistently to both images and their annotations.
- Doubles the dataset with new warped images and adjusted YOLO-format labels.

💬 Augmented files are named using the `_TP` suffix.

📁 Expects a training folder containing:
- `images/` – input images
- `labels/` – YOLO `.txt` annotation files
- `labels.txt` – class mapping file

🟡 You can include unannotated images in training. YOLO will ignore them as long as no `.txt` file is provided.  
See [discussion #7148](https://github.com/ultralytics/yolov5/discussions/7148#discussioncomment-2440612).

---

### 🐉 `4_Predicting_and_checking_YOLO_results.ipynb` – *Inference & Inspection*

- Runs object detection on images using a trained YOLOv8 model.
- Prepares predictions for manual verification and correction.

---

### 🐉 `5_Model_evaluation.ipynb` – *Review & Correct Predictions*

- Imports corrected predictions from Label Studio (CSV format only).
- Reconstructs YOLO-compatible `.txt` annotation files from corrections.
- Enables the creation of a new, improved dataset for retraining.

⚠️ Prerequisites:
- Corrections must be completed in Label Studio.
- Export must be in **CSV format** (YOLO format breaks image name consistency).
- The Labeling Interface must match class names exactly (case-sensitive).
- If Label Studio blocks bbox edits under "predictions", rename them to `"annotations"` as a workaround.

---

### 🐉 `6_Generate_new_ground_truth.ipynb` – *Generate New Ground Truth*

- Converts corrected annotations from Label Studio into a clean YOLO-format dataset.
- Enables new training cycles with improved data quality.
- Uses the original unannotated images, the corrected annotations, and the original `labels.txt` file.

📁 Requires:
- `non_annotated_images/` as input images
- Corrected JSON files in `out/corrections/`
- The original `labels.txt` file from the training session

---

## ⚙️ Installation

TiamaT requires two separate environments:

- One for annotation and project setup using **Label Studio**
- One for training and evaluation using **YOLOv8**

You can install both environments using either **Conda** or **pip + virtualenv**.

---

### 🧱 Label Studio Environment

#### 📦 Using Conda

```bash
# Create the Label Studio environment
conda env create -f LS_environment.yml

# Activate the environment
conda activate label-studio_env

# (Optional) Register the environment as a Jupyter kernel
python -m ipykernel install --user --name=label-studio_env
```

#### Using a Python virtual environment

```bash
# Create and activate the environment
python3 -m venv label-studio_env
source label-studio_env/bin/activate

# Install the requirements
pip install --upgrade pip
pip install -r LS_requirements.txt

# (Optional) Register as Jupyter kernel
python -m ipykernel install --user --name=label-studio_env
```
---
### 🧠 Tiamat Environment

#### 📦 Using Conda

```bash
# Create the YOLO environment
conda env create -f TiamaT_environment.yml

# Activate the environment
conda activate tiamat_env

# (Optional) Register as a Jupyter kernel
python -m ipykernel install --user --name=tiamat_env
```

#### 🐍 Using a Python virtual environment

```bash
# Create and activate the environment
python3 -m venv tiamat_env
source tiamat_env/bin/activate

# Install the requirements
pip install --upgrade pip
pip install -r TiamaT_requirements.txt

# (Optional) Register as a Jupyter kernel
python -m ipykernel install --user --name=tiamat_env
```
---

Once the environments are ready select the appropriate kernel depending on the notebook you're running.

---

### 📁 Project Folder Structure

```
TiamaT/
├── data/                         # Final training datasets
├── environments/                # Virtual environments (e.g., for Label Studio)
│   └── label_studio_env/
├── src/                         # Project source code
│   ├── modules/                 # Custom Python modules
│   └── YOLO_trained/            # Saved YOLO models (optional)
├── partage/                     # Raw and annotated data
│   └── project_name/            # Customizable
│       ├── in/
│       │   ├── non_annotated_images/
│       │   └── annotated_images/
│       └── out/
│           ├── annotations/
│           └── corrections/
└── output/
    └── runs/
        ├── train/
        │   └── model_folder/
        └── predict/
            └── result_folder/
                └── correctedLabels/
```

📌 Only `project_name` can be freely renamed — all other folder names must be preserved for the code to function correctly.

⭐️ All notebooks rely on this layout to locate and process data automatically.

📦 The `src/modules/` folder contains shared utility functions used across notebooks.

🗂️ This structure separates raw data, outputs, and code for better modularity and reproducibility.

---

## 🚀 Usage

TiamaT is organized as a modular notebook pipeline. Each notebook corresponds to a distinct stage in the annotation, training, and evaluation workflow.

### 📋 Notebook Execution Order

1. `0_Launching_LS.ipynb` – *(Optional)* Launch Label Studio locally
2. `1_Get_training_data.ipynb` – Extract annotated images and convert to YOLO format
3. `2_Statistics_for_training_data.ipynb` – Explore the dataset
4. `3_Data_preparation_and_training.ipynb` – Prepare data and train the model
5. `4_Predicting_and_checking_YOLO_results.ipynb` – Run predictions
6. `5_Model_evaluation.ipynb` – Review and extract corrections
7. `6_Generate_new_ground_truth.ipynb` – Generate new training data

### 🐦‍🔥 Iterative Workflow

Below is a visual summary of the TiamaT loop:

```text
        ┌──────────────────────┐
        │ 0. Launch Label Studio│◄────────────┐
        └─────────┬────────────┘             │
                  │                          │
                  ▼                          │
        ┌──────────────────────┐             │
        │1. Extract Training Data│           │
        └─────────┬────────────┘             │
                  ▼                          │
        ┌──────────────────────┐             │
        │2. Dataset Statistics │             │
        └─────────┬────────────┘             │
                  ▼                          │
        ┌──────────────────────┐             │
        │3. Train YOLOv8 Model │             │
        └─────────┬────────────┘             │
                  ▼                          │
        ┌──────────────────────┐             │
        │4. Predict with Model │             │
        └─────────┬────────────┘             │
                  ▼                          │
        ┌──────────────────────┐             │
        │5. Review + Correction│             │
        └─────────┬────────────┘             │
                  ▼                          │
        ┌────────────────────────────┐       │
        │6. Generate New Ground Truth│───────┘
        └────────────────────────────┘

           ⤷ Loop back to step 3 to retrain
```



You can repeat steps 3 to 6 as many times as needed to improve the model’s performance, especially when working with complex or evolving datasets.

📌 You may skip any step if you're starting from partially prepared data or existing corrections.

---

### 🧾 Shared Variables Across Notebooks

The following variables are used consistently across the TiamaT notebooks.  
They define paths, session names, and model references needed throughout the pipeline.

| Variable | Description |
|----------|-------------|
| `YOURNAME` | Name of the Jupyter session |
| `YOURPORT` | Port used to run Label Studio (default is `8080`) |
| `project_folder` | Absolute path to the folder named after your project |
| `data_folder` | Absolute path to the global `data/` directory |
| `training_folder` | Path to the folder where the current training session is stored |
| `pretrained_model` | Path to a YOLO `.pt` file if training starts from a pretrained model |
| `interrupted_model_folder` | Path to an existing model folder to resume interrupted training |
| `img_dataset_folder` | Absolute path to a folder containing images only (no annotations) |
| `yolo_model_folder` | Path to the dataset prepared for training (contains `images/`, `labels/`, and `labels.txt`) |

📌 These variables may be set or redefined in multiple notebooks, depending on the context.  
Make sure to adapt them to your folder structure and data paths before running any notebook.


---

## 🧰 Requirements

- Python 3.10+
- Jupyter Notebook / JupyterLab
- [Label Studio](https://labelstud.io/)
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)

All required dependencies are listed in:

- [`LS_requirements.txt`](./LS_requirements.txt) or [`LS_environment.yml`](./LS_environment.yml)
- [`YOLO_requirements.txt`](./YOLO_requirements.txt) or [`YOLO_environment.yml`](./YOLO_environment.yml)

---

## 📜 License & Attribution

Any use, even partial, of the content in this repository must be accompanied by proper citation.

**Made with ❤️ by [Marion Charpier](https://github.com/Chaouabti/)**  
© 2023–2025 • Project **TiamaT**
