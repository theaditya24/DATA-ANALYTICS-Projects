# 📊 Data Analytics Projects

> A growing portfolio of **end-to-end Data Analytics, Business Intelligence, SQL, Python, and Power BI projects** focused on transforming raw data into meaningful insights and business decisions.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge\&logo=sqlite\&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge\&logo=powerbi\&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge\&logo=postgresql\&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge\&logo=jupyter\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)

---

## 👋 About This Repository

Welcome to my **Data Analytics Portfolio**.

This repository contains practical, end-to-end analytics projects designed to demonstrate how raw data can be transformed into **clean datasets, analytical models, interactive dashboards, and actionable business insights**.

The projects cover multiple areas including:

* 📈 Business & Sales Analytics
* 👥 Customer Analytics
* 💰 Salary & Compensation Analytics
* 🚕 Operations Analytics
* ☕ Retail Analytics
* 🌦️ API & Weather Analytics
* 🗄️ SQL & Data Warehouse Analytics
* 📊 Business Intelligence & Dashboarding

Rather than focusing only on visualization, these projects follow a structured analytical workflow:

```text
Raw Data
   ↓
Data Collection
   ↓
Data Cleaning
   ↓
Data Transformation
   ↓
Exploratory Data Analysis
   ↓
SQL / Statistical Analysis
   ↓
Data Modeling
   ↓
Dashboard / Report / Application
   ↓
Business Insights
   ↓
Recommendations
```

---

# 🚀 Projects

