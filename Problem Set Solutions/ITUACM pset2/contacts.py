#this "list" has 130 fictional names
contacts = [
    "Alice Johnson", "Bob Smith", "Charlie Brown", "David Lee", "Eva Green",
    "Frank Harris", "Grace White", "Hannah Lee", "Ian Black", "Julia Roberts",
    "Kyle Walker", "Lily Adams", "Mason Clark", "Nancy Davis", "Oscar Martinez",
    "Peter Lewis", "Quincy Turner", "Rachel Scott", "Samuel Carter", "Tina Moore",
    "Ursula Simmons", "Victor Allen", "Wendy Nelson", "Xander Pierce", "Yvonne Taylor",
    "Zachary King", "Ariana Hughes", "Brian Thomas", "Catherine Perez", "Daniel Walker",
    "Ella Scott", "Felix Mitchell", "Gina Evans", "Henry Brooks", "Isla Stewart",
    "James White", "Katherine King", "Leo Sanders", "Megan Carter", "Nina Edwards",
    "Oliver Collins", "Patricia Wood", "Quinn Foster", "Riley Morgan", "Sophie Green",
    "Theo Hall", "Una Thomas", "Vera King", "William Young", "Ximena Gonzalez",
    "Yara Brooks", "Zane Cooper", "Aiden Morris", "Bella Gray", "Caleb Wright",
    "Diana Lewis", "Ethan Allen", "Fiona Scott", "George Hernandez", "Holly Adams",
    "Isaac Campbell", "Jack Nelson", "Kendra Clark", "Lucas Bell", "Maya Fisher",
    "Nolan Davis", "Opal Scott", "Paulina Rivera", "Quincy Barnes", "Ryan Mitchell",
    "Sarah King", "Timothy Harris", "Uma Parker", "Victor Thomas", "Willow Young",
    "Xander Morgan", "Yasmine Wright", "Zoe Campbell", "Avery Adams", "Brianna Allen",
    "Connor Brooks", "Derek Johnson", "Eva Ross", "Felix Thomas", "Giselle Moore",
    "Holly White", "Ivy Perez", "Jacob Martinez", "Kylie Lewis", "Liam Carter",
    "Maddie Clark", "Nicholas Evans", "Olivia Sanders", "Penny Hall", "Quinn Miller",
    "Reed Gray", "Sophia Harris", "Tyler Scott", "Ulysses Young", "Vera Simmons",
    "Warren Green", "Xander Reed", "Yasmin Turner", "Zane Allen", "Avery Cooper",
    "Brady Thomas", "Chloe Green", "David Evans", "Ellie Baker", "Finn Mitchell",
    "Gabrielle Clark", "Hayden Ross", "India Morgan", "Jackie Walker", "Kieran Lewis",
    "Lindsay Turner", "Madeline Brown", "Nathaniel Lee", "Olga Walker", "Parker Scott",
    "Quinn Thompson", "Riley Johnson", "Samantha Reed", "Theo White", "Ursula Young",
    "Vince Harris", "Wyatt Green", "Xenia Ross", "Yvonne Anderson", "Zachary Scott"
]

# prompt the user for a filter letter
filter_letter = input("letter you want to filter by: ")

# validate that the input is a single character
if len(filter_letter) == 1:
    # filter contacts that start with the given letter
    filtered_contacts = [name for name in contacts if name.startswith(filter_letter)]

    # sort the filtered contacts alphabetically and print them
    filtered_sorted_contacts = sorted(filtered_contacts)
    print(f"filtered contacts (sorted alphabetically):\n{filtered_sorted_contacts}")

    # prompt the user for start and end indices for slicing
    index_start = int(input("enter the start index of the slice (e.g., 0): "))
    index_end = int(input("enter the end index of the slice (e.g., 3): "))

    # slice contacts and display them
    filtered_sorted_indexed_contacts = filtered_sorted_contacts[index_start:index_end]
    print(f"displaying contacts from {index_start} to {index_end}:\n{filtered_sorted_indexed_contacts}")
else:
    print("please enter only one letter.")
