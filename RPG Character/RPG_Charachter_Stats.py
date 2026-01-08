

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    # ---- Name validation---- 
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    # ---- Stats validation ----
    stats = [strength, intelligence, charisma]

    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"
    if not all(stat >= 1 for stat in stats):
        return "All stats should be no less than 1"
    if not all(stat <= 6 for stat in stats):
        return "All stats should be no more than 6"
    if sum(stats) <= 7:
        return "The character should start with atleast 7 points"

    # ---- Output formatting ----
    def stat_line(label, value):
        return f"{label} {full_dot * value}{empty_dot * (10 - value)}"

    return "\n".join([
        name,
        stat_line("STR", strength),
        stat_line("INT", intelligence),
        stat_line("CHA", charisma)
    ])

def main():
    name =input("Enter character name: ")
    strength = int(input("Enter strength (1-6): "))
    intelligence = int(input("Enter intelligence (1-6): "))
    charisma = int(input("Enter charisma (1-6): "))
    character_info = create_character(name, strength, intelligence, charisma)
    print(character_info)

main()


