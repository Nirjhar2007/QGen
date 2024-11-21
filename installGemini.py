import subprocess
import sys

def install_dependencies():
    """Install required Python packages."""
    print("Installing dependencies...")
    required_packages = ["PyPDF2", "google-generativeai", "mysql-connector-python"]
    subprocess.check_call([sys.executable, "-m", "pip", "install", *required_packages])
    print("Dependencies installed successfully.")

if __name__ == "__main__":
    install_dependencies()
