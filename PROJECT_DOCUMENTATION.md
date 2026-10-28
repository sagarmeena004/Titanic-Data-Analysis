# Titanic Data Analysis — Project Documentation

## 1. Introduction

Titanic Data Analysis is a Python-based exploratory data analysis and visualization project.

The project uses a Titanic passenger dataset stored in an Excel file to explore passenger demographics, embarkation locations, age distribution, and survival statistics.

The primary objective is to practice data preprocessing, data exploration, and visualization using Python libraries.

## 2. Project Objectives

The main objectives of this project are:

- Understand the structure of a real-world dataset.
- Read Excel data using Pandas.
- Identify and handle missing values.
- Analyze passenger characteristics.
- Visualize categorical and numerical data.
- Create multiple charts in a single dashboard.
- Export visualizations as a high-resolution image.

## 3. Technologies Used

### Python
Python is the primary programming language used to implement the analysis.

### Pandas
Pandas is used for loading, cleaning, and exploring the dataset.

### NumPy
NumPy is imported as a numerical computing library, although the current script does not directly use its functions.

### Matplotlib
Matplotlib is used to create bar charts, pie charts, and histograms.

### OpenPyXL
OpenPyXL is used by Pandas to read Excel `.xlsx` files.

## 4. Dataset Information

**Dataset File:** `campasX.xlsx`

The Python script uses the following columns:

| Column | Description |
|---|---|
| Age | Passenger age |
| Sex | Passenger gender |
| Embarked | Passenger embarkation location |
| Survived | Passenger survival status |
| Pclass | Passenger ticket class |

The dataset is loaded using:

```python
df = pd.read_excel('campasX.xlsx')
```

## 5. Data Preprocessing

### Handling Missing Age Values

Missing values in the `Age` column are replaced with the mean age.

```python
df['Age'].fillna(df['Age'].mean(), inplace=True)
```

### Handling Missing Embarked Values

Missing values in the `Embarked` column are replaced with `S`.

```python
df['Embarked'].fillna("S", inplace=True)
```

### Data Preview

The first 10 rows of the dataset are displayed using:

```python
print(df.head(10))
```

## 6. Data Visualization

The project creates a dashboard containing four visualizations.

### 6.1 Gender Distribution

A bar chart displays passenger counts by gender.

### 6.2 Embarkation Distribution

A pie chart displays the distribution of passengers across embarkation categories.

### 6.3 Age Distribution

A histogram displays the distribution of unique age values in the current implementation.

### 6.4 Survival Distribution

A pie chart displays the proportion of survived and non-survived passengers.

## 7. Dashboard Configuration

The dashboard is created using Matplotlib:

```python
fig, ax = plt.subplots(2, 2, figsize=(15, 10))
```

This creates a 2×2 layout containing four charts.

## 8. Exporting the Dashboard

The visualization dashboard is saved using:

```python
plt.savefig('Titanci_Data.png', dpi=300, bbox_inches='tight')
```

The output image is saved at 300 DPI.

## 9. Project Workflow

1. Import Python libraries.
2. Load the Excel dataset.
3. Handle missing values.
4. Preview the dataset.
5. Calculate passenger distributions.
6. Generate visualizations.
7. Arrange charts into a dashboard.
8. Save the dashboard as a PNG image.
9. Display the dashboard.

## 10. Current Limitations

- The age histogram uses unique ages rather than all passenger age observations.
- Some chart labels are based on the order returned by the dataset.
- The script assumes the Excel dataset contains the required columns.
- Dataset validation and automated error handling are not implemented.
- The script uses a fixed Excel filename.

## 11. Future Improvements

Possible improvements include:

- More accurate age distribution visualization.
- Passenger survival analysis by gender.
- Survival analysis by ticket class.
- Improved chart labeling.
- Dataset validation.
- Automated report generation.
- Interactive data visualization dashboards.

## 12. Conclusion

This project demonstrates fundamental data analysis and visualization techniques using Python.

It provides practical experience in working with Excel datasets, preprocessing missing values, and generating graphical representations of passenger information.