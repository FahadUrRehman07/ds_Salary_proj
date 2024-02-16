# ds_Salary_proj

> Fahad Ur Rehman  Markdown and Github Editor - It's how you deal with failure that determines how you achieve success.

  ![Name Logo](https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/e015605f-211a-4274-b4f2-cdc3b6c8d270)




## 🚩 Table of Contents

- [Peoject Overview](#-Project-Overview)
- [Packages](#-packages)
- [Why TOAST UI Editor?](#-why-toast-ui-editor)
- [Features](#-features)
- [Examples](#-examples)
- [Browser Support](#-browser-support)
- [Pull Request Steps](#-pull-request-steps)
- [Contributing](#-contributing)
- [TOAST UI Family](#-toast-ui-family)
- [Used By](#-used-by)
- [License](#-license)


## Data Science Salary Estimator: Project-Overview
* Created a tool that estimates data science [MAE ~ 11k] to help data scientists to negotiate their income when they get a job.
*  Scraped over 1000 job descriptions from glassdoor using Python and Selenium.
*  Engineered features from the text of each job description to quantify the value companies put on python, excel, aws and spark.
*  Optimized Linear, Lasoo and Random Forest Regression using GridSearchCV to reach the best model.
*  Built a client facing API using Flask

## 📦 Packages

### Packages Used in the Project.

|    Name    |                    Description                    |
|    ---     |                       ---                         |
|  Selenium  | Python Library for Data Scraping                  |
|    ---     |                       ---                         |
|   Pandas   | Python Library for Data Cleaning & EDA            |
|    ---     |                       ---                         |
|   Numpy    | Python Library                                    |
|    ---     |                       ---                         |
| Matplotlib | Python Library for Visualization of data          |
|    ---     |                       ---                         |
|  Seaborn   | Python Library for Visualization of data          |
|    ---     |                       ---                         |
|  SkLearn   | Python Library for Machine learning Models        |
|    ---     |                       ---                         |
|   flask    | To built client facing API                        |
|    ---     |                       ---                         |
|   Pickle   | Used for make the pickle file to use in flask app |
|    ---     |                       ---                         |
|    json    | Data to be used in flask app                      |

# Code and Resources Used
The references of code and resources that I took help from to understand and learn and make this project happen.
| Name | Description | Resource Link
| --- | --- | --- |
|  Python | Version = 3.7 |https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe|
| Packages| These are all packages used in project | pandas, numpy, sklearn, seaborn, matplotlib, selenium, flask, json, pickle|
| Web Framework Requirements | Plugin to highlight code syntax | pip install -r requirements.txt
| Scraper Github | I got alot of help and used his code | https://github.com/arapfaik/scraping-glassdoor-selenium.
|  Flask Productionizing | this article help to productionize my flask API | https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2


## 🤖 Wed Scraping:

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

# Data Cleaning
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


### Exploratory Data Analysis ( EDA)

![salary_by_job_title](https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/274b4c4b-11ac-4d4f-89f8-d8218a1af8c5)  ![positions_by_state](https://github.com/FahadUrRehman07/ds_Salary_proj/assets/128632222/101cd04b-e540-4712-8fc1-1bee200c108f)


* **Table** : Through the context menu of the table, you can add or delete columns or rows of the table, and you can also arrange text in cells.
* **Custom Block Editor** : The custom block area can be edited through the internal editor.
* **Copy and Paste** : Paste anything from browser, screenshot, excel, powerpoint, etc.

### UI
* **Toolbar** : Through the toolbar, you can style or add elements to the document you are editing.
![UI](https://user-images.githubusercontent.com/37766175/121808231-767b0f80-cc92-11eb-82a0-433123746982.png)

* **Dark Theme** : You can use the dark theme.
![UI](https://user-images.githubusercontent.com/37766175/121808649-8136a400-cc94-11eb-8674-812e170ccab5.png)

### Use of Various Extended Functions - Plugins

![plugin](https://user-images.githubusercontent.com/37766175/121808323-d8d41000-cc92-11eb-9117-b92a435c9b43.png)

CommonMark and GFM are great, but we often need more abstraction. The TOAST UI Editor comes with powerful **Plugins** in compliance with the Markdown syntax.

**Five basic plugins** are provided as follows, and can be downloaded and used with npm.

* [**`chart`**](https://github.com/nhn/tui.editor/tree/master/plugins/chart) : A code block marked as a 'chart' will render [TOAST UI Chart](https://github.com/nhn/tui.chart).
* [**`code-syntax-highlight`**](https://github.com/nhn/tui.editor/tree/master/plugins/code-syntax-highlight) : Highlight the code block area corresponding to the language provided by [Prism.js](https://prismjs.com/).
* [**`color-syntax`**](https://github.com/nhn/tui.editor/tree/master/plugins/color-syntax) : 
Using [TOAST UI ColorPicker](https://github.com/nhn/tui.color-picker), you can change the color of the editing text with the GUI.
* [**`table-merged-cell`**](https://github.com/nhn/tui.editor/tree/master/plugins/table-merged-cell) : 
You can merge columns of the table header and body area.
* [**`uml`**](https://github.com/nhn/tui.editor/tree/master/plugins/uml) : A code block marked as an 'uml' will render [UML diagrams](http://plantuml.com/screenshot).

## 🎨 Features

* [Viewer](https://github.com/nhn/tui.editor/tree/master/docs/en/viewer.md) : Supports a mode to display only markdown data without an editing area.
* [Internationalization (i18n)](https://github.com/nhn/tui.editor/tree/master/docs/en/i18n.md) : Supports English, Dutch, Korean, Japanese, Chinese, Spanish, German, Russian, French, Ukrainian, Turkish, Finnish, Czech, Arabic, Polish, Galician, Swedish, Italian, Norwegian, Croatian + language and you can extend.
* [Widget](https://github.com/nhn/tui.editor/tree/master/docs/en/widget.md) : This feature allows you to configure the rules that replaces the string matching to a specific `RegExp` with the widget node.
* [Custom Block](https://github.com/nhn/tui.editor/tree/master/docs/en/custom-block.md) : Nodes not supported by Markdown can be defined through custom block. You can display the node what you want through writing the parsing logic with custom block.

## 🐾 Examples

* [Basic](https://nhn.github.io/tui.editor/latest/tutorial-example01-editor-basic)
* [Viewer](https://nhn.github.io/tui.editor/latest/tutorial-example04-viewer)
* [Using All Plugins](https://nhn.github.io/tui.editor/latest/tutorial-example12-editor-with-all-plugins)
* [Creating the User's Plugin](https://nhn.github.io/tui.editor/latest/tutorial-example13-creating-plugin)
* [Customizing the Toobar Buttons](https://nhn.github.io/tui.editor/latest/tutorial-example15-customizing-toolbar-buttons)
* [Internationalization (i18n)](https://nhn.github.io/tui.editor/latest/tutorial-example16-i18n)

Here are more [examples](https://nhn.github.io/tui.editor/latest/tutorial-example01-editor-basic) and play with TOAST UI Editor!


## 🌏 Browser Support

| <img src="https://user-images.githubusercontent.com/1215767/34348387-a2e64588-ea4d-11e7-8267-a43365103afe.png" alt="Chrome" width="16px" height="16px" /> Chrome | <img src="https://user-images.githubusercontent.com/1215767/34348590-250b3ca2-ea4f-11e7-9efb-da953359321f.png" alt="IE" width="16px" height="16px" /> Internet Explorer | <img src="https://user-images.githubusercontent.com/1215767/34348380-93e77ae8-ea4d-11e7-8696-9a989ddbbbf5.png" alt="Edge" width="16px" height="16px" /> Edge | <img src="https://user-images.githubusercontent.com/1215767/34348394-a981f892-ea4d-11e7-9156-d128d58386b9.png" alt="Safari" width="16px" height="16px" /> Safari | <img src="https://user-images.githubusercontent.com/1215767/34348383-9e7ed492-ea4d-11e7-910c-03b39d52f496.png" alt="Firefox" width="16px" height="16px" /> Firefox |
| :---------: | :---------: | :---------: | :---------: | :---------: |
| Yes | 11+ | Yes | Yes | Yes |


## 🔧 Pull Request Steps

TOAST UI products are open source, so you can create a pull request(PR) after you fix issues. Run npm scripts and develop yourself with the following process.

### Setup

Fork `main` branch into your personal repository. Clone it to local computer. Install node modules. Before starting development, you should check if there are any errors.

```sh
$ git clone https://github.com/{your-personal-repo}/tui.editor.git
$ npm install
$ npm run build toastmark
$ npm run test editor
```

> TOAST UI Editor uses [npm workspace](https://docs.npmjs.com/cli/v7/using-npm/workspaces/), so you need to set the environment based on [npm7](https://github.blog/2021-02-02-npm-7-is-now-generally-available/). If subversion is used, dependencies must be installed by moving direct paths per package.

### Develop

You can see your code reflected as soon as you save the code by running a server. Don't miss adding test cases and then make green rights.

#### Run snowpack-dev-server
[snowpack](https://www.snowpack.dev/) allows you to run a development server without bundling.

``` sh
$ npm run serve editor
```

#### Run webpack-dev-server
If testing of legacy browsers is required, the development server can still be run using a [webpack](https://webpack.js.org/).

``` sh
$ npm run serve:ie editor
```

#### Run test

``` sh
$ npm test editor
```

### Pull Request

Before uploading your PR, run test one last time to check if there are any errors. If it has no errors, commit and then push it!

For more information on PR's steps, please see links in the Contributing section.

## 💬 Contributing

* [Code of Conduct](https://github.com/nhn/tui.editor/blob/master/CODE_OF_CONDUCT.md)
* [Contributing Guideline](https://github.com/nhn/tui.editor/blob/master/CONTRIBUTING.md)
* [Commit Convention](https://github.com/nhn/tui.editor/blob/master/docs/COMMIT_MESSAGE_CONVENTION.md)
* [Issue Guidelines](https://github.com/nhn/tui.editor/tree/master/.github/ISSUE_TEMPLATE)


## 🍞 TOAST UI Family

- [TOAST UI Calendar](https://github.com/nhn/tui.calendar)
- [TOAST UI Chart](https://github.com/nhn/tui.chart)
- [TOAST UI Grid](https://github.com/nhn/tui.grid)
- [TOAST UI Image Editor](https://github.com/nhn/tui.image-editor)
- [TOAST UI Components](https://github.com/nhn)


## 🚀 Used By

* [NHN Dooray! - Collaboration Service (Project, Messenger, Mail, Calendar, Drive, Wiki, Contacts)](https://dooray.com)
* [UNOTES - Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=ryanmcalister.Unotes)


## 📜 License

This software is licensed under the [MIT](https://github.com/nhn/tui.editor/blob/master/LICENSE) © [NHN Cloud](https://github.com/nhn).
