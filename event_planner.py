class EventPlanner:

    def __init__(self):
        self.events = []

    def myevents(self):
        print("---Event Management System---")
        print("1. Add Event")
        print("2. View Event")
        print("3. Delete Event")
        print("4. Exit")

    def add_event(self):
        event_name = input("Add event name: ")
        event_date = input("Enter event date (YYYY-MM-DD): ")
        event_type = input("Enter event type e.g (meeting, function, work...): ")
        
        # Create a dictionary with event details
        event = {"name": event_name, "date": event_date, "type": event_type}

        # Append the dictionary to the events list
        self.events.append(event)
        print("Event Added Successfully.")

    def view_event(self):
        if not self.events:
            print("No events.")
        else:
            print("Your Added Events are:")
            for event in self.events:
                print(f"Name: {event['name']}, Date: {event['date']}, Type: {event['type']}")

    def delete_event(self):
        event_name = input("Enter the event name you want to delete: ")
        for event in self.events:
            if event["name"] == event_name:
                self.events.remove(event)
                print("Event deleted successfully.")
                break
        else:
            print("Enter a valid event name.")

    def main(self):
        while True:
            self.myevents()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_event()

            elif choice == '2':
                self.view_event()

            elif choice == '3':
                self.delete_event()

            elif choice == '4':
                print("Exiting the application.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    planner = EventPlanner()
    planner.main()
