# Power BI Project Hub

A repository template and starter kit for developing, version-controlling, and automating **Power BI** semantic models, reports, DAX logic, and ETL pipelines.

---

## 📁 Repository Structure

```text
.
├── .gitignore                      # Ignore temporary Power BI cache, backups, and Python envs
├── dax/                            # Standardized DAX formulas and business logic
│   ├── calendar_dimension.dax      # Production Date/Calendar table script
│   └── time_intelligence_kpis.dax  # Core KPI & Time Intelligence calculations (YTD, YoY, MoM)
├── power_query_m/                  # Power Query (M) scripts and reusable custom functions
│   └── calendar_function.m         # M script to generate dynamic calendar tables
├── scripts/                        # Automation scripts for Power BI REST API / Fabric
│   └── refresh_dataset.py          # Service Principal script to trigger semantic model refreshes
└── README.md                       # Project documentation and guidelines
```

---

## 🚀 Recommended Workflows

### 1. Power BI Developer Mode (`.pbip`) & Git
To version control Power BI reports and models effectively:
1. In **Power BI Desktop**, go to **File** > **Options and settings** > **Options** > **Preview features**.
2. Enable **Power BI Project (.pbip) save option**.
3. Save your file as a `.pbip` project inside this repository.
4. Power BI will generate human-readable folders:
   - `*.Dataset/` (or `*.SemanticModel/`) containing `model.bim` or TMDL definition files.
   - `*.Report/` containing `report.json` visual layout definitions.
5. Commit `.pbip` files to Git for clean peer reviews and diffs.

### 2. DAX Measure Library
- [`dax/calendar_dimension.dax`](file:///home/runner/work/my-project/my-project/dax/calendar_dimension.dax): Create a dynamic Date Dimension with fiscal periods and sorting keys.
- [`dax/time_intelligence_kpis.dax`](file:///home/runner/work/my-project/my-project/dax/time_intelligence_kpis.dax): Standardized implementations of YTD, QTD, SPLY, YoY Growth, and Moving Averages.

### 3. Power Query (M) Functions
- [`power_query_m/calendar_function.m`](file:///home/runner/work/my-project/my-project/power_query_m/calendar_function.m): Create date tables upstream in the ETL layer.

### 4. REST API Automation
- [`scripts/refresh_dataset.py`](file:///home/runner/work/my-project/my-project/scripts/refresh_dataset.py): Trigger semantic model refreshes via GitHub Actions or scheduled jobs using Azure AD / Microsoft Entra service principals.

---

## 🛠️ Next Steps & Customization

What would you like to build next?
- Add your specific business metrics and custom DAX calculations.
- Set up a sample dataset (CSV/Parquet/SQL).
- Configure a GitHub Actions workflow to run automated validation or API refreshes.
