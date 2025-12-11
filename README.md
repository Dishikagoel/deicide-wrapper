# deicide-tool  

Unified wrapper for running **NeoDepends** + **Deicide** in a single, streamlined workflow.

`deicide-tool` automatically extracts dependency information from source projects using **NeoDepends**, then runs **Deicide** to generate architecture-aware clustering and DV8-compatible analysis artifacts. Supports multiple programming languages including Java, Python, JavaScript, TypeScript, C/C++, Go, Kotlin, and Ruby.

---

## 🚀 Features

- ✔️ Runs **NeoDepends** (Rust dependency extractor)  
- ✔️ Runs **Deicide** (Python-based clustering + architecture analysis)  
- ✔️ Automatically produces **multiple output formats**  
  - `dependencies.db`  
  - `deicide_clustering.json`  
  - `deicide_clustering.dv8-clustering.json`  
  - `deicide_clustering.dv8-dependency.json`  

---

## 🛠️ Installation

### Prerequisites

- Python **3.11 or higher** (required)
- macOS or Linux
- Java (used internally by Depends.jar)
- Rust binary `neodepends` (included in `resources/`)

### Step-by-Step Installation

#### 1. Set up a Python virtual environment (recommended)

```bash
# Create a virtual environment with Python 3.11+
python3.11 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

#### 2. Install deicide-tool

Navigate to this wrapper project directory and install it:

```bash
pip install -e .
```

This installs the `deicide-tool` CLI command and includes the bundled Deicide package.

**Note:** Deicide is included in this package, so you don't need to install it separately.

#### 3. Verify Installation

Verify that the tool is installed correctly:

```bash
deicide-tool --help
```

You should see the help message with all available options.

#### 4. Make neodepends executable (if needed)

If you encounter permission errors, make the binary executable:

```bash
chmod +x deicide_wrapper/resources/neodepends
```

### System Requirements

- Python **3.11 or higher** (strictly required)
- macOS or Linux
- Java (used internally by Depends.jar)
- Rust binary `neodepends` (included in `resources/`)

---

## 🧪 Usage

**Important:** Make sure your virtual environment is activated before running commands:

```bash
source venv/bin/activate  # On macOS/Linux
```

### Basic example (Java - default)

```bash
deicide-tool \
  --project "/path/to/project" \
  --output-dir wrapper_output \
  --filename src/Test.java
```

### Analyze a Python project

```bash
deicide-tool \
  --project "/path/to/python-project" \
  --output-dir wrapper_output \
  --filename src/main.py \
  --language python
```

### Analyze a JavaScript/TypeScript project

```bash
deicide-tool \
  --project "/path/to/js-project" \
  --output-dir wrapper_output \
  --filename src/index.js \
  --language javascript
```

### Generate DV8-compatible outputs

```bash
deicide-tool \
  --project "/path/to/project" \
  --output-dir wrapper_output \
  --filename src/Test.java \
  --dv8
```

### Supported Languages

The `--language` (or `--lang`) flag accepts: `c`, `cpp`, `go`, `java` (default), `javascript`, `kotlin`, `python`, `ruby`, `typescript`

---

## 📁 Output Files

Running the tool generates:

| File | Description |
|------|-------------|
| `dependencies.db` | Extracted dependency graph (NeoDepends) |
| `deicide_clustering.json` | Standard Deicide clustering output |
| `deicide_clustering.dv8-clustering.json` | DV8 clustering format |
| `deicide_clustering.dv8-dependency.json` | DV8 dependency file |

All files are placed inside the specified `output-dir`.

---

## 🧩 How It Works

### **Step 1 — NeoDepends**
Parses source files for the specified language, resolves bindings, builds dependency matrices, and outputs a `.db` file.

### **Step 2 — Deicide**
Consumes the `.db` file and performs clustering + architecture analysis on the specified filename.

### **Step 3 — Output Summary**
Displays all generated files and total runtime.

---

## 🟥 Troubleshooting

### **"No module named 'deicide'"**
Make sure the wrapper package is properly installed with your virtual environment activated:

```bash
source venv/bin/activate  # Activate virtual environment
pip install -e .  # Reinstall the wrapper (Deicide is bundled)
```

### **"Package requires Python >= 3.11"**
Ensure you're using Python 3.11 or higher. Check your Python version:

```bash
python3 --version
```

If needed, create a new virtual environment with Python 3.11+:

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### **"neodepends: permission denied"**
Make the binary executable:

```bash
chmod +x deicide_wrapper/resources/neodepends
```

### **"unrecognized arguments: --language"**
Reinstall the package after code changes:

```bash
source venv/bin/activate
pip install -e .
```

### **Output directory exists**
The wrapper automatically overwrites `output-dir` on each run.

---

## 📜 License
Internal academic research tool.
