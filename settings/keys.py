# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy
import os, subprocess


mod = "mod4"
home = os.path.expanduser('~')

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "space",  lazy.layout.next()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "Right", lazy.layout.grow()),
    ([mod, "shift"], "Left", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    ([mod, "shift"], "Up", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),
    ([mod], "Escape", lazy.spawn('xkill')),
    ([mod, "shift"], "space", lazy.layout.flip()),
    ([mod, "shift"],
        "a",
        lazy.spawncmd(),
    ),
    ([mod], 
	    "n", 
	    lazy.layout.normalize(),
    ),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "u", lazy.spawn('rofi -show combi')),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("brave")),

    # File Explorer & Ranger
    ([mod], "e", lazy.spawn("thunar")),
    ([mod, "shift"], "e", lazy.spawn("alacritty -e ranger")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("deepin-screenshot")),
    #([mod, "shift"], "s", lazy.spawn("scrot -s")),

    #Visual Studio Code 
    ([mod], "c", lazy.spawn("code")),
    
    #networkmanager_dmenu
    ([mod], "i", lazy.spawn("networkmanager_dmenu")),

    #LogOut
    ([mod], "x", lazy.spawn('nwg-bar')),
    ([mod,
        "shift"], 
	    "q", 
	    lazy.spawn(home + '/.config/qtile/shutdown.sh'),
	),

    #Cpliboard
    #([mod],"v", lazy.spawn('rofi -modi "clipboard:greenclip print" -show clipboard'))

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    #Media Control
    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    ([], "XF86AudioNext", lazy.spawn("playerctl next")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    ([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
