def main():
    print("\n\n\n\n######### Video Duration Calculator #########")
    print("      Press 'q' to get the final total.\n")
    total_seconds = 0

    def calculate_time(total_seconds):
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    while True:
        val_entered = input("Enter video duration (mm:ss): ")

        if val_entered == 'q':
            print("Generating total time...")
            final_total = calculate_time(total_seconds)
            print(f"Final video duration total: {final_total}")
            break

        try:
            minutes, seconds = map(int, val_entered.split(":"))
            converted_seconds = minutes * 60 + seconds
            total_seconds += converted_seconds
            current_total = calculate_time(total_seconds)
            print(f"Current total: {current_total}")
        except ValueError:
            print("Invalid input. Please use the mm:ss format.")

if __name__ == "__main__":
    main()
