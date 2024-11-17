import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and print its output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        sys.exit(result.returncode)

def main():
    # Step 1: Create a virtual environment
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        run_command(f"{sys.executable} -m venv venv")

    # Step 2: Activate the virtual environment
    activate_script = os.path.join('venv', 'Scripts', 'activate')
    if os.name == 'posix':
        activate_script = os.path.join('venv', 'bin', 'activate')
    print("Activating virtual environment...")
    run_command(f"{activate_script} && echo 'Virtual environment activated.'")

    # Step 3: Upgrade pip
    print("Upgrading pip...")
    run_command(f"{sys.executable} -m pip install --upgrade pip")

    # Step 4: Install or upgrade torch
    print("Installing torch...")
    run_command(f"{sys.executable} -m pip install --upgrade torch")

    # Step 5: Install missing dependencies
    print("Installing missing dependencies...")
    run_command(f"{sys.executable} -m pip install numpy py-cpuinfo")

    # Step 6: Install deepspeed with no build isolation
    print("Installing deepspeed...")
    run_command(f"{sys.executable} -m pip install deepspeed --no-build-isolation")

    # Step 7: Install other requirements
    if os.path.exists('requirements.txt'):
        print("Installing other requirements...")
        run_command(f"{sys.executable} -m pip install -r requirements.txt")

    print("Setup complete.")

if __name__ == "__main__":
    main()
