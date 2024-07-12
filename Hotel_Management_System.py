import pandas as pd
import numpy as np
import datetime

# Load guest data from file using pandas
def load_guest_data():
    try:
        # Read data from CSV file into a DataFrame, parsing dates
        df = pd.read_csv("guest_data.csv", parse_dates=['check_in_date', 'check_out_date'])
    except FileNotFoundError:
        # If file not found, create an empty DataFrame
        df = pd.DataFrame(columns=['name', 'room_number', 'check_in_date', 'check_out_date'])
    return df

# Save guest data to file using pandas
def save_guest_data(df):
    # Write DataFrame to CSV file without row indices
    df.to_csv("guest_data.csv", index=False)

# Check-in a guest
def check_in(df, name, room_number):
    # Get today's date
    check_in_date = datetime.date.today()
    # Create a new DataFrame with check-in data
    new_guest = pd.DataFrame([[name, room_number, check_in_date, np.nan]], columns=df.columns)
    # Append new guest DataFrame to the existing DataFrame
    df = df.append(new_guest, ignore_index=True)
    # Save updated DataFrame to file
    save_guest_data(df)
    print(f"Checked in {name} to Room {room_number}.")

# Check-out a guest
def check_out(df, name):
    # Set check-out date to today's date for the guest with the specified name
    df.loc[df['name'] == name, 'check_out_date'] = datetime.date.today()
    # Save updated DataFrame to file
    save_guest_data(df)
    print(f"Checked out {name}.")

# Search for a guest
def search_guest(df, name):
    # Filter DataFrame for rows with the specified name
    guest = df[df['name'] == name]
    if not guest.empty:
        # If guest found, print guest details
        print("Guest details:")
        print(guest)
    else:
        # If guest not found, print a message
        print(f"Guest {name} not found.")

# Display all guests
def display_all_guests(df):
    if not df.empty:
        # If DataFrame is not empty, print all guest details
        print("All Guests:")
        print(df)
    else:
        # If DataFrame is empty, print a message
        print("No guests checked in.")

# Main menu
def main_menu():
    print("\n=== Hotel Management System ===")
    print("1. Check-in")
    print("2. Check-out")
    print("3. Search Guest")
    print("4. Display All Guests")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

# Main function
def main():
    # Load guest data from file
    df = load_guest_data()
    while True:
        # Display main menu and get user choice
        choice = main_menu()
        if choice == "1":
            print("\n=== Check-in ===")
            name = input("Enter guest name: ")
            room_number = int(input("Enter room number: "))
            # Perform check-in
            check_in(df, name, room_number)
        elif choice == "2":
            print("\n=== Check-out ===")
            name = input("Enter guest name to check out: ")
            # Perform check-out
            check_out(df, name)
        elif choice == "3":
            print("\n=== Search Guest ===")
            name = input("Enter guest name to search: ")
            # Perform guest search
            search_guest(df, name)
        elif choice == "4":
            # Display all guests
            display_all_guests(df)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# if __name__ == "_main_":
#     # Call the main function
main()