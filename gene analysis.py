import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------- Load Dataset ----------------
# Adjust encoding or delimiter if needed
df = pd.read_csv("GSE315381_all.fpkm_anno.csv")

# ---------------- Inspect Data ----------------
print("Shape of dataset:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())

# ---------------- Select Numeric Columns ----------------
numeric_df = df.select_dtypes(include=[np.number])

# ---------------- Basic Statistics ----------------
print("\nSummary Statistics:\n", numeric_df.describe())
print("\nMissing Values:\n", numeric_df.isnull().sum())

# Mean, Median, Std
print("\nColumn Means:\n", numeric_df.mean())
print("\nColumn Medians:\n", numeric_df.median())
print("\nColumn Std Dev:\n", numeric_df.std())

# ---------------- Correlation Analysis ----------------
corr_matrix = numeric_df.corr()
print("\nCorrelation Matrix:\n", corr_matrix)

# ---------------- Outlier Detection ----------------
z_scores = np.abs((numeric_df - numeric_df.mean()) / numeric_df.std())
outliers = (z_scores > 3).sum()
print("\nOutlier Counts per Column:\n", outliers)

# ---------------- PCA (Dimensionality Reduction) ----------------
X_centered = numeric_df - numeric_df.mean()
U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
pca_components = U[:, :2] @ np.diag(S[:2])
print("\nFirst two PCA components:\n", pca_components[:5])

# ---------------- Graphical Representations ----------------

# Histogram of first numeric column
numeric_df.iloc[:,0].hist(bins=30)
plt.title("Histogram of First Column")
plt.show()

# Boxplot of first 5 numeric columns
numeric_df.iloc[:,0:5].boxplot()
plt.title("Boxplot of First 5 Columns")
plt.show()

# Scatter plot between first two numeric columns
plt.scatter(numeric_df.iloc[:,0], numeric_df.iloc[:,1])
plt.xlabel(numeric_df.columns[0])
plt.ylabel(numeric_df.columns[1])
plt.title("Scatter Plot")
plt.show()

# Heatmap of correlation matrix
plt.imshow(corr_matrix, cmap="coolwarm", interpolation="none")
plt.colorbar()
plt.title("Correlation Heatmap")
plt.show()

# Line plot of first column
plt.plot(numeric_df.iloc[:,0])
plt.title("Line Plot of First Column")
plt.show()

# PCA scatter plot
plt.scatter(pca_components[:,0], pca_components[:,1])
plt.title("PCA Scatter Plot (First 2 Components)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
