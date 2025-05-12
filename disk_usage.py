import subprocess

df_output = subprocess.run(["df", "-h"], capture_output=True, text=True)
print(f"Aktualne zuzycie dysku: {df_output.stdout.strip()}") 
