# 📚 TiamaT – Pipeline Overview (Notebooks & Scripts)

This document provides a step-by-step overview of the TiamaT pipeline.  
Each stage can be run either as a Jupyter notebook (for interactive workflows) or as a standalone script (for automation and batch runs).  
The notebook and script versions are functionally equivalent.

---

## 🐉 Stage 0 – Launch Label Studio *(Optional)*

- 📓 **Notebook**: `0_Launching_LS.ipynb`  
- 💬 **Alternative**: run `label-studio` directly from the command line

This notebook is primarily intended for JupyterHub environments, where launching Label Studio from within a controlled kernel (with custom port and environment) is convenient.

### ✅ What it does
- Starts a local Label Studio instance (default port: 8080)
- Enables interactive annotation from the same Jupyter session

### ⚠️ When to use
- When working in a JupyterHub-based setup
- When you want to annotate or correct directly from within the notebook

### 🖥️ Command-line alternative
If you're not using the notebook, you can simply run:

```bash
label-studio
```

> ![WARNING]
> Make sure your virtual environment is activated before running the command.

---

## 🐉 Stage 1 – Extract Annotated Training Data

- 📓 **Notebook**: `1_Get_training_data.ipynb`  
- ⚙️ **Script**: `extract_training_data.py`

Converts manual annotations from Label Studio into a YOLO-compatible dataset.

### ✅ What it does
- Parses JSON annotations exported from Label Studio
- Extracts only annotated images
- Generates:
  - `images/` with annotated images
  - `labels/` with YOLO-format `.txt` files
  - `labels.txt` listing used annotation classes

### ⚠️ Notes
- Do **not** run this if you're using corrected predictions (see Stage 6)

---

## 🐉 Stage 2 – Dataset Statistics

- 📓 **Notebook**: `2_Statistics_for_training_data.ipynb`  
- ⚙️ **Script**: `analyze_dataset.py`

Explores your training dataset to identify imbalances or inconsistencies.

### ✅ What it does
- Computes per-class counts, image coverage, and label distributions
- Verifies alignment between `images/` and `labels/`

### 📌 Requires

- A valid `labels.txt` in the format:

```python
'0': 'class_name0',
'1': 'class_name1',
'2': 'class_name2'
```
---

## 🐉 Stage 3 – Data Augmentation & Training

- 📓 **Notebook**: `3_Data_preparation_and_training.ipynb`
- ⚙️ **Script**: `train_model.py`

Prepares and augments the dataset, then trains a YOLO model.

### ✅ What it does

- Applies geometric transformations (perspective warping)
- Augmented files use the `_TP` suffix
- Trains a YOLO model using Ultralytics CLI or programmatic API

### 📁 Expects

- `images/`, `labels/`, and `labels.txt` in a training folder

### 🟡 Note

- You may include unannotated images — YOLO will ignore them automatically

---

## 🐉 Stage 4 – Predict on Evaluation Images

- 📓 **Notebook**: `4_Predicting_and_checking_YOLO_results.ipynb`
- ⚙️ **Script**: `predict.py`

Uses a trained YOLO model to infer objects on new images.

### ✅ What it does

- Runs predictions on `eval_images/`
- Saves YOLO-format predictions in a dedicated output folder
- Prepares files for manual review and correction in Label Studio

---

## 🐉 Stage 5 – Evaluate Model & Review Corrections

- 📓 **Notebook**: `5_Model_evaluation.ipynb`
- ⚙️ **Script**: `evaluate_model.py`

Imports manually corrected predictions and reconstructs YOLO labels.

### ✅ What it does

- Converts corrected CSV annotations from Label Studio back into YOLO format
- Enables model evaluation via human feedback
- Optionally merges with previous training data for retraining

### ⚠️ Requirements

- Corrections must be exported in CSV format
- Label names must match exactly (case-sensitive)
- If bounding box edits are blocked in LS, change `"predictions"` → `"annotations"`

---

## 🐉 Stage 6 – Generate New Ground Truth

- 📓 **Notebook**: `6_Generate_new_ground_truth.ipynb`
- ⚙️ **Script**: `generate_ground_truth.py`

Generates a clean new training dataset from corrected annotations.

### ✅ What it does

- Extracts corrected bounding boxes from Label Studio exports
- Matches them to original, unannotated images
- Produces a complete YOLO dataset (`images` + `labels` + `labels.txt`)

### 📁 Requires

- `ground_truth_images/` as source images
- Corrected JSON files in `annotations/prediction_corrections/`
- A consistent `labels.txt` from the previous training session

📌 You can repeat stages 3–6 iteratively to refine your model with human-in-the-loop corrections.