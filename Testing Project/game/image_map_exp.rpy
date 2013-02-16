init python:
    choice_1 = True
    choice_2 = False
    choice_3 = True
    choice_4 = True
    choice_5 = True
    choice_6 = True
    choice_7 = True

screen example_imagemap:    
    imagemap:
        auto "imagemap_%s.png" ## This tells the screen the name of the graphic set to use.
        
        if choice_1 == True:
            hotspot (54, 109, 48, 352) clicked Return ("choice_1")
        if choice_2 == True:   
            hotspot (137, 115, 48, 352) clicked Return ("choice_2")
        if choice_3 == True:
            hotspot (252, 75, 48, 352) clicked Return ("choice_3")
        if choice_4 == True:
            hotspot (324, 143, 48, 352) clicked Return ("choice_4")
        if choice_5 == True:
            hotspot (423, 98, 48, 352) clicked Return ("choice_5")
        if choice_6 == True:
            hotspot (503, 132, 48, 352) clicked Return ("choice_6")
        if choice_7 == True:
            hotspot (611, 121, 48, 352) clicked Return ("choice_7")


label image_map_exp:
## Test for working with Ren'Py's screen language for image maps.
   
    call screen example_imagemap
   
    $ result = _return
    
    if result == "choice_1":
        e "You picked 1!"
        menu: 
            "Switch off this choice?":
                $ choice_1 = False
            "Leave this choice on.":
                pass
        
    elif result == "choice_2":
        e "You picked 2!"
        menu: 
            "Switch off this choice?":
                $ choice_2 = False
            "Leave this choice on.":
                pass
        
    elif result == "choice_3":
        e "You picked 3!"
        menu: 
            "Switch off this choice?":
                $ choice_3 = False
            "Leave this choice on.":
                pass
        
    elif result == "choice_4":
        e "You picked 4!"
        menu: 
            "Switch off this choice?":
                $ choice_4 = False
            "Leave this choice on.":
                pass
        
    elif result == "choice_5":
        e "You picked 5!"
        menu: 
            "Switch off this choice?":
                $ choice_5 = False
            "Leave this choice on.":
                pass
                
    elif result == "choice_6":
        e "You picked 6!"
        menu: 
            "Switch off this choice?":
                $ choice_6 = False
            "Leave this choice on.":
                pass
        
    elif result == "choice_7":
        e "You picked 7!"
        menu: 
            "Switch off this choice?":
                $ choice_7 = False
            "Leave this choice on.":
                pass
                
    jump image_map_exp


        
