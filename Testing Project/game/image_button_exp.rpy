##  
init python: 

    buttonlist = [[20, 430, "button_1", [SetVariable("button_1_press", True), Hide("button_1"), Jump("button_1_result")]],
                  [40, 300, "button_2", [SetVariable("button_2_press", True), Hide("button_2"), Jump("button_2_result")]]]

screen buttons:
    modal False
    for b in buttonlist:
        imagebutton:
            xpos b[0] ypos b[1]
            auto (b[2] + "_%s.png")
            action b[3]

label image_button_exp:
    
label room:
    scene imagemap ground
    
    show screen buttons
        
    # whatever else happens in this room
    
    $ renpy.pause()
    jump room

label button_1_result:    
    e "You pressed button 1!"
    jump room
    
label button_2_result:
    e "You pressed button 2!"
    jump room
    

    

    
    
