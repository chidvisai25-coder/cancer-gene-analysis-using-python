# RNA‑seq Gene Expression Analysis (FPKM Dataset)

This project explores **RNA‑seq gene expression data** from the file `GSE315381_all.fpkm_anno.csv`, which contains **FPKM (Fragments Per Kilobase of transcript per Million mapped reads)** values along with gene annotations.  
The goal is to perform **statistical analysis and visualization** using Python libraries **NumPy, Pandas, and Matplotlib**.

---

## Features

- **[Data Loading](ca://s?q=Load_gene_expression_dataset_with_pandas)**  
  Import large CSV datasets with Pandas for easy manipulation.

- **[Data Preprocessing](ca://s?q=Data_cleaning_in_gene_expression_dataset)**  
  Handle missing values, filter numeric columns, and prepare data for analysis.

- **[Statistical Analysis](ca://s?q=Descriptive_statistics_with_pandas)**  
  - Summary statistics (mean, median, std, variance).  
  - Correlation analysis between genes.  
  - Outlier detection using z‑scores.  
  - PCA for dimensionality reduction.

- **[Visualization](ca://s?q=Exploratory_visualization_with_matplotlib)**  
  - Histograms of gene expression distributions.  
  - Boxplots for sample comparisons.  
  - Scatter plots for gene correlations.  
  - Heatmaps of correlation matrices.  
  - Line plots for trends.  
  - PCA scatter plots for clustering.

---

## Tech Stack

- **Python 3**
- **NumPy** (numerical analysis)
- **Pandas** (data handling)
- **Matplotlib** (visualization)

---

## How to Run

1. Install dependencies:
   ```bash
   python -m pip install pandas numpy matplotlib
