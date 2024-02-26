
GoIT Модуль 8 
Домашнє завдання 01, 02 


Домашнє завдання №1 


from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    birthdays = defaultdict(list)
    
    for user in users:
        name = user["name"]
        # Ensure that 'birthday' is a datetime object before calling .date()
        birthday = datetime.strptime(user["birthday"], "%Y-%m-%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        # If the birthday has already passed this year, consider the next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days
        
        # If the birthday is in the next week
        if 0 <= delta_days <= 7:
            day_of_week = birthday_this_year.strftime("%A")
            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"  # Move the greeting to Monday
            birthdays[day_of_week].append(name)
    
    # Output the result
    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")

# Example usage
users = [
    {"name": "Bill Gates", "birthday": "1955-10-28"},
    {"name": "Steve Jobs", "birthday": "1955-02-24"},
    # Add more users for testing
]

get_birthdays_per_week(users)



Завдання 2 


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please enter a command in the format 'add [name] [phone number]'."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please enter a command in the format 'change [name] [new phone number]'."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Error: Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Please enter a command in the format 'phone [name]'."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts stored."
    contacts_list = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return contacts_list

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
