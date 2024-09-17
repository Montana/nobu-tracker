import datetime
import json

class NobuTripTracker:
    def __init__(self):
        self.trips = []
        self.filename = "nobu_trips.json"
        self.load_trips()

    def add_trip(self, date, location, dishes, rating):
        trip = {
            "date": date,
            "location": location,
            "dishes": dishes,
            "rating": rating
        }
        self.trips.append(trip)
        self.save_trips()
        print("Trip added successfully!")

    def view_trips(self):
        if not self.trips:
            print("No trips recorded yet.")
        else:
            for i, trip in enumerate(self.trips, 1):
                print(f"\nTrip {i}:")
                print(f"Date: {trip['date']}")
                print(f"Location: {trip['location']}")
                print(f"Dishes: {', '.join(trip['dishes'])}")
                print(f"Rating: {trip['rating']}/10")

    def save_trips(self):
        with open(self.filename, 'w') as f:
            json.dump(self.trips, f)

    def load_trips(self):
        try:
            with open(self.filename, 'r') as f:
                self.trips = json.load(f)
        except FileNotFoundError:
            self.trips = []

def main():
    tracker = NobuTripTracker()

    while True:
        print("\nNobu Trip Tracker")
        print("1. Add a new trip")
        print("2. View all trips")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            date = input("Enter the date of your visit (YYYY-MM-DD): ")
            location = input("Enter the Nobu location: ")
            dishes = input("Enter the dishes you had (comma-separated): ").split(',')
            rating = int(input("Rate your experience (1-10): "))
            tracker.add_trip(date, location, dishes, rating)
        elif choice == '2':
            tracker.view_trips()
        elif choice == '3':
            print("Thank you for using Nobu Trip Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
