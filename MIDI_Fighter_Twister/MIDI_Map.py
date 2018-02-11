# Brought to you by st4rchild with the help of Hanz Petrov @ http://remotescripts.blogspot.com
# Avoid using tabs for indentation, use spaces.

### SIDE BUTTONS CONFIG

SIDE_BUTTONS_CHANNEL = 3

# midi values for the buttons
TOP_LEFT_SIDE_BTN_VAL = 8
BTM_LEFT_SIDE_BTN_VAL = 10
TOP_RITE_SIDE_BTN_VAL = 11
BTM_RITE_SIDE_BTN_VAL = 13

# order the buttons are added in MIDI_Fighter_Twister.py
TOP_LEFT_SIDE_BTN = 0
BTM_LEFT_SIDE_BTN = 1
TOP_RITE_SIDE_BTN = 2
BTM_RITE_SIDE_BTN = 3

# Combination Mode offsets
# ------------------------

TRACK_OFFSET = -1 #offset from the left of linked session origin; set to -1 for auto-joining of multiple instances
SCENE_OFFSET = 0 #offset from the top of linked session origin (no auto-join)

# Buttons / Pads
# -------------
# Valid Note/CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments are permitted

BUTTONCHANNEL = 1 #Channel assignment for all mapped buttons/pads; valid range is 0 to 15 ; 0=1, 1=2 etc.
MESSAGETYPE = 1 #Message type for buttons/pads; set to 0 for MIDI Notes, 1 for CCs.
        #When using CCs for buttons/pads, set BUTTONCHANNEL and SLIDERCHANNEL to different values.

# General
PLAY = -1 #Global play
STOP = -1 #Global stop
REC = -1 #Global record
TAPTEMPO = -1 #Tap tempo
NUDGEUP = -1 #Tempo Nudge Up
NUDGEDOWN = -1 #Tempo Nudge Down
UNDO = -1 #Undo
REDO = -1 #Redo
LOOP = -1 #Loop on/off
PUNCHIN = -1 #Punch in
PUNCHOUT = -1 #Punch out
OVERDUB = -1 #Overdub on/off
METRONOME = -1 #Metronome on/off
RECQUANT = -1 #Record quantization on/off
DETAILVIEW = -1 #Detail view switch
CLIPTRACKVIEW = -1 #Clip/Track view switch

# Device Control
DEVICELOCK = 24 #Device Lock (lock "blue hand")
DEVICEONOFF = 27 #Device on/off
DEVICENAVLEFT = 28 #Device nav left
DEVICENAVRIGHT = 29 #Device nav right
DEVICEBANKNAVLEFT = 30 #Device bank nav left
DEVICEBANKNAVRIGHT = 31 #Device bank nav right
DEVICEBANK = (-1, #Bank 1 #All 8 banks must be assigned to positive values in order for bank selection to work
              -1, #Bank 2
              -1, #Bank 3
              -1, #Bank 4
              -1, #Bank 5
              -1, #Bank 6
              -1, #Bank 7
              -1, #Bank 8
              )

# Arrangement View Controls
SEEKFWD = -1 #Seek forward
SEEKRWD = -1 #Seek rewind

# Session Navigation (aka "red box")

# defined at the top
SESSIONLEFT = TOP_LEFT_SIDE_BTN #Session left
SESSIONRIGHT = BTM_LEFT_SIDE_BTN #Session right
SESSIONUP = TOP_RITE_SIDE_BTN #Session up
SESSIONDOWN = BTM_RITE_SIDE_BTN #Session down

ZOOMUP = -1 #Session Zoom up
ZOOMDOWN = -1 #Session Zoom down
ZOOMLEFT = -1 #Session Zoom left
ZOOMRIGHT = -1 #Session Zoom right

# Track Navigation
TRACKLEFT = -1 #Track left
TRACKRIGHT = -1 #Track right

# Scene Navigation
SCENEUP = -1 #Scene down
SCENEDN = -1 #Scene up

# Scene Launch
SELSCENELAUNCH = -1 #Selected scene launch
SCENELAUNCH = (3, #Scene 1 Launch
               7, #Scene 2
               11, #Scene 3
               )

# Clip Launch / Stop
SELCLIPLAUNCH = -1 #Selected clip launch
STOPALLCLIPS = -1 #Stop all clips

# 8x8 Matrix note assignments
# Track no.:     1   2   3   4   5   6   7   8
CLIPNOTEMAP = ((0, 1, 2), #Row 1
               (4, 5, 6), #Row 2
               (8, 9, 10), #Row 3
               )

# Track Control
MASTERSEL = -1 #Master track select
TRACKSTOP = (-1, #Track 1 Clip Stop
             -1, #Track 2
             -1, #Track 3
             )
TRACKSEL = (-1, #Track 1 Select
            -1, #Track 2
            -1, #Track 3
            )
TRACKMUTE = (12, #Track 1 On/Off
             13, #Track 2
             14, #Track 3
             )
TRACKSOLO = (-1, #Track 1 Solo
             -1, #Track 2
             -1, #Track 3
             )
TRACKREC = (-1, #Track 1 Record
            -1, #Track 2
            -1, #Track 3
            )


# Pad Translations for Drum Rack

PADCHANNEL = 0 # MIDI channel for Drum Rack notes
DRUM_PADS = (-1, -1, -1, -1, # MIDI note numbers for 4 x 4 Drum Rack
             -1, -1, -1, -1, # Mapping will be disabled if any notes are set to -1
             -1, -1, -1, -1, # Notes will be "swallowed" if already mapped elsewhere
             -1, -1, -1, -1,
             )

# Sliders / Knobs
# ---------------
# Valid CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments will be ignored

SLIDERCHANNEL = 0 #Channel assignment for all mapped CCs; valid range is 0 to 15
TEMPO_TOP = 180.0 # Upper limit of tempo control in BPM (max is 999)
TEMPO_BOTTOM = 80.0 # Lower limit of tempo control in BPM (min is 0)

TEMPOCONTROL = -1 #Tempo control CC assignment; control range is set above
MASTERVOLUME = -1 #Master track volume
CUELEVEL = -1 #Cue level control
CROSSFADER = -1 #Crossfader control

TRACKVOL = (12, #Track 1 Volume
            13, #Track 2
            14, #Track 3
            )
TRACKPAN = (8, #Track 1 Pan
            9, #Track 2
            10, #Track 3
            )
TRACKSENDA = (4, #Track 1 Send A
              5, #Track 2
              6, #Track 3
              )
TRACKSENDB = (0, #Track 1 Send B
              1, #Track 2
              2, #Track 3
              )
TRACKSENDC = (-1, #Track 1 Send C
              -1, #Track 2
              -1, #Track 3
              )
PARAMCONTROL = (24, #Param 1 #All 8 params must be assigned to positive values in order for param control to work
                25, #Param 2
                26, #Param 3
                27, #Param 4
                28, #Param 5
                29, #Param 6
                30, #Param 7
                31, #Param 8
                )
