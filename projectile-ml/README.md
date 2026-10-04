# Can a Neural Network Learn Projectile Motion?

A machine learning project combining **A-level Physics** (mechanics, drag) and **Further Maths** (differential equations, numerical methods).

A projectile with air resistance has no neat SUVAT formula, so we:

1. **Simulate** it by solving the differential equations numerically (Euler's method and Runge–Kutta 4).
2. **Generate** a dataset of 3000 simulated launches.
3. **Train** machine learning models to predict the range, then test where they work and where they fail.

## Files

| File | What it does |
|---|---|
| `01_physics_simulation.ipynb` | Physics derivation, Euler and RK4, checking against SUVAT, and the order of convergence |
| `02_generate_dataset.ipynb` | Runs 3000 simulations and saves them to `data/projectiles.csv` |
| `03_machine_learning.ipynb` | Linear regression vs a neural network, finding the best angle, and extrapolation |
| `projectile.py` | The simulation code, shared by all the notebooks |
| `requirements.txt` | The Python libraries you need |

Run the notebooks **in order** (1 → 2 → 3). Notebook 3 needs the data file that Notebook 2 creates.

## Setup (Windows + VS Code)

### Step 1: Install Python
1. Download **Python 3.12** (or newer) from <https://www.python.org/downloads/>.
2. Run the installer and **tick "Add python.exe to PATH"** at the bottom of the first screen. This is important.
3. Click **Install Now**.
4. Close and reopen VS Code, then check it worked in a new terminal (**Terminal → New Terminal**):
   ```
   python --version
   ```

### Step 2: Install the Jupyter extension for VS Code
Open the Extensions panel (**Ctrl + Shift + X**), search for **Jupyter** (by Microsoft) and click **Install**. You already have the Python extension.

### Step 3: Create a virtual environment and install the libraries
A virtual environment keeps this project's libraries separate from everything else. In the VS Code terminal:

```powershell
cd projectile-ml
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> If you get an error saying *"running scripts is disabled on this system"*, run this once and try again:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

### Step 4: Open a notebook and pick the kernel
1. Open `01_physics_simulation.ipynb`.
2. Click **Select Kernel** (top right) → **Python Environments** → choose the one with **`.venv`** in its name.
3. Run each cell with **Shift + Enter**, or click **Run All**.

### Alternative: no installation (Google Colab)
Go to <https://colab.research.google.com>, choose **File → Upload notebook**, and upload a notebook. Then click the folder icon on the left and upload `projectile.py` too. For Notebook 3, also upload `data/projectiles.csv` into a folder called `data`. Colab already has all the libraries.

## The maths and physics in one place

With quadratic drag $\mathbf{F} = -k|\mathbf{v}|\mathbf{v}$ and $b = k/m$:

$$\frac{dv_x}{dt} = -b\,v\,v_x, \qquad \frac{dv_y}{dt} = -g - b\,v\,v_y$$

These are solved with RK4 (error ∝ h⁴) using a time step of 0.01 s.

## Ideas for extending it
These are listed at the end of Notebook 3. They include predicting the drag of a real ball from a video using [Tracker](https://physlets.org/tracker/), adding spin (the Magnus effect), and investigating overfitting by changing the network size.
