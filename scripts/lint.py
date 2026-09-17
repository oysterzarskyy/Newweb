import subprocess
import sys


def run_lint():
    print("Running ruff checks...")
    
    # Check linting and formatting rules sequentially
    for command in [["ruff", "check", "."], ["ruff", "format", "--check", "."]]:
        result = subprocess.run(command)
        
        if result.returncode != 0:
            print(f"Error: Command '{' '.join(command)}' failed.")
            sys.exit(result.returncode)

    print("All checks passed.")


if __name__ == "__main__":
    run_lint()
