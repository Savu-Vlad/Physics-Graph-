"""
GraphPhysics - Polynomial Regression Analysis Tool
A modern GUI for fitting polynomial curves to experimental data
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from io import StringIO
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import ttkbootstrap as tb
from ttkbootstrap.constants import *


# ============================================================================
# DATA PROCESSING FUNCTIONS
# ============================================================================

def _extract_labels(col0, col1):
    """Extract meaningful axis labels from column headers."""
    x_name, y_name = str(col0), str(col1)
    if x_name.strip().isdigit() or x_name.strip().lower() in {"col0", "column1"}:
        x_name = "x"
    if y_name.strip().isdigit() or y_name.strip().lower() in {"col1", "column2"}:
        y_name = "y"
    return x_name, y_name


def load_csv(path: str):
    """Load CSV file with automatic separator detection and data validation."""
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
    """Parse pasted data from text input (supports CSV and whitespace separated)."""
    if not text.strip():
        raise ValueError("Paste some data first (two columns).")
    
    df = pd.read_csv(
        StringIO(text.strip()),
        sep=r"[,\s]+",
        engine="python",
        comment="#"
    )
    
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
    """Save current dataset to CSV file."""
    if x is None or y is None:
        messagebox.showwarning("GraphPhysics", "No data to save yet.")
        return
    
    path = filedialog.asksaveasfilename(
        title="Save data as CSV",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    
    if not path:
        return
    
    pd.DataFrame({"x": x, "y": y}).to_csv(path, index=False)
    messagebox.showinfo("GraphPhysics", f"✅ Saved → {Path(path).name}")


# ============================================================================
# FITTING AND VISUALIZATION FUNCTIONS
# ============================================================================

def fit_and_plot(x, y, order, xlabel, ylabel):
    """Fit polynomial curve and display results with visualization."""
    if order < 1:
        raise ValueError("Order must be >= 1.")
    
    coeffs = np.polyfit(x, y, order)
    p = np.poly1d(coeffs)

    xx = np.linspace(np.min(x), np.max(x), 400)
    yy = p(xx)

    # Create enhanced plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y, color="#FF6B6B", s=100, alpha=0.7, label="Data Points", edgecolors="darkred", linewidth=1.5)
    ax.plot(xx, yy, color="#4ECDC4", linewidth=2.5, label=f"Polynomial Fit (order {order})")
    ax.set_xlabel(xlabel or "x", fontsize=12, fontweight="bold")
    ax.set_ylabel(ylabel or "y", fontsize=12, fontweight="bold")
    ax.set_title("Polynomial Regression Analysis", fontsize=14, fontweight="bold")
    ax.grid(True, alpha=0.3, linestyle="--")
    ax.legend(fontsize=10, loc="best")
    plt.tight_layout()
    plt.show()

    # Calculate R² goodness of fit
    yhat = p(x)
    ss_res = np.sum((y - yhat) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot != 0 else float("nan")

    # Extract slope (first coefficient) and intercept (last coefficient)
    slope = coeffs[0] if order >= 1 else 0
    intercept = coeffs[-1]

    eq = str(np.poly1d(coeffs))
    print("\n" + "="*60)
    print("📊 REGRESSION RESULTS")
    print("="*60)
    print(f"\n📈 Equation of best fit:\n{eq}")
    print(f"\n📐 Slope (m): {slope:.8f}")
    print(f"📍 Intercept (b): {intercept:.8f}")
    print(f"\n📊 R² (Goodness of fit): {r2:.8f}")
    print(f"✓ Data points fitted: {len(x)}")
    print("="*60 + "\n")
    
    return r2, eq, slope, intercept

# ============================================================================
# GUI CALLBACKS
# ============================================================================

x_data = y_data = None
x_label = y_label = None


def browse_csv():
    """Open file browser to select CSV file."""
    path = filedialog.askopenfilename(
        title="📁 Select CSV File",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if path:
        csv_path.set(path)
        status.set(f"📂 Selected: {Path(path).name}")


def load_clicked():
    """Load CSV file and update data."""
    global x_data, y_data, x_label, y_label
    if not csv_path.get():
        messagebox.showwarning("GraphPhysics", "⚠️  Please select a CSV file first.")
        return
    try:
        x_data, y_data, x_label, y_label = load_csv(csv_path.get())
        status.set(f"✅ Loaded {len(x_data)} rows | {x_label} vs {y_label}")
        data_info_label.config(
            text=f"📊 Data: {len(x_data)} points | Range X: [{x_data.min():.2f}, {x_data.max():.2f}]"
        )
    except Exception as e:
        messagebox.showerror("GraphPhysics Error", str(e))
        status.set("❌ Failed to load CSV")


def use_paste_clicked():
    """Parse pasted data from text box."""
    global x_data, y_data, x_label, y_label
    try:
        x_data, y_data, x_label, y_label = parse_pasted(text_box.get("1.0", "end"))
        status.set(f"✅ Using pasted data ({len(x_data)} rows, {x_label} vs {y_label})")
        data_info_label.config(
            text=f"📊 Data: {len(x_data)} points | Range X: [{x_data.min():.2f}, {x_data.max():.2f}]"
        )
    except Exception as e:
        messagebox.showerror("GraphPhysics Error", str(e))
        status.set("❌ Failed to parse pasted data")


def run_fit():
    """Execute polynomial fitting and visualization."""
    if x_data is None or y_data is None:
        messagebox.showwarning("GraphPhysics", "⚠️  Load a CSV or paste data first.")
        return
    try:
        order = int(order_entry.get())
        if order < 1 or order > 10:
            raise ValueError("Polynomial order must be between 1 and 10.")
        r2, eq, slope, intercept = fit_and_plot(x_data, y_data, order, x_label, y_label)
        status.set(f"✨ Fit completed! R² = {r2:.8f}")
        # Update results panel
        results_text.config(state=tk.NORMAL)
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"📊 RESULTS\n")
        results_text.insert(tk.END, f"{'='*33}\n\n")
        results_text.insert(tk.END, f"📈 Slope (m):\n{slope:.8f}\n\n")
        results_text.insert(tk.END, f"📍 Intercept (b):\n{intercept:.8f}\n\n")
        results_text.insert(tk.END, f"📐 R² Value:\n{r2:.8f}\n\n")
        results_text.insert(tk.END, f"✓ Points: {len(x_data)}\n")
        results_text.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showerror("GraphPhysics Error", str(e))
        status.set("❌ Invalid order value")
    except Exception as e:
        messagebox.showerror("GraphPhysics Error", str(e))
        status.set("❌ Fitting failed")


# ============================================================================
# UI INITIALIZATION (Modern Theme)
# ============================================================================

root = tb.Window(themename="darkly")
root.title("📊 GraphPhysics - Polynomial Regression")
root.geometry("800x550")

# Configure dark theme colors
style = tb.Style()
style.configure("Title.TLabel", font=("Helvetica", 16, "bold"), foreground="#00D9FF")
style.configure("Info.TLabel", font=("Helvetica", 10), foreground="#A0A0A0")
style.configure("Header.TLabel", font=("Helvetica", 11, "bold"), foreground="#00D9FF")

# Main container
main = tb.Frame(root, padding=15)
main.grid(sticky="nsew", row=0, column=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main.columnconfigure(0, weight=1)
main.rowconfigure(3, weight=1)

# --- TITLE ---
title_frame = tb.Frame(main)
title_frame.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(0, 15))
tb.Label(title_frame, text="📊 GraphPhysics", style="Title.TLabel").pack(side="left")
tb.Label(title_frame, text="Polynomial Regression Analysis", style="Info.TLabel").pack(side="left", padx=(15, 0))

# --- SECTION 1: CSV INPUT ---
csv_section = tb.LabelFrame(main, text="📂 Load From CSV File", padding=10)
csv_section.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 12))
csv_section.columnconfigure(0, weight=1)

csv_path = tk.StringVar()
csv_input = tb.Entry(csv_section, textvariable=csv_path, width=60)
csv_input.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="ew")

tb.Button(csv_section, text="📁 Browse", bootstyle="info", command=browse_csv).grid(row=0, column=1, padx=5)
tb.Button(csv_section, text="✓ Load CSV", bootstyle="success", command=load_clicked).grid(row=0, column=2, padx=5)

# --- SECTION 2: POLYNOMIAL ORDER ---
config_section = tb.Frame(main)
config_section.grid(row=2, column=0, columnspan=3, sticky="ew", pady=(0, 12))

tb.Label(config_section, text="📈 Polynomial Order:", style="Header.TLabel").pack(side="left", padx=(0, 10))
order_entry = tb.Entry(config_section, width=4, bootstyle="info")
order_entry.insert(0, "1")
order_entry.pack(side="left", padx=(0, 20))

tb.Label(config_section, text="🎯 Run Analysis:", style="Header.TLabel").pack(side="left", padx=(0, 10))
tb.Button(config_section, text="🚀 Fit & Plot", bootstyle="danger", command=run_fit, width=15).pack(side="left")
tb.Button(config_section, text="💾 Save Data", bootstyle="warning", command=lambda: save_csv_dialog(x_data, y_data), width=15).pack(side="left", padx=(10, 0))

# --- SECTION 3: PASTE DATA ---
paste_label = tb.Label(main, text="📋 Or Paste Data (space/comma separated, optional header):", style="Header.TLabel")
paste_label.grid(row=3, column=0, columnspan=2, sticky="w", pady=(10, 5))

text_frame = tb.Frame(main)
text_frame.grid(row=4, column=0, columnspan=2, sticky="nsew", pady=(0, 12))
text_frame.rowconfigure(0, weight=1)
text_frame.columnconfigure(0, weight=1)

text_box = tk.Text(text_frame, height=10, width=60, bg="#2B2B2B", fg="#FFFFFF", insertbackground="#00D9FF", wrap=tk.WORD)
text_box.pack(fill=tk.BOTH, expand=True, side="left")

# Scrollbar for text box
scrollbar = tb.Scrollbar(text_frame, command=text_box.yview)
text_box.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# --- SECTION 3B: RESULTS PANEL ---
results_label = tb.Label(main, text="📊 Analysis Results:", style="Header.TLabel")
results_label.grid(row=3, column=2, sticky="w", pady=(10, 5), padx=(10, 0))

results_frame = tb.Frame(main)
results_frame.grid(row=4, column=2, sticky="nsew", pady=(0, 12), padx=(10, 0))
results_frame.rowconfigure(0, weight=1)
results_frame.columnconfigure(0, weight=1)

results_text = tk.Text(results_frame, height=10, width=35, bg="#1A1A1A", fg="#00D9FF", insertbackground="#00D9FF", wrap=tk.WORD, font=("Courier", 9))
results_text.pack(fill=tk.BOTH, expand=True)
results_text.insert(tk.END, "⏳ Results will appear here\nafter running a fit analysis")
results_text.config(state=tk.DISABLED)

# --- SECTION 4: ACTION BUTTONS ---
action_frame = tb.Frame(main)
action_frame.grid(row=5, column=0, columnspan=3, sticky="ew", pady=(0, 12))

tb.Button(action_frame, text="📥 Use Pasted Data", bootstyle="info", command=use_paste_clicked).pack(side="left", padx=5)

# --- STATUS & INFO ---
status = tk.StringVar(value="🟢 Ready")
status_label = tb.Label(main, textvariable=status, style="Info.TLabel", anchor="w")
status_label.grid(row=6, column=0, columnspan=3, sticky="ew", pady=(5, 0))

data_info_label = tb.Label(main, text="⏳ Awaiting data...", style="Info.TLabel", anchor="w")
data_info_label.grid(row=7, column=0, columnspan=3, sticky="ew", pady=(2, 0))

# ============================================================================
# RUN APPLICATION
# ============================================================================

root.mainloop()
