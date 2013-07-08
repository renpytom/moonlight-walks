## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = False
    config.debug_image_cache = False
    
    config.version = "2.2"
    
    ## These control the width and height of the screen.

    config.screen_width = 800
    config.screen_height = 600

    config.framerate = None
    
    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Moonlight Walks"
    config.window_icon = "icon.png"
    
    theme.ancient()
    theme.outline_bars("#0080c0", "#0080c0", "#00c0ff")
    
    style.slider.bar_resizing = False
    style.slider.thumb_offset = 3
    
    style.mm_root.background = Image('new/beach1a.jpg')
    style.gm_root.background = Image('new/beach3.jpg')

    style.button_text.hover_color = "#ff0"

    style.file_picker_button.background = Frame('saveslot.png', 16, 16)
    style.file_picker_button.xpadding = 2
    style.file_picker_button.ypadding = 2

    style.file_picker_text.color = "#00c0ff"
    style.file_picker_text.hover_color = "#ff0"
    style.file_picker_text.insensitive_color = "#c0c0c0"
    # style.file_picker_new.idle_color = "#ff8080"
    # style.file_picker_new.hover_color = "#ff4040"
    
    style.file_picker_nav_button.right_margin = 20
    
    style.frame.background = Frame('saveslot.png', 16, 16)
    style.frame.xpadding = 10
    style.frame.ypadding = 10

    style.mm_frame.background = Frame('saveslot.png', 16, 16)
    style.mm_frame.xpadding = 10
    style.mm_frame.ypadding = 10
    style.mm_frame.xpos = 0.5
    style.mm_frame.xanchor = 0.5
    style.mm_frame.ypos = 380
    style.mm_frame.yanchor = 0.0
    
    style.gm_nav_frame.background = Frame('saveslot.png', 16, 16)
    style.gm_nav_frame.xpadding = 10
    style.gm_nav_frame.ypadding = 10
    style.gm_nav_frame.xpos = 0.5
    style.gm_nav_frame.xanchor = 0.5

    style.pref_frame.background = Frame('saveslot.png', 16, 16)
    style.pref_frame.xpadding = 10
    style.pref_frame.ypadding = 10
    style.pref_frame.xpos = 0.5
    style.pref_frame.xanchor = 0.5
    
    style.pref_label_text.color = "#ff0"
    style.pref_label.xalign = .5
    style.yesno_prompt_text.color = "#ff0"
    # style.prefs_pref_choicebox.xalign = 0.5
    style.prefs_button.xalign = 0.5
    style.prefs_jump_button.xalign = 0.5
    # style.prefs_volume_box.xalign = 0.5
    # style.prefs_volume_slider.xalign = 0.5
    # style.prefs_slider.xalign = 0.5
    # style.prefs_slider.xmaximum = 230
    
    style.say_dialogue.rest_indent = 9

    style.window.background = Frame("background.png", 4, 4)
    
    # _remove_preference("Text Speed")
    # _remove_preference("Auto-Forward Time")

    # config.preferences["prefs_right"].append(config.all_preferences["Text Speed"])
    # config.preferences["prefs_right"].append(config.all_preferences["Auto-Forward Time"])

    config.developer = True
    
    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = False

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "waves.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.

    config.enter_transition = dissolve

    ## Used when exiting the game menu to the game.

    config.exit_transition = dissolve

    ## Used between screens of the game menu.

    config.intra_transition = Dissolve(.25)

    ## Used when entering the game menu from the main menu.

    config.main_game_transition = Dissolve(.25)

    ## Used when returning to the main menu from the game.

    config.game_main_transition = Dissolve(.25)

    ## Used when entering the main menu from the splashscreen.

    config.end_splash_transition = dissolve

    ## Used when entering the main menu after the game has ended.

    config.end_game_transition = fade

    ## Used when a game is loaded.

    config.after_load_transition = fade

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
    config.save_directory = "moonlight-2"
    
init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = True

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 0

