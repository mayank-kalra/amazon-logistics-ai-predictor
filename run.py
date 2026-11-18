"""
Amazon Logistics AI Predictor - Pipeline Runner
Runs the predictive modeling pipeline and outputs charts to assets/figures/
"""
import os
import subprocess
import sys

def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(project_root, 'code', 'Final Project.py')
    print("=" * 70)
    print("Starting Amazon Logistics AI Predictor...")
    print(f"Executing: {script_path}")
    print("=" * 70)
    
    result = subprocess.run([sys.executable, script_path], cwd=project_root)
    if result.returncode == 0:
        print("\n" + "=" * 70)
        print("Pipeline execution succeeded!")
        print("Generated figures saved in: assets/figures/")
        print("=" * 70)
    sys.exit(result.returncode)

if __name__ == '__main__':
    main()
