#  Data Science Salary Prediction Project 
![myImage](https://img.shields.io/badge/Blogger-FF5722?style=for-the-badge&logo=blogger&logoColor=white)
[![myImage](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/fahadrehman07)
![myImage](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
[![myImage](https://img.shields.io/badge/Coursera-0056D2?style=for-the-badge&logo=Coursera&logoColor=white)](https://www.coursera.org/user/4b23ff019e716f13d91d5479b9cd99e5)
![myImage](https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white)

#### Hi there! Wellcome to the Project.

<img src="https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/e015605f-211a-4274-b4f2-cdc3b6c8d270" width="100%" height="350" align="center">

>``` It's how you deal with failure that determines how you achieve success. ```




# 🚩 Table of Contents
- [Project-Overview](https://github.com/FahadUrRehman07/ds_Salary_proj/blob/main/README.md#data-science-salary-estimator-project-overview)
- [Packages](https://github.com/FahadUrRehman07/ds_Salary_proj/blob/main/README.md#-packages)
- [Code and Resources Used](https://github.com/FahadUrRehman07/ds_Salary_proj/blob/main/README.md#code-and-resources-used)
- [Wed Scraping](https://github.com/FahadUrRehman07/ds_Salary_proj/blob/main/README.md#-wed-scraping)
- [Data Cleaning](https://github.com/FahadUrRehman07/ds_Salary_proj/blob/main/README.md#data-cleaning)
- [Exploratory Data Analysis ( EDA)](https://github.com/FahadUrRehman07/ds_Salary_proj/blob/main/README.md#exploratory-data-analysis--eda)
- [Model Building](https://github.com/FahadUrRehman07/ds_Salary_proj/blob/main/README.md#model-building)
- [Model Performance](https://github.com/FahadUrRehman07/ds_Salary_proj/blob/main/README.md#model-performance)
- [Productionization](https://github.com/FahadUrRehman07/ds_Salary_proj/blob/main/README.md#-productionization)




# Data Science Salary Estimator: Project-Overview
* Created a tool that estimates data science [MAE ~ 11k] to help data scientists to negotiate their income when they get a job.
*  Scraped over 1000 job descriptions from glassdoor using Python and Selenium.
*  Engineered features from the text of each job description to quantify the value companies put on python, excel, aws and spark.
*  Optimized Linear, Lasoo and Random Forest Regression using GridSearchCV to reach the best model.
*  Built a client facing API using Flask

# 📦 Packages

### Packages Used in the Project.

|    Name    |                    Description                    |
|    ---     |                       ---                         |
|  Selenium  | Python Library for Data Scraping                  |
|   Pandas   | Python Library for Data Cleaning & EDA            |
|   Numpy    | Python Library                                    |
| Matplotlib | Python Library for Visualization of data          |
|  Seaborn   | Python Library for Visualization of data          |
|  SkLearn   | Python Library for Machine learning Models        |
|   flask    | To built client facing API                        |
|   Pickle   | Used for make the pickle file to use in flask app |
|    json    | Data to be used in flask app                      |

# ![icons8-resources-50](https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/da648015-1b39-46e7-b842-c607bf5f3fcd) Code and Resources Used
The references of code and resources that I took help from to understand and learn and make this project happen.
| Name | Description | Resource Link
| --- | --- | --- |
|  Python | Version = 3.7 |https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe|
| Packages| These are all packages used in project | pandas, numpy, sklearn, seaborn, matplotlib, selenium, flask, json, pickle|
| Web Framework Requirements | Plugin to highlight code syntax | pip install -r requirements.txt
| Scraper Github | I got alot of help and used his code | https://github.com/arapfaik/scraping-glassdoor-selenium.
|  Flask Productionizing | this article help to productionize my flask API | https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2


# 🤖 Wed Scraping:

Tweaked the web scraper github repo **above** to scrape **1000** job posting from **glassdoor**. With each job we got the following:

* Job title.
* Salary Estimate.
* Job Description.
* Rating.
* Company.
* Location.
* Company Headquarters.
* Company Size.
* Company Founded Date.
* Type of Ownership.
* Industry.
* Sector.
* Revenue.
* Competitors

# ![icons8-data-cleaning-68](https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/674f22b6-23c1-4c40-8eee-8484d0065a8d) Data Cleaning
After scraping the data. I needed to clean it up so that i was usable for our model. I made the following changes and created the following variable.

* Parsed **numeric data out of salary**.
* Made columns for **employer provided salary** and **hourly wage**.
* Removed  rows without salary.
* Parsed **rating** out of company text.
* Made a **new column** for company state.
* Added a column for if the **job was at the company's headquarters**.
* Transformed founded **date into age of company**.
* Made column for if different **skills** were listed in the **job description**:
    - **Python**
    - **R**
    - **Excel**
    - **AWS**
    - **Spark**
* Column for simplified **job title** and **seniority**.
* Column for **description length**.


# ![icons8-data-analysis-30](https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/79ab3b0b-a801-4ce4-9eb7-2408ad8d4417) Exploratory Data Analysis ( EDA)
I looked at the distribution of the data and the value counts for the various categorical variables.Below are a few highlights from the pivot tables.

![salary_by_job_title](https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/274b4c4b-11ac-4d4f-89f8-d8218a1af8c5)  ![positions_by_state](https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/101cd04b-e540-4712-8fc1-1bee200c108f)

![correlation_visual](https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/a9e14311-5411-4af6-a87e-8d46f3bfb6be)


# ![icons8-animated-skeleton-100](https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/54c5c1f1-2a73-4752-9868-ceff8989e82c) Model Building
First, I transformed the categorical variable into dummy variables. I also split the data into train and tests sets with a test size of 20%.
I tried three different models and evaluated them using **Mean Abosulte Error**. I choose **MAE** because it is relatively easy to interpret and outliers aren't particulary bad in for the type of model.

I tried three different models.

* **Multiple Linear Regression** : Baseline for the model.

* **Lasso Regression** : Because of the sparse data from the many sategorical variables. I thought a normalized regression like lasso would be effective.

* **Random Forest** : Again with the sparsity associated with the data. I thought that this would be a good fit.
  
# ![icons8-3d-model-50](https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/a84ee45f-41d6-41b3-bf1a-8b13f79a6aa5) Model Performance
The Random Forest model for outperformed the other approaches on the test and validation sets.

* **Random Forest:** MAE ≈ 11.22
* **Linear Regression:** MAE ≈ 18.86
* **Ridge Regression:** MAE ≈ 19.67

# 🎨 Productionization

In this step. I built a **flask API** endpoint that was hosted on a local webserver by following along with the **TDS tutorial** in the reference section **above**. The API endpoint takes in a request with a list of values from a job listing and returns an **estimated salary**.
