import ast
import os
import sys

def run_lint():
    # Type hint prevents Pylance from complaining about "Unknown" types
    errors: list[str] = []
    
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        source = f.read()
                    # Check for syntax errors and structural bugs
                    compile(source, file_path, "exec")
                    ast.parse(source, filename=file_path)
                except Exception as e:
                    errors.append(f"- **{file_path}**:\n  ```text\n  {e}\n  ```")
                    
    if errors:
        # Write compilation failures to a file for GitHub Actions to read
        with open("lint_errors.log", "w", encoding="utf-8") as log_file:
            log_file.write("\n".join(errors))
        print(f"Linting failed with {len(errors)} errors.")
        sys.exit(1)
        
    print("All built-in checks passed.")

if __name__ == "__main__":
    run_lint()
