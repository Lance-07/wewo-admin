# WeWo Admin Project

## Setup Instructions

### Prerequisites
Before getting started, ensure you have the following installed:

- **Python** (Version 3.12.8) – [Download here](https://www.python.org/downloads/)
- **Pip** (Version 24.3.1) – Comes with Python
- **Node.js** – Required for npm modules

### 1. Install Python
Download and install Python 3.12.8 from the [official website](https://www.python.org/downloads/). Verify the installation by running:
```bash
python --version
git clone https://github.com/Lance-07/wewo-admin.git
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment:
```bash
cd path-to-clone-repository
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
To deactivate the virtual environment:
```bash
deactivate
```

### 3. Install Project Dependencies
With the virtual environment activated, install required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Install Node.js Modules
Install necessary npm packages:
```bash
npm install
```

### 5. Compile TailwindCSS
Run the following command to watch and compile Tailwind CSS:
```bash
npx @tailwindcss/cli -i ./admin/static/input.css -o ./admin/static/output.css --watch
```

### 6. Run the Flask Application
Start the development server in debug mode:
```bash
flask --app admin run --debug
```

---
Feel free to modify this `README.md` file as needed. Let me know if you need further assistance!

