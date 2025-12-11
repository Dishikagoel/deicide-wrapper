# Deicide Unified Tool — README

## Overview

The **Deicide Unified Tool** provides a single command-line interface that runs:

1. **NeoDepends** — extracts detailed dependency information from source code  
2. **Deicide** — analyzes large files and produces clustering/modularization suggestions  
3. *(Optional)* **DV8 output** — generates DV8-compatible clustering and dependency files  

All required components (NeoDepends binary, depends.jar, Deicide Python source) are fully bundled in this package.  
No external installations are required beyond Python.

**Supported Languages:** Java (default), Python, JavaScript, TypeScript, C/C++, Go, Kotlin, Ruby

## Installation

### Requirements

- Python **3.11+**
- macOS or Linux
- Java (used internally by Depends.jar)

### Install from source

```bash
# Create and activate a virtual environment (recommended)
python3.11 -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install the package
pip install -e .
```

This installs the CLI command:

```
deicide-tool
```

### Install from wheel

```bash
pip install deicide_wrapper-0.1.0-py3-none-any.whl
```

## Usage

### Basic example (Java - default)

```bash
deicide-tool \
  --project /path/to/java/project \
  --filename path/inside/project/FileToAnalyze.java \
  --output-dir results
```

### Analyze a Python project

```bash
deicide-tool \
  --project /path/to/python/project \
  --filename path/to/file.py \
  --output-dir results \
  --language python
```

### Analyze a JavaScript/TypeScript project

```bash
deicide-tool \
  --project /path/to/js/project \
  --filename src/index.js \
  --output-dir results \
  --language javascript
```

### With DV8-compatible output

```bash
deicide-tool \
  --project /path/to/java/project \
  --filename src/MyClass.java \
  --output-dir results \
  --dv8
```

### Supported Languages

The `--language` (or `--lang`) flag accepts: `c`, `cpp`, `go`, `java` (default), `javascript`, `kotlin`, `python`, `ruby`, `typescript`

## Output Files

| File | Description |
|------|-------------|
| `dependencies.db` | Dependency database produced by NeoDepends |
| `deicide_clustering.json` | Main Deicide clustering output |
| `deicide_clustering.dv8-clustering.json` | DV8 clustering file (if `--dv8`) |
| `deicide_clustering.dv8-dependency.json` | DV8 dependency file (if `--dv8`) |

If the output directory already exists, it will be replaced.

## Example Run

```bash
deicide-tool \
  --project "/Users/example/Survey3" \
  --filename src/Test.java \
  --output-dir out_test \
  --dv8
```

Sample output:

```
============================================================
 Deicide Suite — Unified NeoDepends + Deicide Runner
============================================================
[1/3] Running NeoDepends…
✔ NeoDepends complete (2.39s): out_test/dependencies.db

[2/3] Running Deicide (direct import)…
✔ Deicide complete (46.67s): out_test/deicide_clustering.json

[3/3] Output Summary
✔ Files Generated:
   • deicide_clustering.json
   • deicide_clustering.dv8-clustering.json
   • deicide_clustering.dv8-dependency.json
   • dependencies.db

🎉 Analysis complete in 49.06s!
📁 Outputs saved in: out_test
============================================================
```

## Troubleshooting

### **"No module named 'deicide'"**
Make sure the wrapper package is properly installed with your virtual environment activated:

```bash
source venv/bin/activate
pip install -e .
```

### **"Package requires Python >= 3.11"**
Ensure you're using Python 3.11 or higher:

```bash
python3 --version
```

If needed, create a new virtual environment:

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

## Notes

- The tool includes its own NeoDepends binary and depends.jar.  
- The Deicide engine is shipped directly within the package.  
- Temporary SQLite WAL files (`.db-wal`, `.db-shm`) may appear during execution but are safe and may be cleaned automatically.

## License

Internal academic research tool.
