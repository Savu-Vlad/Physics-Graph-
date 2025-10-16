# 🧮 CurveLab

CurveLab is a small Python app for quickly fitting **linear** and **polynomial** regressions to your data.  
It gives you a clean, simple interface to load or paste data, choose the curve order, and instantly see the result.

---

## 💡 What it does

- ✨ Modern, lightweight GUI (thanks to [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap))
- 📊 Fits curves of any order — from a straight line to high-order polynomials
- 📁 Load data from CSV or paste it right in
- 📈 See scatter + best-fit curve in one click
- 💾 Save your data back to CSV
- 🧠 Shows the equation and R² value right in the console

---

## 🧰 What you need first

You’ll need **Python 3.9+** with the `venv` module and `tkinter` for the GUI.

### On Arch Linux
    sudo pacman -S python tk

### On Ubuntu / Debian
    sudo apt install python3 python3-venv python3-tk

### On Fedora
    sudo dnf install python3 python3-tkinter

You can test if Tkinter works:
    python3 -m tkinter
If a tiny window called **“Tk”** pops up — you’re good.

---

## ⚙️ Setup

Clone and install:

```bash
git clone https://github.com/yourusername/CurveLab.git
cd CurveLab
chmod +x install.sh run.sh
./install.sh
```

That creates a `.venv` and installs everything from `requirements.txt`.  
Once it’s ready, launch the app:

```bash
./run.sh
```

---

## 🖱️ Using CurveLab

1. **Start the app** with `./run.sh`  
2. **Load your data**  
   - Click **Browse CSV → Load**, or  
   - Paste your own values into the box (CSV-style or space-separated)  
3. **Choose polynomial order**  
   - Default = 1 (linear)  
   - Try 2 or 3 for curved fits  
4. **Hit “Run Fit”**  
   - See your scatter plot and best-fit curve  
   - The equation and R² show up in the terminal  
5. **Optional:** Save your dataset with **Save CSV**

---

## 🧾 Files in this repo

| File | What it does |
|------|---------------|
| `curvelab.py` | Main app |
| `install.sh` | Creates `.venv` and installs dependencies |
| `run.sh` | Runs the app inside the virtual environment |
| `requirements.txt` | Lists Python dependencies |
| `.gitignore` | Keeps `.venv` and temp files out of git |
| `README.md` | This file |

---

## 🧩 Dependencies

Installed automatically:

    numpy
    pandas
    matplotlib
    ttkbootstrap

---

## 🎨 Extra tips

- Switch between **light** and **dark** themes in the code:
      root = tb.Window(themename="flatly")
  Try `"darkly"`, `"cyborg"`, or `"superhero"` if you like darker looks.

- If Tk is missing on Arch:
      sudo pacman -S tk

---

## 📜 License

MIT License © 2025  
Free to use, modify, and share for learning and personal projects.

---

### 🚀 Quick start

    sudo pacman -S python tk
    git clone https://github.com/yourusername/CurveLab.git
    cd CurveLab
    chmod +x install.sh run.sh
    ./install.sh
    ./run.sh

Happy fitting! 🎉
