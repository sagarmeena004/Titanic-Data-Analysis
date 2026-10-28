# 🚢 Titanic Data Analysis — Project Structure

## 📌 Overview

This document describes the directory structure and organization of the Titanic Data Analysis and Visualization project.

The project uses Python to process an Excel dataset and generate visualizations with Matplotlib.

## 📁 Directory Structure

```text
first project/
│
├── django.py
├── campasX.xlsx
├── requirements.txt
├── README.md
├── .gitignore
│
├── PROJECT_DOCUMENTATION.md
├── INSTALLATION_GUIDE.md
├── USAGE_GUIDE.md
├── PROJECT_STRUCTURE.md
│
└── Titanci_Data.png (generated after execution)
```

## 📄 File Descriptions

### 1. django.py

The main Python script responsible for:

- Loading the Excel dataset.
- Handling missing values.
- Displaying the first 10 rows.
- Analyzing passenger information.
- Creating four visualizations.
- Saving the dashboard as a PNG image.

### 2. campasX.xlsx

The Excel dataset containing Titanic passenger information.

The script uses the following columns:

- Age
- Sex
- Embarked
- Survived

The script also includes commented-out analysis referencing `Pclass`.

### 3. requirements.txt

Contains the Python libraries required to run the project:

```text
numpy
pandas
matplotlib
openpyxl
```

### 4. README.md

Provides the main project introduction, features, technologies, and instructions.

### 5. .gitignore

Specifies files and folders that Git should ignore, including:

- Python cache files
- Virtual environments
- Environment variable files
- IDE configuration files
- Temporary files

### 6. PROJECT_DOCUMENTATION.md

Contains detailed technical information about the project.

Topics include:

- Project objectives
- Technologies
- Dataset columns
- Data preprocessing
- Visualization methods
- Current limitations
- Future improvements

### 7. INSTALLATION_GUIDE.md

Provides step-by-step installation instructions.

Includes:

- Python requirements
- Virtual environment setup
- Dependency installation
- Dataset configuration
- Troubleshooting

### 8. USAGE_GUIDE.md

Explains how to run and use the project.

Includes:

- Execution instructions
- Data processing workflow
- Chart descriptions
- Output information
- Common errors

### 9. PROJECT_STRUCTURE.md

Documents the directory structure and explains the purpose of each project file.

### 10. Titanci_Data.png

A generated visualization dashboard containing four charts:

1. Gender Distribution
2. Embarkation Distribution
3. Age Distribution
4. Survival Distribution

This file is created when the Python script executes successfully.

## 🔄 Project Workflow

```text
Excel Dataset
      |
      v
Python Script
      |
      v
Data Loading
      |
      v
Missing Value Handling
      |
      v
Data Exploration
      |
      v
Matplotlib Visualization
      |
      v
Dashboard Generation
      |
      v
PNG Image Output
```

## ⚙️ Running the Project

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the main Python script:

```bash
python django.py
```

## 📊 Expected Results

The project produces:

- A terminal preview of the first 10 dataset rows.
- Four visualizations in a 2×2 dashboard.
- A high-resolution PNG output image.

## 🚀 Future Project Organization

As the project grows, the following improvements could be considered:

- Moving datasets into a `data/` directory.
- Storing generated charts in an `outputs/` directory.
- Adding a `tests/` directory.
- Separating data preprocessing and visualization functions.
- Adding configuration options for input and output filenames.

## ✅ Conclusion

This project structure keeps the source code, dataset, dependencies, and documentation organized for GitHub users and future development.