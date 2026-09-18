# Data Science Salary Prediction

An end-to-end machine-learning project for estimating data-science salaries from job-market data.

## 🎯 Project Overview

**Web Scraping → Data Cleaning → EDA → Feature Engineering → Model Training → Evaluation → Flask API**

The project scraped more than 1,000 job descriptions and extracted salary, company, location, job-description, and technology-related attributes.

## 🔍 Data Collection

Includes fields such as job title, salary estimate, job description, company, location, rating, company size, industry/sector, revenue, and competitors.

## 🧹 Data Preparation

- Parse numeric salary information
- Identify hourly/employer-provided salary
- Remove records without salary
- Extract company ratings
- Create location/state features
- Calculate company age
- Extract technology indicators from job descriptions
- Simplify job titles and seniority
- Measure description length

Technologies explored include **Python, R, Excel, AWS, and Spark**.

## 📊 Exploratory Data Analysis

The project investigates salary distributions and relationships across job titles, locations, company attributes, and other categorical variables.

## 🤖 Machine Learning

Models explored:
- Multiple Linear Regression
- Lasso Regression
- Random Forest Regression

Evaluation metric: **Mean Absolute Error (MAE)**.

Historical project results:

| Model | Reported MAE |
|---|---:|
| Random Forest | 11.22 |
| Linear Regression | 18.86 |
| Ridge Regression | 19.67 |

These are historical reported results and should be revalidated before being used as current benchmark claims.

## 🚀 Productionization

A Flask API is included to accept job-related inputs and return an estimated salary.

## 🛠️ Technology Stack

Python · Pandas · NumPy · Scikit-learn · Selenium · Matplotlib · Seaborn · Flask

## ⚠️ Reproducibility Notes

The repository contains older artifacts, including notebook checkpoints and historical environment references. These should be standardized before presenting the project as fully reproducible.

**Author:** Fahad Ur Rehman
