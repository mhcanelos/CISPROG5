# Step 1: Define the dictionary with state-capital pairs
states_and_capitals = {'Alabama':'Montgomery','Alaska':'Juneau',
               'Arizona':'Phoenix','Arkansas':'Little Rock',
               'California':'Sacramento','Colorado':'Denver',
               'Connecticut':'Hartford','Delaware':'Dover',
               'Florida':'Tallahassee','Georgia':'Atlanta',
               'Hawaii':'Honolulu','Idaho':'Boise',
               'Illinois':'Springfield','Indiana':'Indianapolis',
               'Iowa':'Des Moines','Kansas':'Topeka',
               'Kentucky':'Frankfort','Louisiana':'Baton Rouge',
               'Maine':'Augusta','Maryland':'Annapolis',
               'Massachusetts':'Boston','Michigan':'Lansing',
               'Minnesota':'Saint Paul','Mississippi':'Jackson',
               'Missouri':'Jefferson City','Montana':'Helena',
               'Nebraska':'Lincoln','Nevada':'Carson City',
               'New Hampshire':'Concord','New Jersey':'Trenton',
               'New Mexico':'Santa Fe','New York':'Albany',
               'North Carolina':'Raleigh','North Dakota':'Bismarck',
               'Ohio':'Columbus','Oklahoma':'Oklahoma City',
               'Oregon':'Salem','Pennsylvania':'Harrisburg',
               'Rhode Island':'Providence','South Carolina':'Columbia',
               'South Dakota':'Pierre','Tennessee':'Nashville',
               'Texas':'Austin','Utah':'Salt Lake City',
               'Vermont':'Montpelier','Virginia':'Richmond',
               'Washington':'Olympia','West Virginia':'Charleston',
               'Wisconsin':'Madison','Wyoming':'Cheyenne'}

# Step 2: Start an infinate loop for user queries

while True:
    user_input = input("Enter state or capital or type exit to stop") # Step 3 get input

    # Step 4 Check if ther user wants to exit
    if user_input.lower() == 'exit':
        break

    # Step 5 Check if input matches state
    if user_input in states_and_capitals:
        print(f"The capital of {user_input} is {states_and_capitals[user_input]}.")

    # Step 6: Check if the input matches a capital 
    elif user_input in states_and_capitals.values():
        # Find the corresponding state by iterating through the dictionary
        for state, capital in states_and_capitals.items():
            if capital == user_input:
                print(f"The state with capital {user_input} is {state}.")
                break
    # Step 7: Handle the invalid input
    else:
        print("State or capital not found. PLease try again.")