# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.


init 3 python:
    if renpy.variant('android'):
        style.button_text.size = 40
        style.button.xalign = 0.5
        style.button.xpadding = 7
        style.button.ypadding = 7

        style.default.size = 30
        style.pref_label_text.size = 30
        
        style.gm_nav_frame.yalign = 1.0
        style.gm_nav_frame.xalign = 1.0

        style.large_button_text.size = 30
        style.large_button_text.color = "#00c0ff"
        style.large_button_text.hover_color = "#ffff00"
        style.large_button_text.insensitive_color = "#c0c0c0"
        style.file_picker_button.xpadding = 20
        style.file_picker_button.ypadding = 20

        style.pref_slider.xmaximum = 700
        style.pref_slider.xalign = 0.5

        slideright = CropMove(0.5, "slideright")
        slideleft = CropMove(0.5, "slideleft")
        slideup = CropMove(0.5, "slideup")
        slidedown = CropMove(0.5, "slidedown")
        
        slideawayright = CropMove(0.5, "slideawayright")
        slideawayleft = CropMove(0.5, "slideawayleft")
        slideawayup = CropMove(0.5, "slideawayup")
        slideawaydown = CropMove(0.5, "slideawaydown")
        
        config.enter_transition = slideup
        config.exit_transition = slideawaydown

        style.window.yminimum = 200

        style.menu_choice.size = 35
        style.menu_choice_button.ymargin = 7
        
        
        
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    variant "android"
    
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        xalign 0.5
        yalign .98

        grid 2 3:
            style_group "mm"
            xfill True
            
            textbutton _("Start Game") action Start() default True
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Extras Menu") action Start("extras")
            textbutton _("Preferences") action ShowMenu("preferences")
            null
            textbutton _("Quit") action Quit(confirm=False)
        

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    variant "android"
    
    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"

        xmargin 5
        ymargin 5
        
        has grid 2 2:
            xfill True
            
        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")

        if renpy.context()._main_menu:
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Quit") action Quit()
        else:
            textbutton _("Save Game") action ShowMenu("save")            
            textbutton _("Main Menu") action MainMenu()


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
screen file_picker:

    variant "android"
    
    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"
            
            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            for i in range(1, 5):
                textbutton str(i):
                    action FilePage(i)
                    
            textbutton _("Next"):
                action FilePageNext()
                
        # Display a grid of file slots.
        grid 2 4:
            transpose True
            xfill True
            style_group "file_picker"
            
            for i in range(1, 9):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox
                    
                    # Format the description, and add it as text.
                    $ description = "%s-%d. %s" % (
                        FilePageName(),
                        i,
                        FileTime(i, empty=_("Empty Slot.")),
                        )

                    text description style "large_button_text"

                    
                    
screen save:

    variant "android"
    
    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    variant "android"

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:

    variant "android"
    
    tag menu

    # Include the navigation.
    use navigation

    vbox:            
        frame:
            style_group "pref"
            has vbox
            
            label _("Skip Messages")

            grid 2 1:
                xfill True
                textbutton _("Seen") action Preference("skip", "seen")
                textbutton _("All") action Preference("skip", "all")

        frame:
            style_group "pref"
            has vbox

            textbutton _("Begin Skipping") action Skip()

        frame:
            style_group "pref"
            has vbox

            label _("Text Speed")

            null height 20

            bar value Preference("text speed")
    

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        has vbox

        label _(message)

        hbox:
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action
