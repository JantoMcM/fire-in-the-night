# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image imagemap ground = "imagemap_ground.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:

menu:
    "Image Map Experiment":
        call image_map_exp
	"Event Manager Experiment.":
		call event_manager_exp
    "End Game":
        return
        
jump start

return