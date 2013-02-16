menu menu_ui_exp:
    "Choice 1":
        e "You chose number 1!You chose number 1! \n You chose number 1!You chose number 1!"
    "Choice 2":
        e "You chose number 2!"
    "Return":
        return
        
jump menu_ui_exp 

label second_menu:
    $ strange_var = "..."
    call screen my_menu(my_menu_bg=( Solid("#ccc") ), text_var="Header",  text_var_two="end line", buttons_list_var=[  ["first button", (None)],    ["second button", ( Jump ("far_away") ) ],      ["fird button", ( [  SetVariable("strange_var", "text value"), Return("1") ] ) ] ] )

    "Value is  [strange_var]"

    label far_away:
        "????"
        return
    
return