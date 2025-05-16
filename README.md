<p align="center">
  <img src="docs/assets/Dingir.png" alt="TiamaT Logo" width="100"/>
</p>

# 🐉 TiamaT – Toolkit for Integrated Annotation and Machine-learning Assisted Training

**TiamaT** is a complete, modular pipeline that helps transform raw, unstructured images into fully annotated, machine learning–ready datasets.

Designed for flexibility and reusability, it supports every step of the computer vision training workflow:
- 📌 Manual annotation with [Label Studio](https://labelstud.io/)
- 🔧 Dataset formatting and transformation
- 🧠 Model training and inference using YOLO
- ✅ Evaluation and correction through human-in-the-loop cycles

Originally built for historical document analysis, TiamaT fits any project where annotations are built incrementally or interactively.

> The name is a nod to [**Tiamat**](https://en.wikipedia.org/wiki/Tiamat), the Mesopotamian goddess of the ocean and chaos — an appropriate symbol for turning raw data into structured knowledge.

---

## Table of Contents

- [🌍 Workflow Overview](#-workflow-overview)
  - [💫 Execution Modes (Notebook & Script)](#-execution-modes-notebook--script)
  - [🧿 Pipeline Steps Overview](#️-pipeline-steps-overview)
  - [🧱 Project Folder Structure](#-project-folder-structure)
- [🚀 Running TiamaT](#-running-tiamat)
  - [🐦‍🔥 Iterative Workflow](#-iterative-workflow)
  - [🌈 Shared Configuration Variables](#-shared-configuration-variables)
- [🧩 Installation](#️-installation)
  - [👾 Requirements](#-requirements) 
  - [🖌️ Label Studio Environment](#-label-studio-environment)
    - [📦 Using Conda](#-using-conda)
    - [🐍 Using a Python virtual environment](#-using-a-python-virtual-environment)
  - [🐲 Tiamat Environment](#-tiamat-environment)
    -  [📦 Using Conda](#-using-conda-1)
    - [🐍 Using a Python virtual environment](#-using-a-python-virtual-environment-1)
- [📜 License & Attribution](#-license--attribution)

---

## 🌍 Workflow Overview

The TiamaT pipeline covers the full annotation-to-training lifecycle.
It is organized as a **modular sequence of stages**, which can be executed in two different modes depending on your needs:


### 💫 Execution Modes (Notebook & Script)

You can use TiamaT either as:

- 📓 **Interactive notebooks** – ideal for exploration, development, or adjusting specific parameters step by step.
- ⚙️ **Command-line scripts** – ideal for automation, production, or batch execution.

Each stage of the pipeline exists in both formats. The scripts are located in `src/scripts/` and replicate the logic of the Jupyter notebooks in `src/notebooks/`.

> You can mix both modes depending on your workflow — for instance, prototype in notebook, then automate with scripts.

---

### 🧿 Pipeline Steps Overview

> [!NOTE]
> For a detailed description of each stage (inputs, outputs, scripts, tips), see [docs/pipeline_overview.md](docs/pipeline_overview.md).



| Stage | Description | Notebook | Script |
|-------|-------------|----------|--------|
| **0** | Launch Label Studio (optional) | `0_Launching_LS.ipynb` | *Use `label-studio` CLI* |
| **1** | Extract annotated training data | `1_Get_training_data.ipynb` | `extract_training_data.py` |
| **2** | Compute dataset statistics | `2_Statistics_for_training_data.ipynb` | `analyze_dataset.py` |
| **3** | Prepare data and train model | `3_Data_preparation_and_training.ipynb` | `train_model.py` |
| **4** | Predict on new images | `4_Predicting_and_checking_YOLO_results.ipynb` | `predict.py` |
| **5** | Evaluate model & review corrections | `5_Model_evaluation.ipynb` | `evaluate_model.py` |
| **6** | Generate updated ground truth | `6_Generate_new_ground_truth.ipynb` | `generate_ground_truth.py` |

> 📝 Notebooks are recommended for first-time users and experimentation.
>
> 🖥️ Scripts are better suited for iterative workflows and large-scale runs.

---

### 🧱 Project Folder Structure

To ensure smooth execution, the TiamaT pipeline expects a specific folder organization.
This structure separates raw inputs, manual annotations, training datasets, and model outputs in a modular and reproducible way.

```
TiamaT/
├── data/                         # Final YOLO-formatted training datasets (images, labels, labels.txt)
├── project/                      # Raw images and annotations (excluded from Git except structure)
│   ├── image_inputs/             # Source images used in the pipeline
│   │   ├── ground_truth_images/       # Manually annotated images used for training
│   │   └── eval_images/               # Images used for inference and manual correction
│   ├── annotations/             # Annotations exported or corrected via Label Studio
│   │   ├── ground_truth/              # Ground truth annotations manually created in LS
│   │   └── prediction_corrections/    # Corrections made after model predictions
├── output/                       # Model training and prediction results
│   └── runs/
│       ├── train/                     # YOLO training runs (auto-generated folders: exp1, exp2, ...)
│       └── predict/                   # Inference outputs (e.g., predicted labels)
├── src/                          # Core source code
│   ├── notebooks/                   # Step-by-step Jupyter notebooks for the full pipeline
│   ├── scripts/                     # Python scripts for CLI-based execution
│   ├── modules/                     # Reusable Python modules (transforms, utils, etc.)
│   └── config.py                    # Shared configuration and path definitions
├── requirements/                 # Installation requirements (pip or conda)
│   ├── tiamat.txt                   # Main pipeline dependencies (YOLO, OpenCV, etc.)
│   └── label_studio.txt             # Label Studio annotation environment
├── .env.example                 # Template for custom environment variables
└── README.md                    # Main project documentation

```

⭐️ All notebooks and scripts rely on this layout to locate and process data automatically.

> [!WARNING]
> Only `project_name` can be freely renamed — all other folder names must be preserved for the code to function correctly.


---

## 🚀 Running TiamaT

Once your environments are set up and the project structure is ready, you can execute the pipeline either via Jupyter notebooks or Python scripts (see [Workflow Overview](#-workflow-overview) for the full step mapping).

### 🐦‍🔥 Iterative Workflow

TiamaT is built around a human-in-the-loop workflow.
The model is not evaluated on a classic "test set", but rather through manual correction of its predictions. This makes the pipeline especially useful when no gold-standard ground truth exists upfront.

```text
        ┌────────────────────────────┐
        │ 0. Launch Label Studio     │
        └─────────────┬──────────────┘                              
                  	  ▼                          
        ┌────────────────────────────┐           
        │ 1. Extract Training Data   │           
        └─────────────┬──────────────┘           
                      ▼                          
        ┌────────────────────────────┐             
        │ 2. Dataset Statistics      │ ◄─────┐
        └─────────────┬──────────────┘       │
                      ▼                      │
        ┌────────────────────────────┐       │
        │ 3. Train YOLO Model        │       │
        └─────────────┬──────────────┘       │
                      ▼                      │
        ┌────────────────────────────┐       │
        │ 4. Predict with Model      │       │
        └─────────────┬──────────────┘       │
                      ▼                      │
        ┌────────────────────────────┐       │
        │ 5. Review + Correction     │       │
        └─────────────┬──────────────┘       │
                      ▼                      │
        ┌────────────────────────────┐       │
        │6. Generate New Ground Truth│───────┘
        └────────────────────────────┘

           ⤷ Loop back to step 3 to retrain
```



You can repeat steps 3 to 6 as many times as needed to improve the model’s performance, especially when working with complex or evolving datasets.

📌 You may skip any step if you're starting from partially prepared data or existing corrections.

---

### 🌈 Shared Configuration Variables

Some key variables are shared across both notebooks and scripts.  
They define core paths, session parameters, and model references, and are typically loaded from a `.env` file using the [`python-dotenv`](https://pypi.org/project/python-dotenv/) package.

| Variable | Description |
|----------|-------------|
| `PROJECT_NAME` | Project name used in folder paths |
| `LS_PORT` | Port to run Label Studio locally |
| `project_folder` | Path to the current project's folder (under `project/`) |
| `data_folder` | Output folder for YOLO-ready datasets (`data/`) |
| `training_folder` | Path to the training dataset inside `data/` |
| `img_dataset_folder` | Path to images used for inference |
| `model_folder` | Path to a YOLO model used for inference or evaluation |
| `pretrained_model` | Path to a pre-trained YOLO model (optional) |

These variables are typically defined in your `.env` file and automatically loaded into both notebooks and scripts at runtime.

---

## 🧩 Installation

TiamaT uses **two separate environments**:

- 🖌️ One for annotation and project setup using [Label Studio](https://labelstud.io/)
- 🐲 One for model training, inference, and evaluation using [YOLO](https://github.com/ultralytics/ultralytics)

You can install both environments using either **Conda** or **Python virtual environments (venv)**.

---

### 👾 Requirements

Before installing, make sure you have:

- Python **3.10+**
- Either `conda` or `venv` (choose your preferred environment manager)
- Jupyter Notebook or JupyterLab (only needed for notebook users)
- Internet access to fetch packages

📦 Dependencies are listed in the `requirements/` folder:
- `label_studio.txt` or `label_studio_environment.yml`
- `tiamat.txt` or `tiamat_environment.yml`

> ⚠️ **PyTorch is not included in the TiamaT environment files.**  
> You must install it manually according to your machine’s configuration (CPU / GPU / CUDA).  
> 👉 See: [https://pytorch.org/get-started/locally](https://pytorch.org/get-started/locally)

---

### 🖌️ Setting up the Label Studio Environment

#### 📦 Using Conda

```bash
conda create --name label-studio
conda activate label-studio

# Only required for Label Studio 1.7.2
conda install psycopg2

pip install label-studio
```

#### 🐍 Using a Python virtual environment

```bash
python3 -m venv label-studio_env
source label-studio_env/bin/activate

pip install --upgrade pip
pip install label-studio
```

> [!NOTE]
> For more information about installing Label Studio, see the official documentation:
> - [Install with Anaconda](https://labelstud.io/guide/install.html#Install-with-Anaconda)
> - [Install using pip](https://labelstud.io/guide/install.html#Install-using-pip)

---

### 🐲 Setting up the TiamaT Environment (YOLO)
#### 📦 Using Conda

```bash
conda env create -f requirements/tiamat_environment.yml
conda activate tiamat_env

# ⚠️ Install PyTorch manually according to your system:
# https://pytorch.org/get-started/locally
```

#### 🐍 Using a Python virtual environment

```bash
python3 -m venv tiamat_env
source tiamat_env/bin/activate

pip install --upgrade pip
pip install -r requirements/tiamat.txt

# ⚠️ Then install PyTorch manually from:
# https://pytorch.org/get-started/locally
```

---

### 📓 (Optional) Jupyter Kernel Registration

If you plan to use Jupyter notebooks, you may register each environment as a kernel:

```bash
# Install Jupyter-compatible kernel support
pip install ipython ipykernel
python -m ipykernel install --user --name=<env_name>

```
> ![WARNING]
> Replace <env_name> with `label-studio_env` or `tiamat_env` accordingly.

This step is **not required** if you're only using the scripts in `src/scripts/`.

---

You're now ready to run the pipeline — either through interactive notebooks or command-line scripts.

---

🌟 Whether you're working on historical archives, custom datasets, or iterative model refinement, TiamaT is designed to adapt to your workflow.

---

## 📜 License & Attribution

Any use, even partial, of the content in this repository must be accompanied by proper citation.

**Made with ❤️ by [Marion Charpier](https://github.com/Chaouabti/)**  
© 2023–2025 • Project **TiamaT**

---

🙌 Want to contribute? See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).
