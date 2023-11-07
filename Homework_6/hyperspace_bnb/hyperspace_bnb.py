"""
    CS 5001
    11/06/2023
    Homework 6 - hyperspace_bnb.py
    Garfield Maitland
"""
def load_travelers(travelers_file_name: str):
    """
    Function: load_travelers()
        Loads the travelers_file_name which is a file that has all the
        file information for the travelers. This includes their
        user_id, their name, and their available credits.

    Parameters:
        travelers_file_name (type: str)

    Returns:
        travelers

    Defense:
        try / except blocks
    """
    travelers = {}
    try:
        with open(travelers_file_name, 'r') as file:
            for line in file:
                parts = line.strip().split('@')
                if len(parts) != 3:
                    continue
                name, user_id, credits_str = parts
                try:
                    credits = int(credits_str)
                except ValueError:
                    print(f"Invalid number of credits: {credits_str} for traveler: {name}. Skipping.")
                    continue
                travelers[user_id] = {'name': name, 'credits': credits}
    except FileNotFoundError:
        print(f"The file {travelers_file_name} does not exist. Please check the filename and try again.")
        return None
    return travelers

def process_requests(travelers, request_file_name: str):
    """
    Function: process_requests()
        Loads the travelers_file_name which is a file that has all the
        file information for the travelers. This includes their
        user_id, their name, and their available credits.

    Parameters:
        travelers (type: str)
        request_file_name (type: str)

    Returns:
        none

    Defense:
        try / except blocks
    """
    if travelers is None:
        print("Traveler data is not available. Cannot process requests.")
        return
    week_booked = {}

    try:
        with open('bookings.txt', 'w') as bookings_file:
            with open(request_file_name, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) != 2:
                        continue
                    user_id, week_str = parts
                    try:
                        week = int(week_str)
                    except ValueError:
                        print(f"Invalid week number: {week_str}. Skipping.")
                        continue

                    if week in week_booked or user_id not in travelers:
                        continue

                    traveler_info = travelers[user_id]
                    if traveler_info['credits'] >= 500:
                        traveler_info['credits'] -= 500
                        week_booked[week] = user_id
                        bookings_file.write(f"{week} - {user_id} - {traveler_info['name']}\n")

    except FileNotFoundError:
        print(f"The file {request_file_name} does not exist. Please check the filename and try again.")
        return

    print("Finished processing reservations. Beam us up, Scottie!")


def main():
    travelers_data = load_travelers("travelers.txt")
    if travelers_data is not None:
        process_requests(travelers_data, "requests.txt")


if __name__ == "__main__":
    main()