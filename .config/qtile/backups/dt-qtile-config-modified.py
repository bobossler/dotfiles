# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "firefox" # My browser of choice

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod, "shift"], "Return",
             lazy.spawn("dm-run"),
             desc='Run Launcher'
             ),
         Key([mod], "x",
             lazy.spawn("rofi -show drun"),
             desc='Run Launcher'
             ),
         Key([mod], "p",
             lazy.spawn("powermenu.sh"),
             desc='Logout/Power menu'
             ),
         Key([mod], "b",
             lazy.spawn(myBrowser),
             desc='Firefox'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key(["control", "shift"], "e",
             lazy.spawn("emacsclient -c -a emacs"),
             desc='Doom Emacs'
             ),
         ### Switch focus to specific monitor (out of two)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         # Emacs programs launched using the key chord CTRL+e followed by 'key'
         KeyChord([mod],"e", [
             Key([], "e",
                 lazy.spawn("emacsclient -c -a 'emacs'"),
                 desc='Emacsclient Dashboard'
                 ),
             Key([], "a",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(emms)' --eval '(emms-play-directory-tree \"~/Music/\")'"),
                 desc='Emacsclient EMMS (music)'
                 ),
             Key([], "b",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
                 desc='Emacsclient Ibuffer'
                 ),
             Key([], "d",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
                 desc='Emacsclient Dired'
                 ),
             Key([], "i",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
                 desc='Emacsclient ERC (IRC)'
                 ),
             Key([], "n",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
                 desc='Emacsclient Elfeed (RSS)'
                 ),
             Key([], "s",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
                 desc='Emacsclient Eshell'
                 ),
             Key([], "v",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
                 desc='Emacsclient Vterm'
                 ),
             Key([], "w",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(doom/window-maximize-buffer(eww \"distro.tube\"))'"),
                 desc='Emacsclient EWW Browser'
                 )
         ]),
         # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
         #KeyChord([mod], "p", [
         #    Key([], "h",
         #        lazy.spawn("dm-hub"),
         #        desc='List all dmscripts'
         #        ),
         #    Key([], "a",
         #        lazy.spawn("dm-sounds"),
         #        desc='Choose ambient sound'
         #        ),
         #    Key([], "b",
         #        lazy.spawn("dm-setbg"),
         #        desc='Set background'
         #        ),
         #    Key([], "c",
         #        lazy.spawn("dtos-colorscheme"),
         #        desc='Choose color scheme'
         #        ),
         #    Key([], "e",
         #        lazy.spawn("dm-confedit"),
         #        desc='Choose a config file to edit'
         #        ),
         #    Key([], "i",
         #        lazy.spawn("dm-maim"),
         #        desc='Take a screenshot'
         #        ),
         #    Key([], "k",
         #        lazy.spawn("dm-kill"),
         #        desc='Kill processes '
         #        ),
         #    Key([], "m",
         #        lazy.spawn("dm-man"),
         #        desc='View manpages'
         #        ),
         #    Key([], "n",
         #        lazy.spawn("dm-note"),
         #        desc='Store and copy notes'
         #        ),
         #    Key([], "o",
         #        lazy.spawn("dm-bookman"),
         #        desc='Browser bookmarks'
         #        ),
         #    Key([], "p",
         #        lazy.spawn("passmenu -p \"Pass: \""),
         #        desc='Logout menu'
         #        ),
         #    Key([], "q",
         #        lazy.spawn("dm-logout"),
         #        desc='Logout menu'
         #        ),
         #    Key([], "r",
         #        lazy.spawn("dm-radio"),
         #        desc='Listen to online radio'
         #        ),
         #    Key([], "s",
         #        lazy.spawn("dm-websearch"),
         #        desc='Search various engines'
         #        ),
         #    Key([], "t",
         #        lazy.spawn("dm-translate"),
         #        desc='Translate text'
         #        )
         #])
]

groups = [Group("DEV", layout='monadtall'),
          Group("WWW", layout='monadtall'),
          Group("SYS", layout='monadtall'),
          Group("SYS", layout='monadtall'),
          Group("DOC", layout='monadtall'),
          Group("VBOX", layout='monadtall'),
          Group("CHAT", layout='monadtall'),
          Group("MUS", layout='monadtall'),
          Group("VID", layout='monadtall'),
          Group("GFX", layout='floating')]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "c678dd",
         active_fg = "000000",
         inactive_bg = "a9a1e1",
         inactive_fg = "1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize = 10,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/python-white.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)}
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 9,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
             widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 5
                       ),
             widget.TextBox(
                       text = '|',
                       font = "Ubuntu Mono",
                       background = colors[0],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
#              widget.Wttr(
#                      location = {
#                          '60504': 'Aurora'
#                      },
#                      format = '%C+%t(%f)+%w',
#                      update_interval = 1800
#                      ),
              widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
             widget.Net(
                       interface = "eno1",
                       format = 'Net: {down} ↓↑ {up}',
                       foreground = colors[3],
                       background = colors[0],
                       padding = 5,
                       decorations=[
                           BorderDecoration(
                               colour = colors[3],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.ThermalSensor(
                       foreground = colors[4],
                       background = colors[0],
                       threshold = 90,
                       fmt = 'Temp: {}',
                       padding = 5,
                       decorations=[
                           BorderDecoration(
                               colour = colors[4],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "Updates: {updates} ",
                       foreground = colors[5],
                       colour_have_updates = colors[5],
                       colour_no_updates = colors[5],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       padding = 5,
                       background = colors[0],
                       decorations=[
                           BorderDecoration(
                               colour = colors[5],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.Memory(
                       foreground = colors[9],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                       fmt = 'Mem: {}',
                       padding = 5,
                       decorations=[
                           BorderDecoration(
                               colour = colors[9],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.Volume(
                       foreground = colors[7],
                       background = colors[0],
                       fmt = 'Vol: {}',
                       padding = 5,
                       decorations=[
                           BorderDecoration(
                               colour = colors[7],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.KeyboardLayout(
                       foreground = colors[8],
                       background = colors[0],
                       fmt = 'Keyboard: {}',
                       padding = 5,
                       decorations=[
                           BorderDecoration(
                               colour = colors[8],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.AnalogueClock(
                       background = colors[0],
                       face_shape = "square",
                       face_background = colors[6],
                       face_border_colour = colors[6],
                       face_border_width = 4,
                       padding = 5
                       ),
              widget.Clock(
                       foreground = colors[6],
                       background = colors[0],
                       format = "%A, %B %d - %H:%M ",
                       decorations=[
                           BorderDecoration(
                               colour = colors[6],
                               border_width = [0, 0, 2, 0],
                               padding_x = 5,
                               padding_y = None,
                           )
                       ],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[9:10]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
