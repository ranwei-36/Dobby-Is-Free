import time
import os
from turtle import *
from dobby import *
from read import *
from intro_out import *

def main():
    current_file = "all-txt/intro.txt"  # Starting story file

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgpic("all-image/map.gif")  # Set the background image

    intro_paint()
    hideturtle()
    time.sleep(5)

    penup()  # Lift the pen to avoid drawing lines
    goto(0,0)
    speed(4)
    draw_dobby(-275,-225)
    
    while current_file:
        choices, coordinates = parse_story(current_file)  # Get choices and coordinates
        if not choices:
            break

        print("\nChoices:")
        for choice in choices:
            print(f"- {choice}")

        user_choice = input("\nWhat do you do? ").lower()
        if user_choice in choices:
            current_file = f"all-txt/{choices[user_choice]}"
            if not os.path.isfile(current_file):
                print(f"Error: The file {current_file} does not exist. Please choose a valid option.")
                current_file = None
            elif any(ending in current_file for ending in ["ending_1", "ending_2", "ending_3", "ending_4"]):
                # Display congratulations and exit
                out_paint()
            else:
                # Move the turtle to the corresponding coordinates
                x, y = coordinates.get(choices[user_choice], (0, 0))  # Default to (0, 0) if not found
                #goto_new_coords(x, y)  # Use goto_new_coords instead of draw_dobby
                draw_dobby(x, y)  # Move turtle
        elif user_choice == "quit":
            print("Exiting the story. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    done()  # Keep the Turtle window open until manually closed

if __name__ == "__main__":
    main()