# ----------------------------------------------------------------------
# Personalized Profile Card
# A simple Python script designed to be an introductory project for Git/GitHub.
# Students can easily customize the profile data to make it their own unique version.
# ----------------------------------------------------------------------

# --- 1. Data Structure ---
# Use a dictionary to store all the profile information.
# Students should easily customize the values in this section.
PROFILE_DATA = {
    "name": "Aiden",
    "title": "High School Python Enthusiast",
    "year_in_school": "Softmore",
    "favorite_project": "The 'Guess the Number' game",
    "favorite_food": "Pizza",
    "learning_goals": ["Mastering functions", "Understanding OOP", "Building a website"],
    "github_username": "AidenTrout825",
    "contact_email": "aidentrout21@gmail.com"
}

# --- 2. Styling and Formatting ---
# Define variables for visual elements (optional, but makes the output look nice)
DIVIDER = "=" * 45
SPACER = " " * 4
CARD_WIDTH = 45

# --- 3. The Display Function ---
def display_profile_card(data):
    """
    Prints the formatted profile card to the console using the provided data.
    """
    
    # 1. Print the top border and name
    print("\n" + DIVIDER)
    
    # Center the name for a clean look
    name_line = f"| {data['name'].upper()} |"
    print(name_line.center(CARD_WIDTH))
    
    # 2. Print the title/role
    title_line = f"| {data['title']} |"
    print(title_line.center(CARD_WIDTH))
    
    print(DIVIDER)
    
    # 3. Print main attributes
    print(f"| {SPACER} **CLASS DETAILS**")
    print(f"| {SPACER} Year: {data['year_in_school']}")
    print(f"| {SPACER} Favorite Python Project: {data['favorite_project']}")
    print(f"| {SPACER} Favorite Food: {data['favorite_food']}")
    print(DIVIDER)

    # 4. Print the Learning Goals (as a list)
    print(f"| {SPACER} **CURRENT LEARNING GOALS**")
    for goal in data["learning_goals"]:
        print(f"| {SPACER} - {goal}")
    
    print(DIVIDER)
    
    # 5. Print contact info
    print(f"| {SPACER} **CONNECT**")
    print(f"| {SPACER} GitHub: {data['github_username']}")
    print(f"| {SPACER} Email: {data['contact_email']}")
    
    print(DIVIDER + "\n")


# --- 4. Main Execution ---
if __name__ == "__main__":
    # Call the function to display the card
    display_profile_card(PROFILE_DATA)

# ----------------------------------------------------------------------
# Customization Task for Students:
# 1. Fork this repository on GitHub.
# 2. Clone it to your local machine.
# 3. Modify the PROFILE_DATA dictionary with your actual information.
# 4. Commit your changes locally.
# 5. Push your customized version back to your GitHub repository.
# ----------------------------------------------------------------------
