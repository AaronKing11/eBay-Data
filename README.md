# eBay Project Overview
This project consists of multiple components designed to analyze and visualize eBay laptop sales data. The repository includes the following files:

## **Files**
- **ebay_project.ipynb**
    - This Jupyter Notebook contains the core data cleaning, processing, and analytical workflows for the project.
    - It loads, cleans, and merges raw datasets (e.g., EbayPcLaptopDataUnclean.csv and EbayPcLaptopPriceData.csv) to produce a clean, combined dataset (ebay_data_clean.csv).
    - Key tasks include handling missing data, standardizing formats, and creating derived columns for analysis.

- **ebaydashboard.py**
    - A Streamlit app designed to visualize and interact with the cleaned dataset.
    - Features multiple dashboards and filtering options to explore data insights:
      - **Sales Records Filtered by Brand, Color, and Resolution Size**: Allows users to filter the dataset by selected attributes and view the results in a table.
      - **eBay Computers by Brand**: Displays the distribution of computers by brand using a bar chart.
      - **Processing Speed's Impact on Price**: Shows a scatter plot illustrating the relationship between processor speed and price.
      - **eBay Computer Prices and their SSD Capacities**: Highlights the relationship between SSD capacities and prices, segmented by condition (new or used).

- **ebay_data_clean.csv**
    - The cleaned dataset produced by ebay_project.ipynb, combining information from the raw datasets.
    - Contains rows of data with standardized and verified fields, ready for analysis and visualization.

- **EbayPcLaptopDataUnclean.csv and EbayPcLaptopPriceData.csv**
    - Raw datasets with unprocessed information about eBay laptop sales.
    - These files include details such as laptop specifications, prices, and sales information.
    - Used as input files in the data cleaning pipeline.

## Project Workflow
- **Data Cleaning**:
    - Conducted in ebay_project.ipynb, where raw datasets are combined, cleaned, and processed.
    - The output is a clean and well-structured dataset, ebay_data_clean.csv.

- **Data Visualization**:
    - Implemented in ebaydashboard.py using Streamlit.
    - Users can interact with the data through various visualizations, gaining insights into trends and patterns in eBay laptop sales.

## How to Use
  - **Jupyter Notebook**
    - Open ebay_project.ipynb in a Jupyter environment.
    - Follow the steps outlined in the notebook to clean and prepare the data.
    - Export the cleaned data to ebay_data_clean.csv.

  - **Streamlit Dashboard**
    - Ensure ebay_data_clean.csv is in the same directory as ebaydashboard.py.
    - Run the Streamlit app using the command:
        _streamlit run ebaydashboard.py_
    - Interact with the dashboard to explore insights into the data.

## Key Insights
- The project provides insights into factors influencing laptop prices on eBay, including:
    - Brand popularity and its potential impact on sales.
    - Relationships between laptop specifications (e.g., processor speed, SSD capacity) and price.
    - Differences in pricing patterns for new vs. used laptops.
