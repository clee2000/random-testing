import subprocess
import sys
print(sys.executable)

push_result = subprocess.run(["ghstack"], capture_output=True).returncode
print(push_result)
print(";aldksfj")
