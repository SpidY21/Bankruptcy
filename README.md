# Bankruptcy Risk Prediction Dataset

## Overview

This dataset contains information about various risk factors related to companies and aims to predict the likelihood of bankruptcy based on these factors. Each row represents a company with specific levels of risk in different areas, and the `class` column indicates whether the company is at risk of bankruptcy. The values in the dataset are categorized as follows:

- `1` represents a high risk.
- `0.5` represents a moderate risk.
- `0` represents a low risk.

## Dataset Description

The dataset includes 7 columns, each describing different risk factors for a company. The target variable is `class`, which identifies whether a company is classified as "bankruptcy" based on its risk levels. Below is a description of each column:

| Column                  | Description                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------|
| `industrial_risk`       | The level of risk related to the company's industry (0 = low, 0.5 = moderate, 1 = high).              |
| `management_risk`       | The level of risk related to the company's management practices (0 = low, 0.5 = moderate, 1 = high).  |
| `financial_flexibility` | The level of risk in the company's financial flexibility (0 = low, 0.5 = moderate, 1 = high).         |
| `credibility`           | The level of risk based on the company's credibility (0 = low, 0.5 = moderate, 1 = high).             |
| `competitiveness`       | The level of risk based on the company's competitiveness in the market (0 = low, 0.5 = moderate, 1 = high). |
| `operating_risk`        | The level of risk in the company's operations (0 = low, 0.5 = moderate, 1 = high).                    |
| `class`                 | Target variable indicating the risk classification, with `bankruptcy` indicating high risk of failure. |

## Objective

The main objective of this dataset is to predict whether a company is at risk of bankruptcy based on various risk factors. This dataset can be used to build classification models that assess the likelihood of bankruptcy, which is valuable for financial analysts, investors, and stakeholders looking to manage risk and make informed investment decisions.

## Key Columns to Explore

1. **Industrial Risk**: High risk in a volatile or declining industry may indicate a greater likelihood of bankruptcy.
2. **Management Risk**: Poor management practices can lead to increased financial distress and higher bankruptcy risk.
3. **Financial Flexibility**: Companies with limited financial flexibility may have difficulty responding to financial challenges.
4. **Credibility**: A lack of credibility (low trust from stakeholders or partners) could increase a company's risk profile.
5. **Competitiveness**: Lower competitiveness in the market may lead to reduced revenue and financial difficulties.
6. **Operating Risk**: Operational inefficiencies or issues can contribute to financial strain, making bankruptcy more likely.

## Usage

This dataset can be used for supervised learning to classify companies as likely to go bankrupt or not based on their risk levels. By analyzing this data, users can develop insights into which risk factors are most strongly associated with bankruptcy, aiding in risk assessment and decision-making.

### Potential Applications

- **Predictive Modeling**: Build machine learning models to predict the bankruptcy risk of a company based on its risk factors.
- **Exploratory Data Analysis (EDA)**: Examine how each risk factor correlates with the likelihood of bankruptcy.
- **Financial and Investment Analysis**: Understand the factors contributing to financial distress and identify companies at risk before they fail.

---

This dataset provides valuable insights for professionals looking to assess financial risk and improve decision-making in the areas of investment and corporate finance.

Link to the deployed App :- https://bankruptcy-jn5klvcyowqer75ncuapppppp.streamlit.app/
