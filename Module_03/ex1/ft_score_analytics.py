import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    all_score_users: list[int] = []
    i: int = 1
    if (len(sys.argv) == 1):
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return
    while (i < len(sys.argv)):
        try:
            if (int(sys.argv[i]) < 0):
                print("The negative values are forbidden")
            else:
                all_score_users.append(int(sys.argv[i]))
        except BaseException:
            print(f"oops, I typed ’{sys.argv[i]}’ instead of ’1000’")
        i += 1
    print(f"Scores processed: {all_score_users}")
    print(f"Total players: {len(all_score_users)}")
    print(f"Total score: {sum(all_score_users)}")
    print(f"Average score: {sum(all_score_users) / len(all_score_users)}")
    print(f"High score: {max(all_score_users)}")
    print(f"Low score: {min(all_score_users)}")
    print(f"Score range: {max(all_score_users) - min(all_score_users)}")


if __name__ == '__main__':
    main()
