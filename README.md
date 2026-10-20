# Sales Analysis

A Python script that reads sales data from a CSV file, calculates revenue for each sale, and generates reports in JSON, Excel, and CSV formats. It also prints each sale and the grand total to the console.

## Setup

Install Python 3.10 or newer, then open a terminal in the project directory.

Create and activate a virtual environment on macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies into the active environment:

```bash
python -m pip install -r requirements.txt
```

The project uses pandas for data processing and openpyxl for Excel exports. `requirements.txt` includes these packages and their dependencies.

## Run

From the project directory, with the virtual environment activated:

```bash
python analyzer.py
```

Run from this directory because the input and output paths are relative to the current working directory. The script creates `output/` automatically and replaces the report files each time it runs. Generated reports are ignored by Git.

## Input data

Edit `data/sales.csv` to analyze your own sales. Keep these column names:

| Column | Description |
| --- | --- |
| `date` | Sale date, such as `2024-01-01` |
| `product` | Product name |
| `quantity` | Numeric number of units sold |
| `price` | Numeric unit price without a currency symbol |

Example:

```csv
date,product,quantity,price
2024-01-01,Laptop,2,999.99
2024-01-01,Mouse,5,29.99
```

Use complete numeric values for quantity and price; the script does not validate input data. Console amounts use a dollar sign and two decimal places. Exported amounts remain numeric, and no currency conversion is performed.

## Calculated reports

Each sale receives a `total` equal to `quantity * price`. The summary includes:

- `sales_count`: number of sales rows, rather than distinct products or orders.
- `units_sold`: sum of quantities.
- `grand_total`: sum of all row totals.

The product report groups rows by product and calculates `units_sold` and `total_sales` for each product.

| Generated file | Contents |
| --- | --- |
| `output/sales_data.json` | An object containing `sales` (individual rows), `summary` (overall metrics), and `by_product` (product totals) |
| `output/sales_data.xlsx` | Three sheets: `Summary`, `By Product`, and `Sales` |
| `output/sales_with_totals.csv` | Original sales rows with the calculated `total` column |
| `output/sales_summary.csv` | One row containing the overall metrics |
| `output/sales_by_product.csv` | Units and revenue for each product |

The included sample contains 8 sales records from January 1–5, 2024, with 26 units sold and a grand total of **$4,749.74**.

## Project files

```text
sales-analysis/
├── analyzer.py          # Reads data, calculates totals, and exports reports
├── helpers.py           # Row-total calculation and currency formatting
├── data/
│   └── sales.csv         # Input sales data
├── output/              # Generated reports (ignored by Git)
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```
