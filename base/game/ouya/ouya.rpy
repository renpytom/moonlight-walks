screen ouya_instructions:
    
    vbox:
        xalign 0.5
        yalign 0.5
    
        text "Controls" size 60 xoffset -80
    
        null height 15
    
        text "{image=ouya/OUYA_O.png} advances dialogue."
        null height 5
        text "{image=ouya/OUYA_LS_DOWN.png} and {image=ouya/OUYA_O.png} select choices."
        null height 5
        text "{image=ouya/OUYA_A.png} shows prior dialogue."
        null height 5
        text "{image=ouya/OUYA_SYSTEM.png} shows the game menu."
        
        null height 40
    
        text "Press {image=ouya/OUYA_O.png} to continue." xoffset 80 xalign 1.0


label ouya_instructions_once:
    
    if persistent.ouya_instructions:
        return 
        
    $ persistent.ouya_instructions = True

label ouya_instructions:
    
    if not renpy.variant('ouya'):
        return
        
    scene black
        
    show screen ouya_instructions
    with dissolve
    pause
    hide screen ouya_instructions
    with dissolve

    return
    