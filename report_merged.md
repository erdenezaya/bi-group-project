# INMT5526: Business Intelligence – Group Report
- **Dataset:** World Bank Global Findex Database 2025  
- **Tool:** Power BI Desktop  
- **Word Count Target:** ~3000 words (≈10 pages)  
- **Group Members:** Group of 4 members
    - Erdenezaya Batnasan (24448191)
    - Stream Huang (23011392)
    - Gideon Tan (24578622)
    - Jinshu Zhang (23773086)
## Table of Contents

- [1. Introduction](#1-introduction)
    - [Purpose of the Report](#purpose-of-the-report)
    - [Importance of Financial Inclusion](#importance-of-financial-inclusion)
    - [Overview of Approach](#overview-of-approach)
- [2. Background](#2-background)
  - [2.1 Dataset Overview](#21-dataset-overview)
  - [2.2 Context of Financial Inclusion](#22-context-of-financial-inclusion)
  - [2.3 Research Question(s)](#23-research-questions)
  - [2.4 Assumptions](#24-assumptions)
- [Discussion](#discussion)
  - [Key Dimensions of Financial Inclusion (Accounts, Payments, Savings, Borrowing)](#key-dimensions-of-financial-inclusion-accounts-payments-savings-borrowing)

<div style="page-break-before: always;"></div>

# 1. Introduction
For this project, we’re diving into the World Bank’s Global Findex 2025 dataset to explore financial inclusion on a global scale. Our main focus is to tackle a specific research questions as suggested below by group members, and see what the data reveals:

- like the gender gap in access to financial services.
- digital device mobile 
- salary across the world

We’ll start by cleaning and transforming the dataset in Power BI, then pick out a few key indicators that really highlight trends across countries, regions, and income levels. From there, we’ll build an interactive dashboard that makes it easy to visualize those patterns and dig deeper into the insights.

Alongside the dashboard, we’re putting together a written report that walks through our process, explains what we found, and reflects on what it all means. We’ve also included extra materials in the appendix like a data dictionary and some dashboard screenshot to keep everything transparent and easy to follow.

The workflow of group projects:
- Explore dataset → shortlist variables.
- Define storyline / research question.
- Clean dataset & rename key columns.
- Build visuals in Power BI.
- Draft report sections in Markdown.
- Merge, polish, and export PDF.
- Submit deliverables.

### Purpose of the Report
Explain the goals of the assignment and why financial inclusion matters globally.

### Importance of Financial Inclusion
- Role in economic development  
- Relevance for policymakers and organisations  

### Overview of Approach
- Dataset: World Bank Global Findex 2025  
- Tool: Power BI Desktop  
- Deliverables: Dashboard + Report  

✍️ *Contributor: Zaya*


<div style="page-break-before: always;"></div>

# 2. Background

## 2.1 Dataset Overview
The analysis in this project is based on the World Bank Global Findex Database (2025) which provides cross-country survey data on financial inclusion and the use of financial services.  
The dataset contains thousands of observations, each representing responses from individuals across multiple countries, and includes variables relating to:

- **Demographics** – age, gender, education, income quintiles.  
- **Financial access** – account ownership, savings, borrowing, digital payments.  
- **Regional/temporal dimensions** – country, region, year of survey.  

Each column (attribute) corresponds to a survey indicator or classification variable, while each row represents a respondent or aggregated survey record. The richness of the dataset allows for both descriptive statistics and deeper comparisons across countries and groups.  

A **data dictionary** has been prepared (see Appendix) to explain each variable and its role in the analysis.

---

## 2.2 Context of Financial Inclusion
Financial inclusion is increasingly recognised as a driver of economic growth and poverty reduction It enables individuals and businesses to access useful and affordable financial products and services, such as banking, credit, savings, and insurance.  
Global Findex surveys highlight disparities across:

- **Regions** – developing vs. developed economies.  
- **Gender** – persistent gaps in account ownership and credit access.  
- **Income levels** – exclusion of low-income households from formal finance.  

This context underscores the importance of understanding which factors drive or hinder inclusion, which is the main focus of this assignment.

---

## 2.3 Research Question(s)
For this project, we will investigate the following guiding question(s):

- **Primary Question:**  
  *What demographic and regional factors influence account ownership and digital payment usage in the 2025 Global Findex dataset?*

- **Secondary Explorations:**  
  - How does gender influence access to financial services across regions?  
  - What role does income quintile play in determining financial inclusion outcomes?  
  - Are there observable differences between developing and developed economies?  

These questions are aligned with the unit learning outcomes and will guide both the dashboard design and the interpretation of insights in later sections.

---

## 2.4 Assumptions
To scope the analysis, we assume:  
- Only the dataset provided via LMS will be used (not external downloads).  
- Missing values represent either *non-response* or *no data collected* in that country/year.  
- Cleaning steps (e.g., removing duplicates, handling nulls) will not distort the representativeness of the dataset.  

These assumptions are explicitly stated to maintain transparency and reproducibility.








<div style="page-break-before: always;"></div>

# Discussion

## Key Dimensions of Financial Inclusion (Accounts, Payments, Savings, Borrowing)

![alt text](image-2.png)

We uncovered a few key takeaways during the analysis:

Account ownership has definitely grown over time from 2011 to 2025 with noticeable jumps in places like Sub-Saharan Africa and South Asia. It's clear that financial services are reaching more people, slowly but surely.

The gender gap still exists, though there’s some good news. Men still tend to have more accounts than women, but in a few regions, that gap is starting to close. Progress, but uneven.

Digital payments are really taking off in areas like East Asia & Pacific and Europe & Central Asia. That said, regions like Sub-Saharan Africa and especially rural populations are still lagging behind when it comes to digital adoption.

Savings and borrowing habits differ a lot depending on income. Wealthier groups (top 60%) are more likely to save, while poorer households often rely on informal borrowing. Not ideal, but not surprising either.

Education and work status seem to play a huge role. People with at least secondary education, or who are active in the labor force, are far more likely to have an account.

Overall, we’re seeing movement toward broader financial inclusion, but the picture isn’t entirely rosy. Gaps still exist especially for women, low-income groups, and rural communities. If the goal is truly universal access, targeted policies will be key to removing the specific barriers these groups face.





