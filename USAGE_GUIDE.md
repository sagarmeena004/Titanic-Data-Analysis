# 🚢 Titanic Data Analysis — Usage Guide

## 📌 Introduction

This guide explains how to use the Titanic Data Analysis and Visualization project.

The project analyzes Titanic passenger information using Python, Pandas, and Matplotlib.

It generates four visualizations to help understand passenger demographics and survival statistics.

## 1. Project Requirements

Before running the project, ensure that Python and the required libraries are installed.

Required libraries:

- NumPy
- Pandas
- Matplotlib
- OpenPyXL

Install all dependencies using:

```bash
python -m pip install -r requirements.txt
```

## 2. Project Files

The project contains the following files:

| File | Description |
|---|---|
| django.py | Main Python data analysis script |
| campasX.xlsx | Titanic passenger dataset |
| README.md | Project overview |
| requirements.txt | Python dependencies |
| INSTALLATION_GUIDE.md | Installation instructions |
| PROJECT_DOCUMENTATION.md | Detailed project documentation |
| .gitignore | Git exclusion rules |
| USAGE_GUIDE.md | Usage instructions |

## 3. Running the Project

Open a terminal in the project directory.

Run:

```bash
python django.py
```

The program will automatically load the Excel dataset and perform the analysis.

## 4. Data Loading

The dataset is loaded using Pandas:

```python
df = pd.read_excel('campasX.xlsx')
```

The dataset must be available in the project directory.

## 5. Data Cleaning

The program handles missing values in two columns.

### Age Column

Missing age values are replaced with the mean age.

### Embarked Column

Missing embarkation values are replaced with `S`.

This prepares the data for visualization.

## 6. Data Preview

The program displays the first 10 rows of the dataset:

```python
print(df.head(10))
```

This helps users understand the dataset structure.

## 7. Data Visualization

The project generates four charts in a 2×2 dashboard.

### Chart 1: Gender Distribution

**Chart Type:** Bar Chart

Displays passenger distribution by gender.

### Chart 2: Embarkation Distribution

**Chart Type:** Pie Chart

Displays the distribution of passengers across embarkation categories.

### Chart 3: Age Distribution

**Chart Type:** Histogram

Displays the distribution of unique age values in the current implementation.

### Chart 4: Survival Distribution

**Chart Type:** Pie Chart

Displays the proportions of survived and non-survived passengers.

## 8. Understanding the Dashboard

The dashboard is arranged as follows:

| Position | Visualization |
|---|---|
| Top Left | Gender Distribution |
| Top Right | Embarkation Distribution |
| Bottom Left | Age Distribution |
| Bottom Right | Survival Distribution |

The dashboard title is:

**Data Analysis with Python**

## 9. Saving the Visualization

The program automatically saves the dashboard using:

```python
plt.savefig('Titanci_Data.png', dpi=300, bbox_inches='tight')
```

The generated image is saved in the current working directory.

**Output filename:** `Titanci_Data.png`

**Resolution setting:** 300 DPI

## 10. Customizing the Charts

Users can customize the visualizations by modifying the Matplotlib settings.

Possible customizations include:

- Changing chart colors.
- Updating chart titles.
- Modifying axis labels.
- Adjusting figure dimensions.
- Changing the histogram bin count.
- Updating grid appearance.

## 11. Common Errors

### Missing Dataset

If the Excel file cannot be found, verify that `campasX.xlsx` exists in the current working directory.

### Missing Libraries

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

### Missing Columns

Ensure the dataset contains:

- Age
- Sex
- Embarked
- Survived

### Chart Display Issues

Make sure Matplotlib is installed and the script is running in an environment that supports graphical windows.

## 12. Current Limitations

The existing script has some limitations:

- The age histogram uses unique age values rather than all passenger ages.
- Some chart labels depend on the ordering of dataset values.
- The script does not validate input columns.
- The input and output filenames are fixed.

## 13. Conclusion

This project provides practical experience with Python-based exploratory data analysis.

It demonstrates how to load Excel datasets, handle missing values, explore passenger information, and generate visual reports using Matplotlib.