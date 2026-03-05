import os
import socket
import tempfile
import subprocess

ALLOWED_SITE = "www.w3schools.com"

def get_ip(domain):
    return socket.gethostbyname(domain)

def block_all_except(domain):
    ip = get_ip(domain)
    print(f"Allowing only {domain} ({ip})...")

    # Write a pf ruleset
    rules = f"""
block out all
pass out inet proto udp to any port 53
pass out inet to {ip}
pass out on lo0
"""
    # Write rules to a temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.conf', delete=False) as f:
        f.write(rules)
        rules_file = f.name

    subprocess.run(["sudo", "pfctl", "-e", "-f", rules_file], check=True)
    print("Done! Only W3Schools is accessible now.")
    return rules_file

def restore_internet(rules_file):
    subprocess.run(["sudo", "pfctl", "-d"], check=True)
    os.unlink(rules_file)
    print("Internet restored!")

# Run
rules_file = block_all_except(ALLOWED_SITE)
input("Press Enter to restore full internet access...")
restore_internet(rules_file)