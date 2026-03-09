def create_cyber_archives() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    try:
        f = open("new_discovery.txt", "x")
        f.write("[ENTRY 001] New quantum algorithm discovered\n")
        f.write("[ENTRY 002] Efficiency increased by 347%\n")
        f.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        print("\nData inscription complete. Storage unit sealed.")
        f.close()
        files = open("new_discovery.txt", "r")
        print(files.read())
        files.close()
        print("Archive 'new_discovery.txt' ready for long-term preservation.")

    except Exception as a:
        print(f"Error: {a}")


if __name__ == '__main__':
    create_cyber_archives()
