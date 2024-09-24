import datetime
import json

class NobuTripTracker:
    def __init__(self):
        self.trips = []
        self.menu = {
            "Spicy Miso Chips - Tuna* or Scallop*": 8.00,
            "Fresh Oysters* with Nobu Sauces": 18.00,
            "Yellowtail Jalapeno*": 36.00,
            "Bigeye and Bluefin Toro Tartare*": 48.00,
            "Seafood Ceviche*": 30.00,
            "Lobster Ceviche on Limestone Lettuce (2 pieces)": 25.00,
            "Tiradito 'Nobu Style'*": 35.00,
            "New Style Sashimi*": 35.00,
            "Sashimi Salad with Matsuhisa Dressing*": 42.00,
        }
        self.filename = "nobu_trips.json"
        self.load_trips()

    def add_trip(self, date, location, selected_dishes, rating):
        total_cost = 0
        dishes_with_prices = []
        
        for dish_name in selected_dishes:
            if dish_name in self.menu:
                price = self.menu[dish_name]
                total_cost += price
                dishes_with_prices.append(f"{dish_name} (${price:.2f})")
            else:
                dishes_with_prices.append(f"{dish_name} (Price not available)")

        trip = {
            "date": date,
            "location": location,
            "dishes": dishes_with_prices,
            "total_cost": total_cost,
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
                print(f"Total Cost: ${trip['total_cost']:.2f}")
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
        print("3. View menu")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            date = input("Enter the date of your visit (YYYY-MM-DD): ")
            location = input("Enter the Nobu location: ")
            print("\nMenu:")
            for dish, price in tracker.menu.items():
                print(f"{dish} - ${price:.2f}")
            selected_dishes = input("\nEnter the dishes you had (comma-separated): ").split(',')
            rating = int(input("Rate your experience (1-10): "))
            tracker.add_trip(date, location, [dish.strip() for dish in selected_dishes], rating)
        elif choice == '2':
            tracker.view_trips()
        elif choice == '3':
            print("\nMenu:")
            for dish, price in tracker.menu.items():
                print(f"{dish} - ${price:.2f}")
        elif choice == '4':
            print("Thank you for using Nobu Trip Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
