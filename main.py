import subprocess
profiles = []
output = subprocess.check_output(
    ["ipconfig"],
    encoding="utf-8",
    errors="ignore"
)
def ethernet_info(output):
    ethernet_profiles = []
    for line in output.split("\n"):
        if "IPv4 Address" in line:
            ip_adress = line.split(":")[1].strip()
            ethernet_profiles.append(ip_adress)
    return ethernet_profiles
        
        
    
w_output = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"],
    encoding="utf-8",
    errors="ignore"
)
for line in w_output.split("\n"):
    if "All user Profile" in line:
        name = line.split(":")[1].strip()
        profiles.append(name)
print(output)
print(profiles)
ethernet_info(output)
