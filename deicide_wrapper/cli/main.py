import argparse
import subprocess
from pathlib import Path
import sys
import shutil
import time


# ------------------------------------------------
# Utility: Locate bundled resources
# ------------------------------------------------
def resource_path(filename):
    """Locate bundled resources inside the package."""
    return Path(__file__).resolve().parent.parent / "resources" / filename


# ------------------------------------------------
# Run NeoDepends
# ------------------------------------------------
def run_neodepends(project_dir: Path, db_out: Path, language: str = "java"):
    neodepends_bin = resource_path("neodepends")
    neodepends_bin.chmod(0o755)  # ensure executable

    cmd = [
        str(neodepends_bin),
        f"--input={project_dir}",
        f"--output={db_out}",
        f"-l{language}",
        "-D",
    ]

    print("\n[1/3] Running NeoDepends…")

    start = time.time()

    # Suppress NeoDepends stdout (but keep stderr for warnings)
    with subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    ) as proc:
        _, stderr = proc.communicate()
        if proc.returncode != 0:
            print("NeoDepends error:\n", stderr)
            raise subprocess.CalledProcessError(proc.returncode, cmd)

    elapsed = time.time() - start
    print(f"✔ NeoDepends complete ({elapsed:.2f}s): {db_out}")


# ------------------------------------------------
# Run Deicide
# ------------------------------------------------
def run_deicide(db_file: Path, output_json: Path, filename: Path, dv8: bool):
    print("\n[2/3] Running Deicide (direct import)…")

    start = time.time()

    from deicide import main as deicide_main

    args = [
        "--input", str(db_file),
        "--output", str(output_json),
        "--filename", str(filename),
    ]

    if dv8:
        args.append("--dv8-result")

    try:
        deicide_main(args)
    except SystemExit:
        pass  # Click exits normally with SystemExit

    elapsed = time.time() - start
    print(f"✔ Deicide complete ({elapsed:.2f}s): {output_json}")


# ------------------------------------------------
# Main CLI Entry Point
# ------------------------------------------------
def main():
    print("============================================================")
    print(" Deicide Suite — Unified NeoDepends + Deicide Runner")
    print("============================================================")

    parser = argparse.ArgumentParser(
        description="Run NeoDepends + Deicide in one command"
    )

    parser.add_argument(
        "--project", required=True,
        help="Path to the source-code directory (repo root)",
    )
    parser.add_argument(
        "--output-dir", required=True,
        help="Directory where outputs will be written",
    )
    parser.add_argument(
        "--filename", required=True,
        help="File inside the project to analyze (e.g. src/Test.java)",
    )
    parser.add_argument(
        "--dv8", action="store_true",
        help="Generate DV8-compatible outputs",
    )
    parser.add_argument(
        "--language", "--lang", default="java",
        choices=["c", "cpp", "go", "java", "javascript", "kotlin", "python", "ruby", "typescript"],
        help="Programming language to analyze (default: java). Supported: c, cpp, go, java, javascript, kotlin, python, ruby, typescript",
    )

    args = parser.parse_args()

    project_dir = Path(args.project).resolve()
    output_dir = Path(args.output_dir).resolve()
    filename = Path(args.filename)

    # Handle output directory
    if output_dir.exists():
        print(f"⚠️ Output directory exists, overwriting: {output_dir}")
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Output file paths
    db_out = output_dir / "dependencies.db"
    clustering_out = output_dir / "deicide_clustering.json"

    start_total = time.time()

    # Run tools
    run_neodepends(project_dir, db_out, args.language)
    run_deicide(db_out, clustering_out, filename, args.dv8)

    # Summary
    print("\n[3/3] Output Summary")
    print("✔ Files Generated:")
    for f in sorted(output_dir.iterdir()):
        print(f"   • {f}")

    total_time = time.time() - start_total
    print(f"\n🎉 Analysis complete in {total_time:.2f}s!")
    print(f"📁 Outputs saved in: {output_dir}")
    print("============================================================")


if __name__ == "__main__":
    main()
