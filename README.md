# System Resource Monitor Flask App

This Flask-based application gathers system resource information such as CPU, memory, disk, and GPU usage and displays it on a simple web interface. Users can run the app locally on their own machines.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Interacting with the App](#interacting-with-the-app)
- [Stopping the App](#stopping-the-app)
- [Optional: Packaging for Distribution](#optional-packaging-for-distribution)
- [Libraries Required](#libraries-required)

---

## Prerequisites

To run this app, you'll need:

- **Python 3.6+** installed on your machine.
- Basic knowledge of using the terminal/command prompt.

---

## Installation

### Step 1: Install Python

1. Download and install Python from [python.org](https://www.python.org/downloads/). Ensure you select **"Add Python to PATH"** during installation.

2. Verify Python installation by running the following command in the terminal (or command prompt):
   ```bash
   python --version
   ```

### Step 2: Clone or Download the Repository

1. Clone this repository to your local machine or download the necessary files:
   ```bash
   git clone https://github.com/yourusername/system-resource-monitor.git
   ```
2. Change into the directory:
   ```bash
   cd system-resource-monitor
   ```

### Step 3: Set Up a Virtual Environment (Optional)

1. Create a virtual environment to isolate the dependencies:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```

### Step 4: Install Required Libraries

Install the required libraries with:

```bash
pip install Flask psutil GPUtil
```

---

## Running the App

Once you've installed the dependencies, you can run the app.

1. In the terminal or command prompt, run:

   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Interacting with the App

- Once the page loads, click the **"Get System Resources"** button.
- You will see the system's CPU, memory, disk, and GPU information displayed in a neat table format.

---

## Stopping the App

To stop the Flask server, simply press `CTRL + C` in the terminal or command prompt.

---

## Optional: Packaging for Distribution

If you'd like to package the app as a standalone executable, you can use **PyInstaller**:

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Run PyInstaller to create an executable:
   ```bash
   pyinstaller --onefile app.py
   ```

This will generate a standalone executable file (in the `dist` folder) that can be distributed to other users without requiring Python installation.

---

## Libraries Required

The following Python libraries are required to run the app:

- **Flask**: For serving the web app. Install via:

  ```bash
  pip install Flask
  ```

- **psutil**: For gathering system information like CPU, memory, and disk usage. Install via:

  ```bash
  pip install psutil
  ```

- **GPUtil**: For gathering GPU information (if available). Install via:
  ```bash
  pip install GPUtil
  ```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
