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

### 1. Install Deicide (Python package)

```bash
pip install -e /path/to/deicide
```

You must use **Python ≥ 3.11**.

### 2. Install deicide-tool

Inside this wrapper project:

```bash
pip install -e .
```

This installs the CLI:

```
deicide-tool
```

### System Requirements

- Python **3.11 or higher**
- macOS or Linux
- Java (used internally by Depends.jar)
- Rust binary `neodepends` (included in `resources/`)

---

## 🧪 Usage

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

### **“No module named 'deicide'”**
Install Deicide:

```bash
pip install -e /path/to/deicide
```

### **“neodepends: permission denied”**
Run:

```bash
chmod +x deicide_wrapper/resources/neodepends
```

### **Output directory exists**
The wrapper automatically overwrites `output-dir` on each run.

---

## 📜 License
Internal academic research tool.
