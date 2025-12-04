import subprocess

output = subprocess.check_output(
    ["ipconfig"],
    encoding="utf-8",
    errors="ignore"
)

print(output)
