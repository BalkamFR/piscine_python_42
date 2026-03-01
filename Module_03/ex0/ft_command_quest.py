import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    i: int = 1
    print(f"Arguments received: {len(sys.argv) - 1}")
    while (i < len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments : {len(sys.argv)}")


if __name__ == '__main__':
    main()
