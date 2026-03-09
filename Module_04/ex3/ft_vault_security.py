def cyber_archives_extraction() -> None:
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt") as f:
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            print(f.read())
    except Exception as e:
        print(f"Error: {e}")


def cyber_archives_add() -> None:
    print("\nSECURE PRESERVATION:")
    try:
        print("[CLASSIFIED] New security protocols archived")
        with open("classified_data.txt", "a") as f:
            f.write("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    cyber_archives_extraction()
    cyber_archives_add()
    print("\nAll vault operations completed with maximum security.")
