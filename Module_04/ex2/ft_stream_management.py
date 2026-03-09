import sys


def pars_create_files() -> None:
    id_file = input("Input Stream active. Enter archivist ID: ")
    data_file = input("Stream active. Enter status report: ")

    print(
        f"\n[STANDARD] Archive status from {id_file}: {data_file}",
        file=sys.stdout)
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print("\nThree-channel communication test successful.", file=sys.stdout)


if __name__ == '__main__':
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    pars_create_files()
