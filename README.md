# Retail Sales Statistical Distribution Analysis using Python

## Overview

This project performs statistical distribution analysis on retail sales data using Python.  
The analysis includes visualization of data distributions, outlier detection, skewness analysis, and comparison of sales across categories and payment methods.

The project demonstrates how statistical plots can be used to understand business sales patterns and identify trends in retail transaction data.

---

## Features

- Histogram visualization with KDE
- KDE (Kernel Density Estimation) plot
- Boxplot for outlier detection
- Category-wise sales distribution comparison
- Payment method comparison analysis
- Mean and median analysis
- IQR-based outlier detection
- Skewness analysis
- Exported plot images
- Automated interpretation report generation

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

## Project Structure

```text
retail-sales-statistical-analysis/
│
├── plots/
│   ├── histogram.png
│   ├── kde_plot.png
│   ├── boxplot.png
│   ├── category_comparison.png
│   └── payment_method_comparison.png
│
├── sales_data.csv
├── analysis.py
├── interpretation.txt
├── requirements.txt
└── README.md
```

---

## Dataset Information

The dataset contains retail transaction records including:

- Customer details
- Product categories
- Quantity purchased
- Price per unit
- Total sales amount
- Payment methods

### Dataset Columns

- Order_ID
- Customer_Name
- City
- Product
- Category
- Quantity
- Price_Per_Unit
- Total_Sales
- Payment_Method

---

## Statistical Analysis Performed

### 1. Histogram Analysis
Used to visualize the distribution of total sales values.

### 2. KDE Plot
Used to estimate the probability density of sales distribution.

### 3. Boxplot Analysis
Used to detect outliers and understand spread of sales data.

### 4. Category-wise Comparison
Compared sales distributions across product categories.

### 5. Payment Method Comparison
Analyzed sales trends based on payment methods.

### 6. Outlier Detection
Implemented using the Interquartile Range (IQR) method.

### 7. Skewness Analysis
Calculated skewness to understand distribution symmetry.

---

## Installation

Install required libraries using:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pandas matplotlib seaborn
```

---

## How to Run

Run the Python script:

```bash
python analysis.py
```

---

## Output

The program generates:

- Statistical plots saved inside the `plots/` folder
- Interpretation report saved as `interpretation.txt`

---

## Key Insights

- The sales distribution is positively skewed.
- High-value electronics products contribute significantly to outliers.
- Sales patterns vary across product categories and payment methods.
- Mean sales are higher than median sales due to large transaction values.

---

## Example Outputs

### Generated Plots
- Histogram
- KDE Plot
- Boxplot
- Category Comparison Plot
- Payment Method Distribution Plot

---

## Author

Satyam

---
