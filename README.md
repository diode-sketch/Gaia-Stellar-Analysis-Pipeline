# Gaia Data Analysis

### Stellar Kinematics and Photometric Exploration

This repository provides a computational framework for processing and visualizing astronomical data from the **ESA Gaia Mission (DR3)**. By leveraging the Python scientific stack, the project transforms raw celestial coordinates into meaningful astrophysical insights.

---

## Overview

The primary objective of this project is to filter observational noise and process large-scale stellar catalogs to reconstruct the physical properties of stars. The core of the analysis focuses on the construction of **Hertzsprung-Russell (HR) diagrams** to identify stellar evolution stages.

## Technical Stack

* **NumPy**: High-performance vectorization and distance calculus from parallax.
* **Pandas**: Data wrangling, cleaning missing values, and managing large CSV or VOTable datasets.
* **Matplotlib**: Scientific data visualization and density mapping.

## Methodology

1. **Quality Control**: Automated removal of sources with high uncertainty where $parallax\_error > 0.05$.
2. **Distance Modulus**: Implementation of the absolute magnitude formula:

$$M = m - 5 \log_{10}(d) + 5$$

3. **Stellar Synthesis**: Mapping temperature versus luminosity to categorize Main Sequence, Red Giant, and White Dwarf populations.

## Project Structure

* `analysis.py`: Main processing script.
* `data/`: Directory for raw Gaia source files in CSV format.
* `plots/`: Generated visualizations and HR diagrams.
* `requirements.txt`: List of environment dependencies.

## Installation and Usage

```bash
# Clone the repository
git clone [https://github.com/your-username/Gaia-Data-Analysis.git](https://github.com/your-username/Gaia-Data-Analysis.git)

# Install dependencies
pip install -r requirements.txt

# Run the analysis
python analysis.py
