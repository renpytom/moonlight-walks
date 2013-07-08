init python:
    def extras_button(label, target, condition):
        if eval(condition):
            clicked = ui.jumps(target)
        else:
            clicked = None

        ui.textbutton(
            label,
            clicked=clicked,
            xalign=0.5,
            size_group="buttons")
        

    pytom = Character(None, what_style='say_thought')

    # Menus
    config.main_menu.insert(2, ("Extras Menu", "extras", "True"))

    style.hyperlink_text.underline = False
    style.hyperlink_text.hover_underline = True
    style.hyperlink_text.color = "#bbf"

init:
    image fanart deji = "contrib/deji.jpg"
    image fanart doomfest = "contrib/doomfest.jpg"
    image fanart mugenjohncel = "contrib/mugenjohncel.jpg"
    
        
label extras:

    play music "softwaves.ogg"

    scene dawn1
    with dissolve

label extras_loop:

    python:
        ui.frame(xalign=0.5, yalign=.75)
        ui.vbox()
        ui.text("Extras Menu", xalign=0.5)
        ui.text("")

        either = persistent.unlock_3 or persistent.unlock_4
        both = persistent.unlock_3 and persistent.unlock_4
        
        extras_button("Art Gallery", "gallery", "True")
        extras_button("Contributed Art", "contrib_art", "either") 
            
        if renpy.loadable("old/beach1b.jpg"):
            extras_button("Original Art", "original_art", "both")

        extras_button("Story Spoilers", "spoilers", "both")
        extras_button("Return", "extras_return", "True")
        
        ui.close()

        # This is in the wrong place, but here it prevents us from
        # rolling back from the menu.
        renpy.checkpoint()

        ui.interact(suppress_underlay=True)


label extras_return:
    return
        


# Code for the MW image gallery.
init:
    python:
        def gallery_button(x, y, page, condition):
            if eval(condition):
                ui.button(xpos=x, ypos=y, xanchor=0, yanchor=0, clicked=ui.jumps("gallery_" + page))
                ui.image("gal-" + page + ".png")
            else:
                ui.image("gal-locked.png", xpos=x, ypos=y, xanchor=0, yanchor=0)

label gallery:

    $ _game_menu_screen = None
    
    scene beach3

    python:
        # x 50, 300, 550
        # y 37, 224, 411
        
        gallery_button(50, 37, "dark", "persistent.unlock_dark")
        gallery_button(300, 37, "dawn", "persistent.unlock_dawn")
        gallery_button(550, 37, "end1", "persistent.unlock_1")

        gallery_button(50, 224, "end2", "persistent.unlock_2")
        gallery_button(300, 224, "end3", "persistent.unlock_3")
        gallery_button(550, 224, "end4", "persistent.unlock_4")

        gallery_button(50, 411, "dark_mary", "persistent.unlock_1 and persistent.unlock_2 and persistent.unlock_3 and persistent.unlock_4")
        gallery_button(300, 411, "dawn_mary", "persistent.unlock_1 and persistent.unlock_2 and persistent.unlock_3 and persistent.unlock_4")

        ui.textbutton("Return", xanchor=.5, yanchor=.5,
                      xpos=550 + 200 / 2, ypos=411 + 150 / 2,
                      xpadding=20, ypadding=15,
                      background=Frame('saveslot.png', 16, 16),
                      clicked=ui.returns(True),
                      )

        renpy.transition(dissolve)

        ui.interact()
        
    scene dawn1
    with dissolve

    $ _game_menu_screen = "save_screen"
    
    jump extras_loop
    
    
label gallery_dark:

    scene beach1 with dissolve
    $ renpy.pause(10)

    scene beach1 mary with dissolve
    $ renpy.pause(10)

    scene beach2 with dissolve
    $ renpy.pause(10)
    
    scene beach3 with dissolve
    $ renpy.pause(10)
    
    jump gallery

label gallery_dawn:
    
    scene dawn1 with dissolve
    $ renpy.pause(10)

    scene dawn2 with dissolve
    $ renpy.pause(10)
    
    scene dawn3 with dissolve
    $ renpy.pause(10)

    jump gallery

label gallery_end1:

    scene transfer with dissolve
    $ renpy.pause(10)

    scene moonpic with dissolve
    $ renpy.pause(10)

    scene girlpic with dissolve
    $ renpy.pause(10)

    scene nogirlpic with dissolve
    $ renpy.pause(10)

    scene bad_ending with dissolve
    $ renpy.pause(10)

    jump gallery

label gallery_end2:

    scene library with dissolve
    $ renpy.pause(10)

    scene beach1 nomoon with dissolve
    $ renpy.pause(10)

    scene bad_ending with dissolve
    $ renpy.pause(10)

    jump gallery

label gallery_end3:

    scene littlemary2 with dissolve
    $ renpy.pause(10)
    
    scene littlemary with dissolve
    $ renpy.pause(10)

    scene good_ending with dissolve
    $ renpy.pause(10)

    jump gallery

label gallery_end4:

    scene hospital1 with dissolve
    $ renpy.pause(10)
    
    scene hospital2 with dissolve
    $ renpy.pause(10)

    scene hospital3 with dissolve
    $ renpy.pause(10)

    scene heaven with dissolve
    $ renpy.pause(10)

    scene white with slowdissolve
    $ renpy.pause(1)

    scene good_ending with slowdissolve
    $ renpy.pause(10)

    jump gallery

