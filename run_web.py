"""
Amazon Logistics AI - Web App Launcher
Starts the interactive browser interface
"""
import os
import subprocess
import sys

def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(project_root, 'app.py')
    print("=" * 70)
    print("Launching Amazon Logistics AI Web App...")
    print(f"Opening browser at: http://localhost:8501")
    print("=" * 70)
    
    cmd = [sys.executable, "-m", "streamlit", "run", app_path]
    subprocess.run(cmd, cwd=project_root)

if __name__ == '__main__':
    main()
