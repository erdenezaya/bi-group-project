# Methodology

## Data Preparation and Cleaning

We brought the Global Findex 2025 CSV from the LMS into Power BI Desktop and did all the prep work using Power Query. Following the World Bank’s official glossary, we cleaned up and standardized the variable names, made sure data types were consistent, and trimmed the dataset to keep only what mattered for our research. That meant focusing on things like account ownership, digital payments, savings, borrowing, and key demographic info.

### **Field Standardisation**
To make things easier to understand and keep things consistent with previous survey waves; we replaced the confusing column headers with names that actually make sense. Here's how we renamed them:

| Original Field | New Field Name   | Description |
|----------------|------------------|--------------|
| `countrynewwb` | **Country**      | Country name |
| `codewb` | **Country_Code** | ISO/World Bank country code |
| `year` | **Year** | Survey wave year |
| `pop_adult` | **Adult_Population** | Adult population (15+) |
| `regionwb24_hi` | **Region** | World Bank region |
| `incomegroupwb24` | **Income_Group** | World Bank income classification (Low, Lower-middle, Upper-middle, High) |
| `con1` | **Own_Mobile_Phone** | Respondent owns a mobile phone |
| `account_t_d` | **Account** | Has any financial account (bank or mobile money) |
| `fiaccount_t_d` | **Fiaccount** | Has an account at a financial institution |
| `fin2_t_d` | **Debit_Card** | Owns a debit card |
| `fin24aP` | **Emergency_Fund30d** | Can raise emergency funds within 30 days |
| `borrow_any_t_d` | **Borrow_Any** | Borrowed from any source in the past 12 months |
| `save_any_t_d` | **Save_Any** | Saved money in the past 12 months |
| `fin30` | **Utility_Payment** | Made a utility payment |
| `fin17a_17a1_d` | **Saved_At_Bank_Using_Mobile** | Saved using an account or mobile platform |

### **Handling Missing Data**
The raw data used "NA" and blank fields for non-responses. In Power Query, we swapped out all "NA" entries for actual nulls; we didn’t impute anything just to avoid messing with data types or skewing any results. Since the survey coverage isn't the same across every country and year, we treated these nulls as real missing values, not zeros.
Later on, we used tooltips and summary cards in the dashboard to help users see where the data was patchy.

### **Variable Selection and Reduction**
To align with our research focus, changes in account ownership and digital financial usage across regions and income groups with a gender-gap.  We retained the following variables:
- Core classification fields: *Country, Country_Code, Year, Region, Income_Group, Adult_Population*  
- Key inclusion indicators: *Account, Fiaccount, Utility_Payment, Save_Any, Borrow_Any, Own_Mobile_Phone, Debit_Card*  

Redundant grouping fields (`group`, `group2`) and sparsely populated variables unrelated to our analysis were removed to improve model clarity and Power BI performance.

### **Transformation Workflow**
We kept track of all the changes in Power Query’s Applied Steps pane so everything’s easy to follow and repeat later.
Once we finished cleaning the data, we hit Close & Apply to bring it into Power BI’s model layer.

From there, we created a few key measures for analysis, like:

- Averages for percentage-based indicators,
- Year-over-year changes, and
- Gender gaps (measured in percentage points).

This setup gave us a clean, transparent workflow—everything’s right there in the `assign.pbix` file and ready to go.

✍️ *Contributor: Stream Huang*