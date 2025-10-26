<-ll filepath: GraphPhysics README -->
# 📊 GraphPhysics

GraphPhysics is a modern Python application for fitting **linear** and **polynomial** regressions to experimental data.  
It provides a sleek, professional interface to load or paste data, select the polynomial order, and instantly visualize the results with beautiful plots.

---

## 💡 What it does

- ✨ Modern dark theme GUI with intuitive controls (powered by [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap))
- 📊 Fits polynomial curves of any order — from linear (order 1) to high-degree polynomials
- 📁 Load data from CSV files or paste it directly
- 📈 Beautiful scatter plots with best-fit curves and color-coded visualization
- 💾 Save your analyzed datasets back to CSV
- 🧮 Displays regression equations, R² statistics, and detailed analysis in terminal
- 🎨 Professional-grade plots with customizable styling

---

## 🧰 Requirements

You'll need **Python 3.9+** with the `venv` module and `tkinter` for the GUI.

### On Arch Linux
\`\`\`bash
sudo pacman -S python tk
\`\`\`

### On Ubuntu / Debian
\`\`\`bash
sudo apt install python3 python3-venv python3-tk
\`\`\`

### On Fedora
\`\`\`bash
sudo dnf install python3 python3-tkinter
\`\`\`

You can test if Tkinter works:
\`\`\`bash
python3 -m tkinter
\`\`\`
If a tiny window called **"Tk"** pops up — you're good to go!

---

## ⚙️ Setup

Clone and install:

\`\`\`bash
git clone https://github.com/yourusername/GraphPhysics.git
cd GraphPhysics
chmod +x install.sh run.sh
./install.sh
\`\`\`

That creates a \`venv\` directory and installs everything from \`requirements.txt\`.  
Once it's ready, launch the app:

\`\`\`bash
./run.sh
\`\`\`

---

## 🖱️ How to use GraphPhysics

1. **Start the application** with \`./run.sh\`  

2. **Load your data**  
   - Click **📁 Browse** to select a CSV file, then click **✓ Load CSV**, or  
   - Paste your data directly into the text area (comma or space-separated)
   - The first line can be axis labels (e.g., "voltage intensity" or "distance light_intensity")

3. **Configure polynomial order**  
   - Enter the desired polynomial order (default = 1 for linear)
   - Try 2-3 for curved data, higher values for complex relationships

4. **Run the analysis**  
   - Click **🚀 Fit & Plot**
   - A window opens with your scatter plot and best-fit curve
   - The console displays the equation and R² value

5. **Save results** (optional)  
   - Click **💾 Save Data** to export your dataset

---

## 📊 Example Data Format

**CSV File or Pasted Data:**
\`\`\`
voltage,intensity
0.5,0.1
1.0,0.2
1.5,0.3
2.0,0.4
\`\`\`

Or space-separated:
\`\`\`
voltage intensity
0.5 0.1
1.0 0.2
1.5 0.3
2.0 0.4
\`\`\`

---

## 🧾 Files in this repo

| File | Purpose |
|------|---------|
| \`graph_physics.py\` | Main application |
| \`install.sh\` | Creates \`venv\` and installs dependencies |
| \`run.sh\` | Launches the app in virtual environment |
| \`requirements.txt\` | Python package dependencies |
| \`README.md\` | This documentation |

---

## 🧩 Dependencies

Automatically installed via \`requirements.txt\`:

\`\`\`
numpy
pandas
matplotlib
ttkbootstrap
\`\`\`

---

## 🎨 Customization

### Change the theme
Edit \`graph_physics.py\` and modify:
\`\`\`python
root = tb.Window(themename="darkly")
\`\`\`

Available themes: \`"flatly"\`, \`"darkly"\`, \`"cyborg"\`, \`"superhero"\`, \`"solar"\`, etc.

### Adjust plot colors
In the \`fit_and_plot()\` function:
\`\`\`python
ax.scatter(x, y, color="#FF6B6B", ...)  # Data points color
ax.plot(xx, yy, color="#4ECDC4", ...)   # Fit line color
\`\`\`

---

## 🔧 Troubleshooting

**ImportError for pandas/numpy:**
\`\`\`bash
source venv/bin/activate
pip install --upgrade pip
pip install numpy pandas matplotlib ttkbootstrap
\`\`\`

**Tkinter not found (Arch Linux):**
\`\`\`bash
sudo pacman -S tk
\`\`\`

**Tkinter not found (Ubuntu/Debian):**
\`\`\`bash
sudo apt install python3-tk
\`\`\`

---

## 📜 License

MIT License © 2025  
Free to use, modify, and distribute for educational and personal projects.

---

## 🚀 Quick Start

\`\`\`bash
# Install dependencies
sudo pacman -S python tk

# Clone and setup
git clone https://github.com/yourusername/GraphPhysics.git
cd GraphPhysics
chmod +x install.sh run.sh

# Install Python packages
./install.sh

# Run the application
./run.sh
\`\`\`
