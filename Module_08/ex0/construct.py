import sys, os
import site
from pathlib import Path


def main() -> None:
	if sys.prefix == "/usr":
		print(f"\nMATRIX STATUS: You're still plugged in\n")
		print(f"Current Python: {sys.executable}")
		print("Virtual Environment: None detected")
		print("WARNING: You're in the global environment!\n")
		print("The machines can see everything you install.")
		print("To enter the construct, run:")
		print("python -m venv matrix_env")
		print("source matrix_env/bin/activate # On Unix")
		print("matrix_env")
		print("Scripts")
		print("activate # On Window")
		print("\nThen run this program again.")
	else:
		print("\nMATRIX STATUS: Welcome to the construct\n")
		print(f"Current Python: {sys.executable}")
		env_name = os.path.basename(sys.prefix)
		print(f"Virtual Environment: {env_name}")
		print(f"Environment Path: {sys.prefix}")
		print("\nSUCCESS: You're in an isolated environment!")
		print("Safe to install packages without affecting the global system.")
		print(f"\nPackage installation path:")
		print(site.getsitepackages()[0])

if __name__ == '__main__':
	main()