def parse_story(file_name):
    try:
        with open(file_name, "r") as file:
            # Read and display the story introduction
            story_lines = []
            choices = {}
            coordinates = {  # Add story file names with their coordinates
                "intro.txt": (-275, -225),
                "distraction.txt": (-175,-250),
                "lever.txt": (45, -200),
                "charm.txt": (80, -80),
                "magical.txt": (-75,35),
                "negotiate.txt": (260, 80),
                "thestral.txt": (120, 50),
                "unicorn.txt": (-350, 40),
                "chaos.txt": (-5, -185),
                "crystal.txt": (40,200),
                "sneak.txt": (10,20),
                "ride.txt": (-80,-90),
                "chores.txt": (110,-120),
                "freeze.txt": (-250,20),
                "focus.txt": (-130,-140),
                "healer.txt": (-230,100),
                "elf.txt": (108,-250),
                "summon.txt": (10,-60),
                "gap.txt": (30,-180),
                "observation.txt": (10,80),
                "feed.txt": (200,-250),
                "teleport.txt": (-170,40),
                "guard.txt": (-66,-230),
                "call.txt": (-100,-10),
                "garden.txt": (108,-200),
                "goblin.txt": (4,130),
                "career.txt": (-200,-90),
                "approach.txt": (200,-20),
                "adventure.txt": (310,-30),
                "hippogriff.txt": (200,170),

            }
            for line in file:
                line = line.strip()
                if line.startswith("---"):  # Separator between story and choices
                    break
                story_lines.append(line)
            print("\n".join(story_lines))  # Display the story

            # Read and parse choices
            for line in file:
                line = line.strip()
                if not line:
                    continue
                choice_text, choice_file = line.split(":")
                choices[choice_text.strip().lower()] = choice_file.strip()

            return choices, coordinates  # Return choices and coordinates
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        return None, None  # Return None