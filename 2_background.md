<div style="page-break-before: always;"></div>

# 2. Background

## 2.1 Dataset Overview
The Global Findex Database is the world’s only demand-side survey on financial inclusion and a leading source of data on how adults access and use financial services. The 2025 edition, its fifth, introduces the Global Findex Digital Connectivity Tracker, the world’s first globally comparable demand-side dataset on mobile phone ownership and internet use, and their contribution to financial inclusion.
 
This project’s analysis is built on the World Bank’s Global Findex Database (2025) a huge source of survey data that looks at financial inclusion and how people use financial services around the world. The dataset includes thousands of responses from individuals in different countries, and it covers a wide range of variables related to things like:

- **Financial Behavior** – `Save_Any`, `Borrow_Any`, `Saved_At_Bank_Using_Mobile`  
- **Financial access** –  `Account`, `Fiaccount`, `Debit_Card`  
- **Regional/temporal dimensions** – `country`, `region`, `year of survey`.  
- **Financial Application Usage** - `Utility_Payment`, `Emergency_Fund30d`
- **Demographics** – `age`, `gender`, `education`, `income quintiles`.

Each column in the dataset maps to a survey question or a classification variable, and every row represents either an individual response or a rolled-up summary. There's a ton of depth here, which means we can look at the basics like averages and percentages but also dig into comparisons across different countries and groups.  

As the only global source of comparable demand-side data, the Global Findex enables cross-country and cross-regional analysis of how adults use mobile phones, the internet, and financial accounts to access digital information, save, borrow, make payments, and manage their financial well-being.

---

## 2.2 Literature Review

### **Definition of Financial Inclusion**
Financial inclusion refers to the access to and use of formal financial services by households and firms. According to the IMF (2015), financial inclusion serves as a policy tool to improve livelihoods, reduce poverty, and promote economic development. Similarly, the BIS (2015) defines it as access to and usage of financial services that meet users’ needs in a sustainable and responsible manner.

### **Dimensions and Measurement of Financial Inclusion**
Numerous studies and international organizations have developed frameworks to measure financial inclusion. Allen et al. (2016) explored the individual and country-level determinants of financial inclusion, focusing on financial access, financial use, and the barriers or costs that hinder participation. They argue that account ownership and account usage represent the core indicators of financial inclusion, as they directly reflect individuals’ ability to engage with formal financial institutions. The OECD (2022), in its Toolkit for Measuring Financial Literacy and Financial Inclusion, emphasized that the measurement of financial inclusion should consider multiple aspects, including access, usage, and behavioral or attitudinal components such as financial knowledge and attitudes toward money management. Sharma and Changkakati (2022) examined financial inclusion using three key dimensions—access, usage, and quality—and linked these to the United Nations Sustainable Development Goals (SDGs), highlighting the broader role of inclusion in achieving equitable growth. In addition, the G20 Financial Inclusion Indicators (2015) framework explicitly defines three dimensions of financial inclusion: access to financial services, usage of financial services, and the quality of products and service delivery. Taken together, these frameworks provide a coherent view that financial inclusion can be conceptualized through three main dimensions: access, usage, and enabler (or quality).
In the 2025 Global Findex dataset, there is a particular emphasis on digital financial inclusion, reflecting the growing importance of digital connectivity in promoting financial participation. The dataset highlights variables such as mobile phone ownership and internet use, which represent the digital access and usage aspects of inclusion. Therefore, this study conceptualizes financial inclusion as a three-dimensional construct comprising digital inclusion, financial access, and financial behavior. These dimensions represent the progressive stages of inclusion—from the availability of digital tools, to access to formal financial services, and finally, to active engagement in financial activities.

### **Digital Inclusion**
According to the OECD (2021), digital inclusion encompasses both digital access — the availability and affordability of ICT — and digital use, referring to the ability and frequency of engaging with digital tools. The ITU (2022) further highlights that digital access and digital use are the two key pillars of digital inclusion and readiness. Jia and Kanagaretnam (2024) examined the ethical and social dimensions of digital inclusion and found that it plays a critical role in advancing financial inclusion, especially in vulnerable and underserved regions. Their findings suggest that digital inclusion empowers financial service providers and other stakeholders to better fulfill their ethical and social responsibilities toward marginalized populations.

### **Financial Access**
As discussed by Birkenmaier et al. (2019), financial access broadly refers to the ability of all individuals to obtain and use safe, affordable, and appropriate financial products and services. It promotes financial well-being at both household and societal levels by ensuring access to instruments such as savings accounts, credit cards, mortgages, and loans. However, many people remain unbanked or underbanked, relying on alternative financial services, which hinders full financial inclusion.

### **Financial Behavior**
Financial behavior reflects the attitudes and actions individuals take in managing their finances — including budgeting, spending, saving, investing, and financial planning. Previous research shows that positive perceptions of electronic payments can significantly enhance behavioral intentions and foster greater financial inclusion. Overall, financial behavior demonstrates how individuals plan for the future, control their expenditures, and build saving habits that influence long-term financial decision-making and well-being.

<div style="page-break-before: always;"></div>

## 2.3 Research Question(s)
For this project, we will investigate the following questions:

- How did account owernership and digital payment use change from 2011 to 2025 across regions and income groups, and where do gender gaps persist or narrow?
  **Research Focus:**
     - How does regions, income groups, and gender gaps and period of time (years) = x variables influence account ownership (y variable)
     -  How does regions, income groups, and gender gaps and period of time (years) = x variables influence digital payment use (y variable)"

These questions tie directly into the unit’s learning goals, and they’ll help shape how we build the dashboard and make sense of the results later on.

✍️ *Contributor: Zaya, Jinshu* 
