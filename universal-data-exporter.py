# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 10:25:44 2025

@author: deepj
"""

import pandas as pd
import json
from fpdf import FPDF
import sqlite3
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class SmartUniversalExporter:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.df = data
        elif isinstance(data, list):
            self.df = pd.DataFrame(data)
        elif isinstance(data, dict):
            self.df = pd.DataFrame([data])
        else:
            raise ValueError("Unsupported data type. Must be DataFrame, list of dicts, or dict.")

    def export(self, file_paths, table_name=None, sql_connection=None):
        for file_path in file_paths:
            ext = os.path.splitext(file_path)[1].lower().replace(".", "")
            self._export_by_format(ext, file_path, table_name, sql_connection)

    def _export_by_format(self, fmt, file_path, table_name=None, sql_connection=None):
        fmt = fmt.lower()
        try:
            if fmt == "csv":
                self.df.to_csv(file_path, index=False)
            elif fmt in ["xlsx", "xls"]:
                self.df.to_excel(file_path, index=False)
            elif fmt == "json":
                self.df.to_json(file_path, orient='records', indent=4)
            elif fmt == "txt":
                with open(file_path, "w") as f:
                    f.write(self.df.to_string(index=False))
            elif fmt == "pdf":
                self._export_pdf(file_path)
            elif fmt == "html":
                self.df.to_html(file_path, index=False)
            elif fmt == "xml":
                self._export_xml(file_path)
            elif fmt == "parquet":
                self.df.to_parquet(file_path, index=False)
            elif fmt in ["db", "sqlite"]:
                if sql_connection is None:
                    sql_connection = sqlite3.connect(file_path)
                if table_name is None:
                    table_name = "table1"
                self.df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
                if sql_connection:
                    sql_connection.close()
            else:
                print(f"Format {fmt} not supported. Skipping {file_path}")
                return
            print(f"Data exported successfully to {file_path}")
        except Exception as e:
            print(f"Error exporting to {file_path}: {e}")

    def _export_pdf(self, file_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        col_width = pdf.w / (len(self.df.columns) + 1)
        row_height = pdf.font_size * 1.5

        for col in self.df.columns:
            pdf.cell(col_width, row_height, str(col), border=1)
        pdf.ln(row_height)

        for i in range(len(self.df)):
            for col in self.df.columns:
                pdf.cell(col_width, row_height, str(self.df.iloc[i][col]), border=1)
            pdf.ln(row_height)
        pdf.output(file_path)

    def _export_xml(self, file_path):
        def row_to_xml(row):
            xml = "  <row>\n"
            for col in self.df.columns:
                xml += f"    <{col}>{row[col]}</{col}>\n"
            xml += "  </row>\n"
            return xml

        with open(file_path, "w") as f:
            f.write("<data>\n")
            for i in range(len(self.df)):
                f.write(row_to_xml(self.df.iloc[i]))
            f.write("</data>\n")


# -------------------- GUI -------------------- #
class DataExporterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Universal Data Exporter")
        master.geometry("800x600")

        self.data = None
        self.exporter = None

        # Buttons
        self.load_btn = tk.Button(master, text="Load Data", command=self.load_data)
        self.load_btn.pack(pady=10)

        self.export_btn = tk.Button(master, text="Export Data", command=self.export_data)
        self.export_btn.pack(pady=10)

        # Format checkboxes
        self.formats = ["CSV", "Excel", "JSON", "TXT", "PDF", "HTML", "XML", "Parquet", "SQLite"]
        self.format_vars = {}
        for fmt in self.formats:
            var = tk.IntVar(value=1)
            chk = tk.Checkbutton(master, text=fmt, variable=var)
            chk.pack(anchor="w")
            self.format_vars[fmt] = var

        # Table preview
        self.tree = ttk.Treeview(master)
        self.tree.pack(expand=True, fill='both', pady=10)

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[
            ("All Files", "*.*"),
            ("CSV", "*.csv"),
            ("Excel", "*.xlsx;*.xls"),
            ("JSON", "*.json"),
            ("TXT", "*.txt")
        ])
        if not file_path:
            return
        ext = os.path.splitext(file_path)[1].lower()
        try:
            if ext == ".csv":
                self.data = pd.read_csv(file_path)
            elif ext in [".xlsx", ".xls"]:
                self.data = pd.read_excel(file_path)
            elif ext == ".json":
                self.data = pd.read_json(file_path)
            elif ext == ".txt":
                self.data = pd.read_csv(file_path, delimiter="\t")
            else:
                messagebox.showerror("Error", f"Unsupported file format: {ext}")
                return
            self.exporter = SmartUniversalExporter(self.data)
            self.show_preview()
            messagebox.showinfo("Success", "Data loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

    def show_preview(self):
        # Clear previous data
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(self.data.columns)
        self.tree["show"] = "headings"
        for col in self.data.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        for _, row in self.data.iterrows():
            self.tree.insert("", "end", values=list(row))

    def export_data(self):
        if not self.exporter:
            messagebox.showerror("Error", "No data loaded!")
            return

        save_dir = filedialog.askdirectory()
        if not save_dir:
            return

        file_paths = []
        for fmt, var in self.format_vars.items():
            if var.get() == 1:
                ext = fmt.lower() if fmt != "Excel" else "xlsx"
                filename = os.path.join(save_dir, f"exported_data.{ext}")
                file_paths.append(filename)

        try:
            self.exporter.export(file_paths, table_name="exported_table")
            messagebox.showinfo("Success", "Data exported successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Export failed: {e}")


# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = DataExporterGUI(root)
    root.mainloop()
