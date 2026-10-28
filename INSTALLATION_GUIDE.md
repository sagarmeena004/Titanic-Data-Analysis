# 🚢 Titanic Data Analysis — Installation Guide

## 📌 Overview

This guide explains how to install and run the Titanic Data Analysis project on a local computer.

The project uses Python, Pandas, NumPy, Matplotlib, and OpenPyXL to analyze and visualize Titanic passenger data.

## 1. Prerequisites

Before running the project, make sure the following tools are installed:

- Python 3.10 or later
- pip (Python package manager)
- Git (optional)
- Visual Studio Code (recommended)

## 2. Download the Project

Clone the GitHub repository:

```bash
git clone <repository-url>
```

Alternatively, download the project as a ZIP file from GitHub.

## 3. Open the Project Directory

Navigate to the project folder:

```powershell
cd "first project"
```

## 4. Create a Virtual Environment

Creating a virtual environment is recommended to keep project dependencies isolated.

On Windows:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, use the virtual environment's Python executable directly.

## 5. Install Required Libraries

Install all dependencies:

```powershell
python -m pip install -r requirements.txt
```

The following packages will be installed:

| Library | Purpose |
|---|---|
| NumPy | Numerical computing |
| Pandas | Data analysis and manipulation |
| Matplotlib | Data visualization |
| OpenPyXL | Excel file support |

## 6. Verify Installation

Run:

```powershell
python -c "import numpy, pandas, matplotlib, openpyxl; print('All libraries installed successfully')"
```

## 7. Dataset Setup

Ensure the Excel dataset is available in the project directory.

Required dataset filename:

`campasX.xlsx`

The dataset must contain the following columns:

- Age
- Sex
- Embarked
- Survived

The script also contains commented-out code referencing `Pclass`.

## 8. Run the Project

Execute:

```powershell
python django.py
```

The program will:

1. Load the Excel dataset.
2. Handle missing values.
3. Display the first 10 rows.
4. Generate four data visualizations.
5. Save the visualization dashboard.
6. Display the dashboard.

## 9. Expected Output

The generated image will be saved as:

`Titanci_Data.png`

The image contains four visualizations:

- Gender distribution
- Embarkation distribution
- Age distribution
- Survival distribution

## 10. Troubleshooting

### ModuleNotFoundError

If a required library is missing, reinstall dependencies:

```powershell
python -m pip install -r requirements.txt
```

### FileNotFoundError

Ensure `campasX.xlsx` is located in the same directory from which you run the script.

### Excel Reading Error

Verify that OpenPyXL is installed:

```powershell
python -m pip install openpyxl
```

### Python Command Not Recognized

Check Python installation:

```powershell
python --version
```

On Windows, you can also try the Python launcher:

```powershell
py --version
```

## 11. Notes

- Run the script from the project directory.
- Keep the dataset filename unchanged.
- The output image will be overwritten when the script runs again.
- A graphical environment is needed to display the Matplotlib window.

## 12. Conclusion

After following these steps, the project should be ready for local execution and Titanic passenger data visualization.