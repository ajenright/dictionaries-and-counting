
# Create an empty dictionary
names = {}


names['Enright'] = 'Aaron'
names['Gill'] = 'Molly'

while True:
    last_name = input("Enter a student's last name: ")
    if last_name == "":
        # If the user hits enter without entering a name, stop the loop
        break
    print("Their first name is", names[last_name])

