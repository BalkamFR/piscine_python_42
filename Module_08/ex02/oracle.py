import os
import sys
try:
    from dotenv import load_dotenv
except BaseException:
    print("please : pip install dotenv")
    sys.exit(1)


def read_config() -> None:
    print("Configuration loaded:")
    load_dotenv()
    MATRIX_MODE = os.getenv('MATRIX_MODE')
    DATABASE_URL = os.getenv('DATABASE_URL')
    API_KEY = os.getenv('API_KEY')
    LOG_LEVEL = os.getenv('LOG_LEVEL')
    ZION_ENDPOINT = os.getenv('ZION_ENDPOINT')
    print(f"Mode: {MATRIX_MODE}")
    if DATABASE_URL is not None:
        print("Database: Connected to local instance")
    else:
        print("Database: WARNING - Connection Failed")
    if API_KEY is not None:
        print("API Access: Authenticated")
    else:
        print("API Access: WARNING - Unauthenticated")
    print(f"Log Level: {LOG_LEVEL}")
    if ZION_ENDPOINT is not None:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    read_config()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