| #  | Project                                                                         | Domain               | Primary Tools                 |
| -- | ------------------------------------------------------------------------------- | -------------------- | ----------------------------- |
| 01 | [Customer Shopping Behaviour Analysis](#1-customer-shopping-behaviour-analysis) | Customer Analytics   | Python, MySQL, Power BI       |
| 02 | [Global Data Science Salary Dashboard](#2-global-data-science-salary-dashboard) | Salary Analytics     | Python, Pandas, Power BI      |
| 03 | [Ride Bookings Analysis](#3-ride-bookings-analysis)                             | Operations Analytics | Power BI, Power Query, DAX    |
| 04 | [Starbucks Analysis Dashboard](#4-starbucks-analysis-dashboard)                 | Retail Analytics     | PostgreSQL, Next.js, Power BI |
| 05 | [Weather Dashboard](#5-weather-dashboard)                                       | API Analytics        | Power BI, Power Query, Excel  |
| 06 | [SQL Data Analytics Project](#6-sql-data-analytics-project)                     | SQL Analytics        | SQL Server, T-SQL             |
| 07 | [Banking Analysis](#7-banking-analysis)                                         | Financial Analytics  | SQL, Power BI, Python         |

---

# 1. 🛍️ Customer Shopping Behaviour Analysis

### Overview

An end-to-end customer analytics project focused on understanding **customer purchasing behaviour, product performance, customer loyalty, discounts, payment methods, shipping preferences, and customer satisfaction**.

The project combines Python-based data analysis, SQL querying, and Power BI dashboard development.

### Key Business Questions

* Which customer segments generate the most revenue?
* Which product categories perform best?
* How does customer loyalty affect purchasing behaviour?
* What impact do discounts have on sales?
* Which payment methods are most frequently used?
* How do subscription and shipping preferences vary?
* Which customer segments have the highest purchase frequency?
* What seasonal patterns exist in customer purchases?

### Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Exploratory Data Analysis
     ↓
SQL Analysis
     ↓
Power BI Data Modeling
     ↓
DAX Measures
     ↓
Interactive Dashboard
     ↓
Business Insights
```

### Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* MySQL
* SQL
* Power BI
* DAX
* Jupyter Notebook

👉 **[View Project →](./Customer%20Shopping%20Behaviour%20Analysis)**

---

# 2. 💼 Global Data Science Salary Dashboard

### Overview

A salary analytics project analyzing the **global Data Science job market** and comparing compensation across countries, experience levels, job roles, and work arrangements.

A particular focus is placed on understanding **India vs global salary trends**.

### Key Areas

* Salary distribution
* Experience-level analysis
* Job role comparison
* India vs Global salary comparison
* Remote work analysis
* Geographic salary trends
* Highest-paying roles
* Salary progression with experience

### Workflow

```text
Raw Salary Dataset
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Data Transformation
        ↓
Power BI Data Preparation
        ↓
Dashboard Development
        ↓
Salary Insights
```

### Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Power BI
* DAX
* Jupyter Notebook

👉 **[View Project →](./Global-Data-Science-Salary-Dashboard)**

---

# 3. 🚕 Ride Bookings Analysis

### Overview

An end-to-end Power BI project analyzing **150,000 ride bookings across 2024** to understand booking performance, revenue, vehicle utilization, cancellations, and failed rides.

The report contains multiple analytical pages covering operational and business KPIs.

### Key Metrics & Analysis

* Total bookings
* Completed bookings
* Revenue
* Completion rate
* Booking trends
* Vehicle type performance
* Customer cancellations
* Driver cancellations
* Failed rides
* Payment methods
* Revenue distribution
* Customer distribution

### Dashboard Structure

```text
Home
 │
 ├── Overview
 │
 ├── Vehicle Type Analysis
 │
 └── Cancellations & Failed Rides
```

### Workflow

```text
150K Ride Bookings
        ↓
Power Query
        ↓
Data Cleaning
        ↓
Data Modeling
        ↓
DAX Measures
        ↓
Power BI Dashboard
        ↓
Operational Insights
```

### Technologies

* Power BI Desktop
* Power Query
* DAX
* JSON Theme
* Data Modeling

👉 **[View Project →](./Riding%20Analysis)**

---

# 4. ☕ Starbucks Analysis Dashboard

### Overview

A retail analytics project combining a **PostgreSQL-backed web application** with a **Power BI sales dashboard**.

The project demonstrates how transactional data can support both **real-time operational monitoring** and **executive-level business reporting**.

### Starbucks Sales Manager

The web application provides:

* Real-time sales KPIs
* Order volume
* Average Order Value
* Top-selling item
* Searchable transactions
* Filtering capabilities
* PostgreSQL-backed data

### Power BI Report

The Power BI report analyzes:

* Revenue by hour
* Average spend by hour
* Units sold
* Order volume
* Customer metrics
* Quantity metrics
* Sales performance

### Architecture

```text
Transactional Data
       ↓
   PostgreSQL
       ↓
  SQL Queries
       ↓
 ┌───────────────┐
 │               │
 ▼               ▼
Next.js       Power BI
Web App       Dashboard
 │               │
 ▼               ▼
Operations    Reporting
```

### Technologies

* Next.js
* React
* PostgreSQL
* SQL
* Power BI
* Tailwind CSS

👉 **[View Project →](./Starbucks%20Analysis%20Dashboard)**

---

# 5. 🌦️ Weather Dashboard

### Overview

An interactive weather analytics dashboard that integrates **API-based weather data** and transforms it into an interactive Power BI experience.

The dashboard provides both current conditions and forecast-based analysis.

### Key Features

* Current temperature
* Weather conditions
* Daily forecast
* Hourly forecast
* Wind information
* Humidity
* Weather trends
* Interactive filtering

### Workflow

```text
Weather API
     ↓
API Response
     ↓
Data Transformation
     ↓
Structured Dataset
     ↓
Power BI
     ↓
Interactive Dashboard
```

### Technologies

* Power BI
* Power Query
* Weather API
* Microsoft Excel
* Data Transformation

👉 **[View Project →](./Weather%20Dashboard)**

---

# 6. 🗄️ SQL Data Analytics Project

### Overview

A comprehensive SQL analytics project focused on **data exploration, analytical SQL, segmentation, ranking, trends, performance analysis, and reporting** using a layered data warehouse.

The project demonstrates practical SQL techniques used in real-world analytical environments.

### Analysis Areas

* Database exploration
* Dimension exploration
* Date-range analysis
* Measures exploration
* Magnitude analysis
* Ranking analysis
* Change-over-time analysis
* Cumulative analysis
* Performance analysis
* Customer segmentation
* Product segmentation
* Part-to-whole analysis
* Customer reporting
* Product reporting

### SQL Concepts Demonstrated

```text
SELECT
WHERE
GROUP BY
HAVING
ORDER BY
JOINs
Subqueries
CTEs
Window Functions
CASE Statements
Aggregations
Date Functions
Analytical Queries
```

### Workflow

```text
Data Warehouse
      ↓
Database Exploration
      ↓
Data Analysis
      ↓
Trend & Ranking Analysis
      ↓
Segmentation
      ↓
Performance Analysis
      ↓
Customer & Product Reports
```

### Technologies

* SQL Server
* T-SQL
* Data Warehouse
* Analytical SQL

> This project was completed as course-based practice following the Data With Baraa SQL Data Analytics course. Original educational materials and attribution are maintained within the project folder.

👉 **[View Project →](./SQL%20Project)**

---

# 7. 🏦 Banking Analysis

### Overview

A banking analytics project focused on extracting meaningful insights from banking-related data using analytical techniques and business intelligence tools.

The project focuses on understanding customer, transaction, and financial patterns to support data-driven decision-making.

### Focus Areas

* Customer analysis
* Banking transactions
* Financial metrics
* Customer segmentation
* Transaction trends
* Business performance
* KPI analysis
* Interactive reporting

👉 **[View Project →](./Banking%20Analysis)**

---

# 🧠 Skills Demonstrated

These projects collectively demonstrate practical knowledge across the complete analytics lifecycle.

## 📊 Data Analytics

* Data Cleaning
* Data Transformation
* Exploratory Data Analysis
* Feature Engineering
* Data Validation
* Statistical Analysis
* Business Analysis
* KPI Development
* Insight Generation

## 🐍 Python

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Data Cleaning
* EDA
* Feature Engineering

## 🗄️ SQL

* SELECT / WHERE
* GROUP BY / HAVING
* JOINs
* Subqueries
* CTEs
* Window Functions
* Aggregations
* CASE Statements
* Date Functions
* Ranking
* Segmentation
* Trend Analysis
* Reporting Queries

## 📈 Power BI

* Power Query
* Data Modeling
* DAX
* Calculated Columns
* Measures
* KPI Cards
* Slicers
* Interactive Reports
* Dashboard Design
* Custom Themes
* Business Intelligence

## 🛢️ Databases

* MySQL
* PostgreSQL
* SQL Server

## 🌐 Web & APIs

* Next.js
* React
* Tailwind CSS
* REST APIs
* API Data Integration

## 🛠️ Other Tools

* Microsoft Excel
* Git
* GitHub
* Jupyter Notebook
* Power Query

---

# 🏗️ End-to-End Analytics Framework

The projects in this portfolio generally follow a structured approach:

```text
                 ┌──────────────┐
                 │   RAW DATA   │
                 └──────┬───────┘
                        ↓
                Data Collection
                        ↓
                 Data Cleaning
                        ↓
                Transformation
                        ↓
               Exploratory Analysis
                        ↓
                 SQL / Analysis
                        ↓
                  Data Modeling
                        ↓
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
       Power BI       Reports       Web Apps
          ↓             ↓             ↓
          └─────────────┼─────────────┘
                        ↓
                Business Insights
                        ↓
                  Recommendations
```

The objective is not simply to build dashboards, but to understand **why something is happening, what the data is telling us, and how those insights can support better decisions**.

---

# 📁 Repository Structure

```text
DATA-ANALYTICS-Projects/
│
├── Banking Analysis/
│
├── Customer Shopping Behaviour Analysis/
│
├── Global-Data-Science-Salary-Dashboard/
│
├── Riding Analysis/
│
├── Starbucks Analysis Dashboard/
│
├── Weather Dashboard/
│
├── SQL Project/
│
├── .gitignore
│
└── README.md
```

Each project folder contains its own datasets, notebooks, SQL scripts, Power BI files, documentation, or application source code where applicable.

---

# 🛠️ Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/theaditya24/DATA-ANALYTICS-Projects.git
```

## 2. Navigate to the Repository

```bash
cd DATA-ANALYTICS-Projects
```

## 3. Choose a Project

```bash
cd "Customer Shopping Behaviour Analysis"
```

Each project may have different requirements. Check the project's individual `README.md` before running notebooks, SQL scripts, dashboards, or applications.

---

# 📌 Project Highlights

### 🛍️ Customer Analytics

Analyzes customer purchasing behaviour to identify product, customer, loyalty, discount, and revenue patterns.

### 💼 Salary Analytics

Explores global Data Science compensation and compares salary trends across roles, experience levels, and geographic markets.

### 🚕 Operations Analytics

Analyzes 150K ride bookings to understand completion rates, vehicle performance, revenue, cancellations, and failed rides.

### ☕ Retail Analytics

Combines PostgreSQL, Next.js, and Power BI to demonstrate both operational monitoring and executive sales reporting.

### 🌦️ API Analytics

Demonstrates API integration, data transformation, and interactive weather visualization.

### 🗄️ SQL Analytics

Demonstrates analytical SQL techniques including ranking, segmentation, trends, cumulative analysis, and reporting.

### 🏦 Banking Analytics

Applies data analysis and visualization techniques to banking and financial datasets.

---

# 📚 What I Am Building Through These Projects

This portfolio is focused on developing the skills required for real-world **Data Analyst / Business Intelligence roles**, including:

* Turning business questions into analytical problems
* Working with raw and messy datasets
* Cleaning and transforming data
* Writing efficient analytical SQL
* Performing exploratory data analysis
* Building data models
* Creating meaningful KPIs
* Designing professional dashboards
* Communicating insights through data storytelling
* Connecting databases with analytical applications
* Working with APIs
* Translating findings into actionable business recommendations

---

# 🔮 Future Projects

This repository will continue to grow with projects covering areas such as:

* 📈 Sales Analytics
* 👥 Customer Churn Analysis
* 💳 Financial Analytics
* 👨‍💼 HR Analytics
* 📣 Marketing Analytics
* 🚚 Supply Chain Analytics
* 🛒 E-commerce Analytics
* 📊 Business Performance Analytics
* 💰 Financial Dashboarding
* 🧑‍💻 Advanced SQL Analytics
* 🤖 Machine Learning for Analytics

---

# 👨‍💻 About Me

**Aditya Raj**

B.Tech Computer Science & Engineering

**Aspiring Data Analyst | Python | SQL | Power BI | Data Visualization**

I enjoy working with data to uncover patterns, solve business problems, and build analytical solutions that turn complex datasets into understandable insights.

---

# 🔗 Connect With Me

* **GitHub:** [@theaditya24](https://github.com/theaditya24)

---

# ⭐ Support

If you find these projects useful or interesting, consider giving the repository a ⭐.

Your feedback, suggestions, and contributions are always welcome.

---

<p align="center">
  <b>Turning Data into Insights. Turning Insights into Decisions. 🚀</b>
</p>
