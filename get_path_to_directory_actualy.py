import subprocess
pwd_output = subprocess.run(["pwd"], capture_output=True, text=True)
print(f"Aktualna sciezka do folderu: {pwd_output.stdout.strip()}")
