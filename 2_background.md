## 2. Background

### 2.1 Dataset Overview
The analysis in this project is based on the World Bank Global Findex Database (2025) which provides cross-country survey data on financial inclusion and the use of financial services.  
The dataset contains thousands of observations, each representing responses from individuals across multiple countries, and includes variables relating to:

- **Demographics** – age, gender, education, income quintiles.  
- **Financial access** – account ownership, savings, borrowing, digital payments.  
- **Regional/temporal dimensions** – country, region, year of survey.  

Each column (attribute) corresponds to a survey indicator or classification variable, while each row represents a respondent or aggregated survey record. The richness of the dataset allows for both descriptive statistics and deeper comparisons across countries and groups.  

A **data dictionary** has been prepared (see Appendix) to explain each variable and its role in the analysis.

---

### 2.2 Context of Financial Inclusion
Financial inclusion is increasingly recognised as a driver of economic growth and poverty reduction It enables individuals and businesses to access useful and affordable financial products and services, such as banking, credit, savings, and insurance.  
Global Findex surveys highlight disparities across:

- **Regions** – developing vs. developed economies.  
- **Gender** – persistent gaps in account ownership and credit access.  
- **Income levels** – exclusion of low-income households from formal finance.  

This context underscores the importance of understanding which factors drive or hinder inclusion, which is the main focus of this assignment.

---

### 2.3 Research Question(s)
For this project, we will investigate the following guiding question(s):

- **Primary Question:**  
  *What demographic and regional factors influence account ownership and digital payment usage in the 2025 Global Findex dataset?*

- **Secondary Explorations:**  
  - How does gender influence access to financial services across regions?  
  - What role does income quintile play in determining financial inclusion outcomes?  
  - Are there observable differences between developing and developed economies?  

These questions are aligned with the unit learning outcomes and will guide both the dashboard design and the interpretation of insights in later sections.

---

### 2.4 Assumptions
To scope the analysis, we assume:  
- Only the dataset provided via LMS will be used (not external downloads).  
- Missing values represent either *non-response* or *no data collected* in that country/year.  
- Cleaning steps (e.g., removing duplicates, handling nulls) will not distort the representativeness of the dataset.  

These assumptions are explicitly stated to maintain transparency and reproducibility.
