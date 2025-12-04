import subprocess

output = subprocess.check_output(
    ["ipconfig"],
    encoding="utf-8",
    errors="ignore"
)
w_output = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"],
    encoding="utf-8",
    errors="ignore"
)

print(output)
print(w_output)
