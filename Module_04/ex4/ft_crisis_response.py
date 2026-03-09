def crisis_response() -> None:
    try:
        with open("lost_archive.txt") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"CRISIS ALERT: Attempting access to '{e.filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    print()
    try:
        with open("classified_vault.txt") as f:
            print(f.read())
    except PermissionError as e:
        print(f"CRISIS ALERT: Attempting access to '{e.filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    print()
    try:
        with open("standard_archive.txt") as f:
            print("ROUTINE ACCESS: Attempting access to "
                  "'standard_archive.txt'...")
            print(f"SUCCESS: Archive recovered - '{f.read()}'")
            print("STATUS: Normal operations resumed")
    except Exception as e:
        print(e)
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == '__main__':
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_response()
