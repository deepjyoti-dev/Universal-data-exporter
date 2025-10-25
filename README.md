📊 Universal Data Exporter GUI (Python)

A Python-based graphical tool to load data from multiple formats and export it to almost any popular file format: CSV, Excel, JSON, PDF, TXT, HTML, XML, Parquet, and SQLite.

Ideal for developers, data analysts, or anyone needing fast dataset conversion and export.

✨ Features
Load Data

Supports CSV, Excel (.xls / .xlsx), JSON, and TXT

Preview loaded datasets in a table within the GUI

Export Data

Export to multiple formats simultaneously:

CSV, Excel, JSON, TXT, PDF, HTML, XML, Parquet, SQLite

Choose formats via checkboxes

Specify export directory

Handles column headers and data formatting automatically

PDF Export

Generates basic PDF tables with headers and rows

SQLite Export

Export datasets as SQLite databases with customizable table names

User-Friendly GUI

Built using Tkinter

File dialogs for loading and saving data

Table preview using ttk.Treeview

🧩 Installation

Clone the repository or download the code

Install dependencies:

pip install pandas fpdf openpyxl xlrd pyarrow


Notes:

openpyxl and xlrd are required for Excel support

pyarrow is required for Parquet support

⚙️ Usage

Run the GUI:

python universal_data_exporter.py


Load a dataset

Click Load Data

Choose a CSV, Excel, JSON, or TXT file

Preview Data

The loaded data appears in a table within the GUI

Select Export Formats

Tick the checkboxes for desired formats

Export Data

Click Export Data

Choose a directory to save files

Files are saved as exported_data.{format}

Example:

Load a CSV:

Name,Age,City
Alice,25,New York
Bob,30,Los Angeles


Select CSV, Excel, JSON, PDF → Click Export Data

Generated files:

exported_data.csv
exported_data.xlsx
exported_data.json
exported_data.pdf

🗂️ Code Structure

SmartUniversalExporter – Handles data exporting logic (CSV, Excel, JSON, TXT, PDF, HTML, XML, Parquet, SQLite)

DataExporterGUI – GUI interface using Tkinter

Loads and previews data

Provides options to select formats and export directory

🧩 Requirements

Python 3.7+

Dependencies: pandas, fpdf, openpyxl, xlrd, pyarrow

🔮 Future Enhancements

Drag-and-drop support for files

Handle very large datasets with pagination in preview

Custom PDF styling (colors, fonts, borders)

Option to rename files per export format

Multi-language support

🏷️ Tags

#python #data #export #csv #excel #json #pdf #tkinter #gui #sqlite #parquet #universal
