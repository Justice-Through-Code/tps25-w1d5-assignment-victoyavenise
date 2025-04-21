# """
# Assignment Overview:

# You are building a Dog Image Browser using the Dog CEO REST API.

# The app should allow users to:
# - View a list of all available dog breeds
# - Get a random image of a breed
# - Get a random image of a sub-breed

# You will be using the Dog CEO API: https://dog.ceo/dog-api/

# Your app should display a main menu with the following options:
# 1. Show all breeds
# 2. Get a random image from a breed
# 3. Get a random image from a sub-breed
# 4. Exit

# The system should handle the following errors:
# - Handling errors when a user enters an invalid menu option
# - Handling errors when a user enters a breed that does not exist
# - Handling errors when a user enters a sub-breed that does not exist
# - Handling connection errors when calling the API

# If there is an error you should print your own custom error message to the user and allow them to try again.
# - Hint: you can use a while loop + try / except blocks to handle this

# You should use try / except blocks to handle these errors.

# You can either use the should use the requests library or the http.client library to make your requests

# """



import requests

def get_all_breeds():
    """GET request to fetch all dog breeds."""
    try:
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print("Error: Could not fetch breed list from API.")
        return {}

def get_random_image(breed):
    """GET request to fetch a random image from a breed."""
    try:
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print(f"Error: Could not fetch image for breed '{breed}'.")
        return None

def get_random_sub_breed_image(breed, sub_breed):
    """GET request to fetch a random image from a sub-breed."""
    try:
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print(f"Error: Could not fetch image for sub-breed '{sub_breed}' of breed '{breed}'.")
        return None

def show_breeds(breeds_dict):
    """Prints all available breeds 5 per line."""
    all_breeds = sorted(breeds_dict.keys())
    print("\nAvailable Breeds:")
    for i in range(0, len(all_breeds), 5):
        print(", ".join(all_breeds[i:i+5]))

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Show all breeds")
        print("2. Get a random image from a breed")
        print("3. Get a random image from a sub-breed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            breeds = get_all_breeds()
            show_breeds(breeds)

        elif choice == "2":
            breeds = get_all_breeds()
            if not breeds:
                continue
            breed = input("Enter breed name: ").strip().lower()
            if breed not in breeds:
                print("Error: Breed not found. Please try again.")
                continue
            image_url = get_random_image(breed)
            if image_url:
                print(f"Here's a random image of a {breed}: {image_url}")

        elif choice == "3":
            breeds = get_all_breeds()
            if not breeds:
                continue
            breed = input("Enter breed name: ").strip().lower()
            if breed not in breeds or not breeds[breed]:
                print("Error: This breed does not have sub-breeds or doesn't exist.")
                continue
            print("Available sub-breeds:", ", ".join(breeds[breed]))
            sub_breed = input("Enter sub-breed name: ").strip().lower()
            if sub_breed not in breeds[breed]:
                print("Error: Sub-breed not found. Please try again.")
                continue
            image_url = get_random_sub_breed_image(breed, sub_breed)
            if image_url:
                print(f"Here's a random image of a {sub_breed} {breed}: {image_url}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()