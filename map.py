
#FIRST LET ME SAY THIS IS A LAB FOR SCHOOL, I BASED MY HOMEWORK ASSIGNMENT OF A GAME OFF A CLASS  (CentralCorridor(Scene):) TUTORIAL OF THE GAME (The Gothons of Planet Percal #25)" IN CHPATER 43 FROM LEARN PYTHON 3 THE HARD WAY..

from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):#shows surroundings and makes decision
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):# process through story
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene() # set current_scene to "from scene_map, get the opening_scene funciton" get opening scene basically
        last_scene = self.scene_map.next_scene('finished') # set last_scene to "from scene_map, get the next_scene function with 'finished' as a parameter"
        # this while loop makes next scene be current scene
        while current_scene != last_scene: # while current_scene is not the last_scene
            next_scene_name = current_scene.enter() # set next_scene_name to "from current.scene, run the enter function"
            current_scene = self.scene_map.next_scene(next_scene_name) # set current scene to "from scene_map, get the next_scene function with next_scene_name as a parameter"
        # be sure to print out the last scene_map
        current_scene.enter()

class Death(Scene):
        def enter(self):

            exit(1)


class Basement(Scene):
    def enter(self): # dedent takes away white spaces
        print(dedent(""" FIRST LET ME SAY THIS IS A LAB FOR SCHOOL, I BASED MY HOMEWORK ASSIGNMENT OF A GAME OFF A CLASS  (CentralCorridor(Scene):) TUTORIAL OF THE GAME (The Gothons of Planet Percal #25)" IN CHPATER 43 FROM LEARN PYTHON 3 THE HARD WAY..
            The crazy neighborhood robbers are in your home and killed everyone in your house. You are the only one in the house to survive, the only way out is by
    defeating the robber, to get to the robber you have to get to the attic to get the only gun in the house and shoot him. You're in the basement good luck.
       - You notice a staircase to your right and a door to your left.
        - Which way will you go?
            """))

        action = input("> ")

        if action == "left":
            print(dedent("""
                As you slowly approach the door, you hear a noise inside, there was a robber there and he punched you and knocked you out and then shot you. You died.
                """))
            return 'death' # return the death scene

        elif action == "right": #
            print(dedent("""
            As you go up the stairs you find a door, that leads you to a kitchen. There you see through the hole, nobody is there. You open the door."""))
            return 'hallwayspace'



        else:
            print("DOES NOT COMPUTE.")
            return 'basementroom'

class Hallway(Scene):
    def enter(self): # dedent takes away white spaces
        print(dedent("""
            - Once you get in the kitchen, there is a door on the left of you going straight outside also there is a hallway to the right to continue into the
           living room. Which way you going?
            """))

        action = input("> ")

        if action == "left":
            print(dedent("""
                A robber is there waiting and the lookout starts alerting the other robbers and they kill you. You died.
                """))
            return 'death' # return the death scene

        elif action == "right":
            print(dedent("""
            The robber hears you are coming so it starts preparing for a break, but you get quiet instantly making him think it is the floor sounding.
            ."""))
            return 'livingroom'
            # return the death scene

class LivingRoom(Scene):
    def enter(self): # dedent takes away white spaces
        print(dedent("""
        As you move around the living room. you discover that it leads to a ladder.  The ladder is somewhat unstable though it seemingly goes to another room. You do see a safe, and a box. You can 'climb' on the ladder or 'break' into the safe.
 What will you do climb or break?"""))

        action = input("> ")

        if action == "climb":
            print(dedent("""
            the ladder falls and you hit yourself on the head causing you to die from impact on the head.  You died.
                """))
            return 'death' # return the death scene

        elif action == "break":
            print(dedent("""
             You get the gun to kill the robber. You go up a rope and get to the attic  Phew.
            """))
            return 'atticroom'

class AtticRoom(Scene):
    def enter(self): # dedent takes away white spaces
        print(dedent("""Now you are at the attic, you see the robber. He is coming right at you? You have the gun and shoot him. You miss, that was your last bullet. What do you do now? You can PUNCH, RETREAT, TACKLE.""")) #  This is also the start of the game

        action = input("> ")

        if action == "TACKLE": # this is an input option in order to receive the text on lines 53-54
            print(dedent("""You tackle the robber!!! Now he loses the gun. You, grab his gun and shoot. HEAD SHOT!!! You beat the robber. You are victorious!!!"""))
            return 'finished' # return the death scene

        else:
            print("you're dead")
            return 'basementroom'

class Finished(Scene):
    def enter(self):
        print("You won! Good job.") # print this string
        return 'finished' # return finished scene when finished is called


class Map(object):#links scenes into story
    scenes = {
     'basementroom': Basement(),
     'livingroom': LivingRoom(),
     'hallwayspace': Hallway(),
     'atticroom': AtticRoom(),
     'death': Death(),
     'finished': Finished()
    } # store each scene by name in a dicitonary.  use Map.scenes to refer to a name
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('basementroom')
a_game = Engine(a_map)
a_game.play()
