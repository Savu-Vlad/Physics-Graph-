# 🧮 CurveLab

**CurveLab** is a lightweight Python application for performing **linear and polynomial regression** on user-supplied data.  
It provides a simple, cross-platform graphical interface for loading or pasting datasets, fitting polynomial curves, and visualizing results instantly.

---

## ✨ Features

- 🔹 **Interactive GUI** built with [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)
- 🔹 Load data from `.csv` files (first row used as axis labels)
- 🔹 Paste data directly (supports commas, tabs, or spaces)
- 🔹 Choose polynomial order (1st, 2nd, 3rd, …)
- 🔹 Automatically compute and display the regression curve and **R²**
- 🔹 Save edited or new datasets to `.csv`
- 🔹 Cross-platform — works on Linux, macOS, and Windows (with Python + Tkinter)

---

## 🧰 Requirements

Before installing, make sure your system has:

### System prerequisites
| Component | Description / Install Command |
|------------|------------------------------|
| **Python 3.9+** | Must include the `venv` module |
| **Tkinter** | Required for the GUI |
| **bash shell** | To run setup scripts |
| **Internet connection** | Needed once for dependency install |

#### 🐧 Arch Linux
    sudo pacman -S python tk

#### 🐧 Debian / Ubuntu
    sudo apt install python3 python3-venv python3-tk

#### 🐧 Fedora
    sudo dnf install python3 python3-tkinter

You can verify Tkinter works:
    python3 -m tkinter

A small window titled **“Tk”** should appear.

---

## ⚙️ Installation

Clone the repository and run the installation script:

    git clone https://github.com/yourusername/CurveLab.git
    cd CurveLab
    chmod +x install.sh run.sh
    ./install.sh

This will:
1. Create a local `.venv` virtual environment  
2. Install all required Python libraries from `requirements.txt`  
3. Print confirmation when setup is complete  

Once the setup finishes, start the app with:

    ./run.sh

---

## 🧾 Included Files

| File | Description |
|------|-------------|
| `curvelab.py` | Main application script |
| `requirements.txt` | Python dependencies |
| `install.sh` | Creates `.venv` and installs dependencies |
| `run.sh` | Activates `.venv` and launches the app |
| `README.md` | This documentation file |

---

## 📂 How to Use

1. **Launch the app**  
       ./run.sh

2. **Choose your data source**  
   - **Load CSV:** Click *Browse CSV → Load* and select a file with two numeric columns.  
     - The first row is used as axis labels (`x` and `y`).  
   - **Paste Data:** Paste values directly into the text box (comma, space, or tab separated).  
     Example:

        x, y  
        1, 2.3  
        2, 3.8  
        3, 5.7  
        4, 7.8  
        5, 10.2  

     Click **Use Pasted Data** to load it.

3. **Select Polynomial Order**  
   - Default = 1 (linear).  
   - You can try higher orders (2, 3, 4, …) to see curve fits.

4. **Run Fit**  
   - Click **Run Fit** to visualize.  
   - The app will display the scatter plot and regression curve using Matplotlib.  
   - Equation and R² are printed in the terminal.

5. **Save CSV (optional)**  
   - Click **Save CSV** to export your dataset to a new file.

---

## 📊 Example

Example data (`test.csv`):

    x, y
    1, 2.3
    2, 3.8
    3, 5.7
    4, 7.8
    5, 10.2
    6, 12.0
    7, 15.2
    8, 17.6
    9, 20.3
    10, 23.1

Running a 2nd-order polynomial fit produces a smooth curve following:

    y ≈ 0.16x² + 0.8x + 1.2  
    R² ≈ 0.999

---

## 🧩 Dependencies

All dependencies are automatically installed via `requirements.txt`:

    numpy
    pandas
    matplotlib
    ttkbootstrap

---

## 💡 Tips

- You can switch between **light** and **dark** themes by editing:
      root = tb.Window(themename="flatly")

  Try themes like `"darkly"`, `"cyborg"`, `"superhero"`, or `"litera"`.

- If you get an error about `libtk8.6.so` missing on Arch:
      sudo pacman -S tk

---

## 🧑‍💻 Development Notes

- The app uses `venv` for isolation — it won’t affect system packages.  
- To add new libraries:
      source .venv/bin/activate  
      pip install <package>  
      pip freeze > requirements.txt
- To remove the environment:
      rm -rf .venv

---

## 📜 License

MIT License © 2025  
You’re free to use, modify, and share this code for educational or personal purposes.

---

## 🧠 Acknowledgments

- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)
- [Matplotlib](https://matplotlib.org/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)

---

### 🏁 Quick Start Summary

    sudo pacman -S python tk
    git clone https://github.com/yourusername/CurveLab.git
    cd CurveLab
    chmod +x install.sh run.sh
    ./install.sh
    ./run.sh

Enjoy fitting curves! 🎉
