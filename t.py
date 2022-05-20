import subprocess
import sys
print(sys.executable)

if subprocess.run([sys.executable, "-m", "ghstack", "--help"], capture_output=True).returncode != 0:
    subprocess.run([sys.executable, "-m", "pip", "install", "ghstack"])
print(";aldksfj")