label gallery_dawn_mary:

    scene dawn1
    show mary dawn confused smiling
    with dissolve
    $ renpy.pause(5)
    
    show mary dawn confused wistful with dissolve
    $ renpy.pause(5)

    show mary dawn wistful with dissolve
    $ renpy.pause(5)
    
    show mary dawn smiling with dissolve
    $ renpy.pause(5)
    
    show mary dawn vhappy with dissolve
    $ renpy.pause(5)

    jump gallery

label gallery_dark_mary:

    scene beach2
    show mary dark confused smiling
    with dissolve
    $ renpy.pause(5)
    
    show mary dark confused wistful with dissolve
    $ renpy.pause(5)

    show mary dark sad with dissolve
    $ renpy.pause(5)
    
    show mary dark crying with dissolve
    $ renpy.pause(5)
    
    show mary dark wistful with dissolve
    $ renpy.pause(5)
    
    show mary dark smiling with dissolve
    $ renpy.pause(5)
    
    show mary dark smiling b with dissolve
    $ renpy.pause(5)
    
    show mary dark laughing with dissolve
    $ renpy.pause(5)

    show mary dark vhappy with dissolve
    $ renpy.pause(5)
    
    show mary dark happy with dissolve
    $ renpy.pause(5)
    
    jump gallery

label original_art:

    pytom "I singlehandedly made the original version of Moonlight Walks in less than a month."

    pytom "While I'm proud of that achievement, it also meant that the original version of Moonlight Walks was limited to what I could accomplish, skill-wise, in a limited amount of time."

    pytom "While this new version of Moonlight Walks has been massively improved by the addition of Mugenjohncel's art, I will admit some sentimental attachment to those old images."

    $ oldart = True
    
    pytom "And so, as an extra I've included the ability to play Moonlight Walks using the original art."

    menu:

        "Would you like to play using the original art?"

        "Yes.":
            jump start

        "No.":
            pass


    $ oldart = False
    jump extras_loop
    
label contrib_art:

    pytom "In September 2008, when it was clear that this remake would soon be done, we put out a {a=http://lemmasoft.renai.us/forums/viewtopic.php?p=57621}call for art{/a} out on the Lemma Soft Forums."

    pytom "Within a few hours, Deji gave us the following:"

    scene fanart deji
    with dissolve
    $ renpy.pause()
    scene dawn1
    with dissolve

    pytom "Our next contribution is from Doomfest:"

    scene fanart doomfest
    with dissolve
    $ renpy.pause()
    scene dawn1
    with dissolve
    
    pytom "Our final contribution is from Mugenjohncel. And while an image from the official artist might technically be off-topic, it made us laugh enough to include it here."
    
    scene fanart mugenjohncel
    with dissolve
    $ renpy.pause()
    scene dawn1
    with dissolve

    pytom "I'd like to thank everyone who posted their art."
    
    jump extras_loop


label spoilers:

    scene beach1
    with dissolve

    pytom "In this section, I'll talk a little bit about the backstory behind Moonlight Walks, and where the inspiration for various things came from."

    pytom "Probably the most direct influence on Moonlight Walks was the Marvel 1602 comic book, which featured the character of Virginia Dare, the first child born in America to English parents."

    pytom "In reality, she disappeared with the Roanoke colony a few years after she was born. But that's only lead to a host of mythology springing up about her."

    pytom "I had been thinking this over for a few days when suddenly Moonlight Walks came to me, with ending 4 fully formed, while in the shower."

    pytom "Although the setup for Moonlight Walks was different than the Virginia Dare piece, a number of elements remain."

    pytom "For example, the story takes place on an island in the Atlantic. North Sand Island is intended to be an island in the Outer Banks of the coast of North Carolia, around where Roanoke is."

    pytom "The name Mary Harper was taken from 1790 census records of that region. I arrived at the name by combining a man's last name and a woman's first name, so as not to name someone who really lived."

    scene beach2
    with dissolve
    
    pytom "Mary died in a plague that hit the island in 1790."

    pytom "She was ten at the time. Her dream of getting married is what kept her around after her death."

    pytom "Her dress, or at least the version which you can see in the original art, was patterned after an actual wedding dress, but one from Ohio and about thirty years later."

    pytom "The game takes place in the summer of 2005. That means that Mary has been wandering the island for between 2804 and 2826 nights, or over seven years her time."

    pytom "She ages one day per full moon, so that makes her 17."

    pytom "I don't know what she does during the hours when it's not night, but she does seem to age them. I guess she sleeps."

    pytom "Our main character is probably 18, as he's in between high school and college. That's probably the age when a person has the least responsibility, and is the most free to follow his dreams."

    scene beach3
    with dissolve
    
    pytom "In the third ending, Mary gets married, fulfilling the condition that's keeping her on earth. Once this is done, she can rest in peace."

    pytom "Of course, the whole thing about common law marriage is BS, at least by modern laws, but Mary believes it, and that's what counts."

    pytom "Although I didn't really mention this directly, in Ending three the main character winds up marrying one of the librarians that helps him with his research."

    pytom "In ending four, Mary decides that she wants to be with the point-of-view character more than she wants to stay on earth, and so she leaves with him."

    pytom "Ending four is what motivated me to make the game, while Ending three was a relatively late addition upon seeing that the player could make a choice."

    scene dawn1
    with dissolve

    pytom "Thank you for taking the time to read these notes, and once again, thank you for playing Moonlight Walks.\n\nPyTom, Kings Park, January 2009"

    jump extras_loop
    
    
    
