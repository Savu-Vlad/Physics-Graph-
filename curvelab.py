import tkinter as tk
from tkinter import filedialog, messagebox
from io import StringIO
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import ttkbootstrap as tb
from ttkbootstrap.constants import *

# ------- Data helpers -------

def _extract_labels(col0, col1):
    x_name, y_name = str(col0), str(col1)
    if x_name.strip().isdigit() or x_name.strip().lower() in {"col0", "column1"}:
        x_name = "x"
    if y_name.strip().isdigit() or y_name.strip().lower() in {"col1", "column2"}:
        y_name = "y"
    return x_name, y_name

def load_csv(path: str):
    df = pd.read_csv(path, sep=None, engine="python", comment="#")
    if df.shape[1] < 2:
        raise ValueError("CSV must have at least two columns (x and y).")
    x_name, y_name = _extract_labels(df.columns[0], df.columns[1])
    x = pd.to_numeric(df.iloc[:, 0], errors="coerce")
    y = pd.to_numeric(df.iloc[:, 1], errors="coerce")
    clean = pd.DataFrame({"x": x, "y": y}).dropna()
    if len(clean) < 2:
        raise ValueError("Need at least two numeric (x,y) rows after cleaning.")
    return clean["x"].to_numpy(float), clean["y"].to_numpy(float), x_name, y_name

def parse_pasted(text: str):
    if not text.strip():
        raise ValueError("Paste some data first (two columns).")
    df = pd.read_csv(StringIO(text.strip()), sep=r"[,\s]+", engine="python", comment="#")
    if df.shape[1] < 2:
        raise ValueError("Need at least two columns (x and y).")
    x_name, y_name = _extract_labels(df.columns[0], df.columns[1])
    x = pd.to_numeric(df.iloc[:, 0], errors="coerce")
    y = pd.to_numeric(df.iloc[:, 1], errors="coerce")
    clean = pd.DataFrame({"x": x, "y": y}).dropna()
    if len(clean) < 2:
        raise ValueError("Need at least two numeric (x,y) rows after cleaning.")
    return clean["x"].to_numpy(float), clean["y"].to_numpy(float), x_name, y_name

def save_csv_dialog(x, y):
    if x is None or y is None:
        messagebox.showwarning("CurveLab", "No data to save yet.")
        return
    path = filedialog.asksaveasfilename(
        title="Save data as CSV",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if not path:
        return
    pd.DataFrame({"x": x, "y": y}).to_csv(path, index=False)
    messagebox.showinfo("CurveLab", f"Saved CSV → {Path(path).name}")

# ------- Fit & plot -------

def fit_and_plot(x, y, order, xlabel, ylabel):
    if order < 1:
        raise ValueError("Order must be >= 1.")
    coeffs = np.polyfit(x, y, order)
    p = np.poly1d(coeffs)

    xx = np.linspace(np.min(x), np.max(x), 400)
    yy = p(xx)

    plt.scatter(x, y, label="Data")
    plt.plot(xx, yy, label=f"Fit (order {order})")
    plt.xlabel(xlabel or "x")
    plt.ylabel(ylabel or "y")
    plt.title("Polynomial Regression")
    plt.grid(True)
    plt.legend()
    plt.show()

    yhat = p(x)
    ss_res = np.sum((y - yhat) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot != 0 else float("nan")

    eq = str(np.poly1d(coeffs))
    print("\nEquation of best fit:")
    print(eq)
    print(f"R² = {r2:.6g}")
    return r2, eq

# ------- GUI -------

x_data = y_data = None
x_label = y_label = None

def browse_csv():
    path = filedialog.askopenfilename(
        title="Select CSV",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if path:
        csv_path.set(path)

def load_clicked():
    global x_data, y_data, x_label, y_label
    if not csv_path.get():
        messagebox.showwarning("CurveLab", "Select a CSV first.")
        return
    try:
        x_data, y_data, x_label, y_label = load_csv(csv_path.get())
        status.set(f"Loaded {len(x_data)} rows ({x_label} vs {y_label})")
    except Exception as e:
        messagebox.showerror("CurveLab", str(e))

def use_paste_clicked():
    global x_data, y_data, x_label, y_label
    try:
        x_data, y_data, x_label, y_label = parse_pasted(text_box.get("1.0", "end"))
        status.set(f"Using pasted data ({len(x_data)} rows, {x_label} vs {y_label})")
    except Exception as e:
        messagebox.showerror("CurveLab", str(e))

def run_fit():
    if x_data is None or y_data is None:
        messagebox.showwarning("CurveLab", "Load a CSV or paste data first.")
        return
    try:
        order = int(order_entry.get())
        r2, _ = fit_and_plot(x_data, y_data, order, x_label, y_label)
        status.set(f"Fit ok. R²={r2:.6g}")
    except Exception as e:
        messagebox.showerror("CurveLab", str(e))

# Build UI (ttkbootstrap)
root = tb.Window(themename="flatly")
root.title("CurveLab")
root.geometry("700x420")

main = tb.Frame(root, padding=12)
main.grid(sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=0)
main.columnconfigure(2, weight=0)

csv_path = tk.StringVar()
status = tk.StringVar(value="Ready")

# Row 0: CSV path + buttons
tb.Entry(main, textvariable=csv_path, width=56).grid(row=0, column=0, padx=6, pady=6, sticky="ew")
tb.Button(main, text="Browse CSV", bootstyle=SECONDARY, command=browse_csv).grid(row=0, column=1, padx=4, pady=6)
tb.Button(main, text="Load", bootstyle=PRIMARY, command=load_clicked).grid(row=0, column=2, padx=4, pady=6)

# Row 1: Order
tb.Label(main, text="Order:").grid(row=1, column=0, sticky="w", padx=6)
order_entry = tb.Entry(main, width=6)
order_entry.insert(0, "1")
order_entry.grid(row=1, column=0, padx=(56, 6), sticky="w")

# Row 2-3: Paste area
tb.Label(main, text="Or paste data (header optional; x y or x,y):").grid(row=2, column=0, columnspan=3, sticky="w", padx=6)
text_box = tk.Text(main, height=12)
text_box.grid(row=3, column=0, columnspan=3, padx=6, pady=4, sticky="nsew")
main.rowconfigure(3, weight=1)

# Row 4: Actions
tb.Button(main, text="Use Pasted Data", bootstyle=INFO, command=use_paste_clicked).grid(row=4, column=0, pady=10, padx=6, sticky="w")
tb.Button(main, text="Save CSV", bootstyle=SUCCESS, command=lambda: save_csv_dialog(x_data, y_data)).grid(row=4, column=1, pady=10)
tb.Button(main, text="Run Fit", bootstyle=PRIMARY, command=run_fit).grid(row=4, column=2, pady=10, padx=6, sticky="e")

# Status
tb.Label(main, textvariable=status, anchor="w").grid(row=5, column=0, columnspan=3, sticky="we", padx=6, pady=(0, 6))

root.mainloop()
