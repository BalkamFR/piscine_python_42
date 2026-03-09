def open_cyber_archives() -> None:
    try:
        f = open("ancient_fragment.txt", "r")
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f.read())
        f.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except Exception:
        print("ERROR: Storage vault not found")


if __name__ == '__main__':
    open_cyber_archives()
