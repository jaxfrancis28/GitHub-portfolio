#The Galactic Battle Adventure Game
# #move from planet to planet obtaining the 6 abilities to defeat the Galactus.
#Jax Francis
#10/17/2022

def main_menu():
    # Print instructions and intro
    print("The Galactic Battle Adventure Game")
    print("Collect 6 abilities to win the game, or be destroyed by Galactus.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'ability name'")


def move_between_planets(current_room: object, move: object, planets: object) -> object:

    # move to corresponding planet
    current_room = planets[current_room][move]
    return current_room

def get_ability(current_room, move, rooms, inventory):
    # add item to inventory and remove it from the room
    inventory.append(rooms[current_room]['ability'])
    del rooms[current_room]['ability']


def main():
    # dictionary of connecting rooms with abilities
    global current_planet
    planets = {
        'Earth': dict(East='Mercury', West='Mars', South='Neptune', North='Saturn'),
        'Mars': dict(East='Earth', ability='Metallic'),
        'Saturn': dict(South='Earth', East='Jupiter', ability='Flying'),
        'Neptune': dict(North='Earth', East='Venus', ability='Water'),
        'Jupiter': dict(West='Saturn', ability='Strength'),
        'Venus': dict(West='Neptune', ability='Spiritual'),
        'Mercury': dict(West='Earth', North='Galactus Lair', ability='Fire'),
        'Galactus Lair': dict(South='Mercury''FIGHT GALACTUS!')
    }
    s = ' '
    # list for storing player inventory
    inventory = []
    # starting planet
    current_room = "Earth"
    # show the player the main menu
    main_menu()

    while True:
        # handle the case when player encounters the 'villain'
        if current_room == 'Galactus Lair':
            # winning case
            if len(inventory) == 6:
                print('Congratulations you have defeated The Great Galactus and saved the world!')
                print('Thank you for playing!')
                break
            # losing case
            else:
                print('\nOH NO! You did not collect all of the abilities!')
                print('You were destroyed by Galactus and the world was Demolished!')
                print('Thank you for playing!')
                break
        # Tell the user their current planet, inventory and prompt for a move, ignores case
        print('You are on ' + current_room)
        print(inventory)
        # tell the user if there is an ability in the room
        if current_room != 'The Sun' and 'ability' in planets[current_room].keys():
            print('You see the {}'.format(planets[current_room]['ability']))
        print('------------------------------')
        move = input('Enter your move: ').title().split()

        # handle if the user enters a command to move to a new planet
        if len(move) >= 2 and move[1] in planets[current_room].keys():
            current_room: object = move_between_planets(current_room, move[1], planets)
            continue
        # handle if the user enter a command to get an ability
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in planets[current_room]['ability']:
            print('You pick up the {}'.format(planets[current_room]['ability']))
            print('------------------------------')
            get_ability(current_room, move, planets, inventory)
            continue
        # handle if the user enters an invalid command
        else:
            print('Invalid move, please try again')
            continue


main()
