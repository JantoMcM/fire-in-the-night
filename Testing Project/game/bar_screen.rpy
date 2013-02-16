## UI experiment to create permanent black bars on main window using screen language.

screen bars:
    frame:
        style "top_bar"
    frame:
        style "bottom_bar"
            
init -2 python: 
    style.top_bar.area = (0, 0, 1.0, 114) # sets xpos, ypos, width, height for item
    style.top_bar.background = "#000" # background colour is black
        
    style.bottom_bar.area = (0, 606, 1.0, 114) # sets xpos, ypos, width, height for item
    style.bottom_bar.background = "#000" # background colour is black