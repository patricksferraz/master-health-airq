# Master Health AirQ 🌍

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Data Science](https://img.shields.io/badge/Data%20Science-Project-purple)](https://github.com/patricksferraz/master-health-airq)

A comprehensive data science project focused on analyzing health and air quality data, featuring advanced data preprocessing, analysis, and visualization capabilities.

## 📋 Overview

This project provides a robust framework for analyzing health and environmental data, with a particular focus on air quality metrics. It includes tools for data preprocessing, address processing, and comprehensive data analysis using modern data science techniques.

## 🚀 Features

- **Data Preprocessing**: Advanced data cleaning and normalization tools
- **Address Processing**: Automated address collection and standardization using zip codes
- **Interactive Analysis**: Jupyter notebooks with interactive visualizations
- **Geospatial Analysis**: Integration with geospatial data processing
- **Comprehensive Reporting**: Automated generation of analysis results and visualizations

## 🛠️ Technical Stack

- Python 3.7+
- Jupyter Lab
- Key Libraries:
  - Pandas & NumPy for data manipulation
  - Matplotlib & Seaborn for visualization
  - GeoPandas for geospatial analysis
  - Scikit-learn for machine learning
  - PySUS for health data processing

## 🏗️ Project Structure

```
master-health-airq/
├── code/
│   ├── preprocessing-datasets.ipynb    # Data preprocessing notebook
│   ├── data-analysis.ipynb            # Main analysis notebook
│   ├── requirements.txt               # Python dependencies
│   ├── master-ds.yml                  # Conda environment
│   └── utils/                         # Utility scripts
├── datas/
│   ├── preprocessing/                 # Processed datasets
│   └── raw/                          # Raw data files
└── results/                          # Analysis outputs
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Conda package manager
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/patricksferraz/master-health-airq.git
cd master-health-airq
```

2. Create and activate the conda environment:
```bash
conda env create -n master-health -f code/master-ds.yml
conda activate master-health
```

3. Install Jupyter Lab extensions:
```bash
conda install -c conda-forge nodejs
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

4. Launch Jupyter Lab:
```bash
jupyter-lab
```

## 📊 Usage

### Data Preprocessing

1. Open `preprocessing-datasets.ipynb` in Jupyter Lab
2. Follow the notebook instructions for data preprocessing
3. Processed data will be saved in the `datas/preprocessing` directory

### Address Processing

1. Copy `.env-example` to `.env` and configure your API tokens
2. Create a `.buffer` directory and add your CSV.GZ files
3. Run the address processing script:
```bash
python code/utils/process_addr.py
```

### Data Analysis

1. Open `data-analysis.ipynb` in Jupyter Lab
2. Execute the cells sequentially
3. Results will be generated in the `results` directory

## 📈 Results

The analysis results, including graphs and tables, are stored in the `results` directory. These outputs provide insights into:
- Health metrics analysis
- Air quality patterns
- Geographic distribution of data
- Statistical correlations
- Temporal trends

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

- **Patrick Sferraz** - [GitHub Profile](https://github.com/patricksferraz)

## 🙏 Acknowledgments

- PySUS team for their excellent health data processing library
- The open-source community for their invaluable tools and resources
