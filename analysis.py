# =========================================================
# Project: Retail Sales Statistical Distribution Analysis
# =========================================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================================================
# STEP 1: SET STYLE
# =========================================================

sns.set_style("whitegrid")

# =========================================================
# STEP 2: CREATE OUTPUT FOLDER
# =========================================================

os.makedirs("plots", exist_ok=True)

# =========================================================
# STEP 3: LOAD DATASET
# =========================================================

df = pd.read_csv("sales_data.csv")

# =========================================================
# STEP 4: DISPLAY DATASET INFO
# =========================================================

print("\nFirst 5 Rows:\n")
print(df.head())

print("\nColumn Names:\n")
print(df.columns)

# =========================================================
# STEP 5: CALCULATE MEAN & MEDIAN
# =========================================================

mean_sales = df["Total_Sales"].mean()
median_sales = df["Total_Sales"].median()

print("\nMean Sales:", round(mean_sales, 2))
print("Median Sales:", round(median_sales, 2))

# =========================================================
# STEP 6: HISTOGRAM WITH KDE
# =========================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Total_Sales"],
    bins=10,
    kde=True
)

# Mean & Median Lines
plt.axvline(
    mean_sales,
    color="red",
    linestyle="--",
    label="Mean"
)

plt.axvline(
    median_sales,
    color="green",
    linestyle="-",
    label="Median"
)

plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")

plt.legend()

plt.tight_layout()

plt.savefig("plots/histogram.png")

plt.close()

# =========================================================
# STEP 7: KDE PLOT
# =========================================================

plt.figure(figsize=(10, 6))

sns.kdeplot(
    df["Total_Sales"],
    fill=True
)

plt.title("KDE Plot of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Density")

plt.tight_layout()

plt.savefig("plots/kde_plot.png")

plt.close()

# =========================================================
# STEP 8: BOXPLOT
# =========================================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    x=df["Total_Sales"]
)

plt.title("Boxplot of Total Sales")
plt.xlabel("Total Sales")

plt.tight_layout()

plt.savefig("plots/boxplot.png")

plt.close()

# =========================================================
# STEP 9: CATEGORY-WISE DISTRIBUTION COMPARISON
# =========================================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Category",
    y="Total_Sales"
)

plt.title("Sales Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=10)

plt.tight_layout()

plt.savefig("plots/category_comparison.png")

plt.close()

# =========================================================
# STEP 10: PAYMENT METHOD DISTRIBUTION
# =========================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Total_Sales",
    hue="Payment_Method",
    kde=True,
    bins=10
)

plt.title("Sales Distribution by Payment Method")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("plots/payment_method_comparison.png")

plt.close()

# =========================================================
# STEP 11: OUTLIER DETECTION USING IQR
# =========================================================

Q1 = df["Total_Sales"].quantile(0.25)
Q3 = df["Total_Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

outliers = df[
    (df["Total_Sales"] < lower_bound) |
    (df["Total_Sales"] > upper_bound)
]

print("\nOutliers Detected:\n")
print(outliers)

# =========================================================
# STEP 12: SKEWNESS ANALYSIS
# =========================================================

skewness = df["Total_Sales"].skew()

print("\nSkewness Value:", round(skewness, 2))

if skewness > 0:
    skewness_result = "positively skewed"
elif skewness < 0:
    skewness_result = "negatively skewed"
else:
    skewness_result = "symmetric"

print(f"The distribution is {skewness_result}.")

# =========================================================
# STEP 13: EXPORT INTERPRETATION
# =========================================================

interpretation = f"""
Retail Sales Statistical Analysis Report
========================================

The Total Sales distribution was analyzed using
histograms, KDE plots, and boxplots.

The histogram and KDE plot indicate the overall
distribution pattern of sales values.

The mean sales value is {round(mean_sales, 2)}
while the median sales value is {round(median_sales, 2)}.

The boxplot identified possible outliers in the dataset,
especially among high-value electronic products.

Category-wise comparison showed variation in sales
distribution between Electronics, Accessories,
and Home Appliances.

The skewness value is {round(skewness, 2)},
indicating that the distribution is {skewness_result}.

Higher sales values from premium products such as
laptops and air conditioners contribute to the
spread and skewness of the data.
"""

with open("interpretation.txt", "w") as file:
    file.write(interpretation)

# =========================================================
# STEP 14: COMPLETION MESSAGE
# =========================================================

print("\nAnalysis Completed Successfully!")
print("Plots saved inside 'plots' folder.")
print("Interpretation saved as interpretation.txt")