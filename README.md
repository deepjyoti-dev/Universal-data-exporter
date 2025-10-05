# Universal-data-exporter
export data in any format
Universal Data Exporter GUI

A Python-based graphical tool that allows you to load data from multiple formats and export it to almost any popular file format, including CSV, Excel, JSON, PDF, TXT, HTML, XML, Parquet, and SQLite. Ideal for developers, data analysts, or anyone who needs to quickly convert and export datasets.

Features

Load Data

Supports CSV, Excel (.xls / .xlsx), JSON, and TXT.

Preview the loaded dataset in a table within the GUI.

Export Data

Export to multiple formats at once:

CSV, Excel, JSON, TXT, PDF, HTML, XML, Parquet, SQLite.

Choose which formats to export via checkboxes.

Specify the export directory.

Automatically handles column headers and data formatting.

PDF Export

Generates a basic PDF table with headers and rows.

SQLite Export

Export the data as a SQLite database with a customizable table name.

User-Friendly GUI

Built using Tkinter.

File dialogs for loading and saving data.

Table preview using ttk.Treeview.

Installation

Clone the repository or download the code.

Install dependencies:

pip install pandas fpdf openpyxl xlrd pyarrow


Notes:

openpyxl and xlrd are required for Excel file handling.

pyarrow is required for Parquet support.

Usage

Run the GUI:

python universal_data_exporter.py


Load a dataset

Click Load Data.

Choose a file (CSV, Excel, JSON, TXT).

Preview Data

The loaded data will appear in a table.

Select Export Formats

Tick the checkboxes for the desired export formats.

Export Data

Click Export Data.

Choose a directory to save the exported files.

Check the exported files

Files will be saved in the selected directory, named exported_data.{format}.

Example

Load a CSV with:

Name,Age,City
Alice,25,New York
Bob,30,Los Angeles


Select CSV, Excel, JSON, PDF and click Export Data.

The program will generate:

exported_data.csv
exported_data.xlsx
exported_data.json
exported_data.pdf

Code Structure

SmartUniversalExporter

Handles all the data exporting logic.

Supports CSV, Excel, JSON, TXT, PDF, HTML, XML, Parquet, SQLite.

DataExporterGUI

Handles the GUI interface using Tkinter.

Loads and previews data.

Provides options to select export formats and destination.

Requirements

Python 3.7+

Dependencies: pandas, fpdf, openpyxl, xlrd, pyarrow

Future Enhancements

Drag-and-drop support for files.

Support for very large datasets with pagination in preview.

Custom PDF styling (colors, fonts, borders).

Option to rename files for each export format.

Multi-language support.
