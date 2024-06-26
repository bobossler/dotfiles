# Copyright (c) 2010 Aldo Cortesi
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

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.scripts.main import VERSION
mod = "mod4"
terminal = guess_terminal()
myBrowser = "firefox"

keys = [
    ### Window focus controls
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    ### Essentials
    Key([mod], "m", lazy.layout.maximize(), desc='toggle window between minimum and maximum sizes'),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "x", lazy.spawn("rofi -show drun"), desc='Run launcher'),
    Key([mod], "p", lazy.spawn("powermenu.sh"), desc='Logout/Power menu'),
    Key([mod], "b", lazy.spawn(myBrowser), desc='Firefox'),
    Key(["control", "shift"], "e", lazy.spawn("emacsclient -c -a emacs"), desc='Doom Emacs'),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc='Kill focused window'),
    Key([mod, "shift"], "r", lazy.reload_config(), desc='Reload the config'),
    Key([mod, "control"], "r", lazy.restart, desc='Restart Qtile'),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([], 'F11', lazy.group['sp1'].dropdown_toggle('mc')),
    Key([], 'F12', lazy.group['sp2'].dropdown_toggle('ranger'))
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group("1"),
          Group("2", matches=[Match(wm_class=["firefox"])]),
          Group("3"),
          Group("4", matches=[Match(wm_class=["pcmanfm"])]),
          Group("5", matches=[Match(wm_class=["spotify"])]),
          Group("6"),
          Group("7"),
          Group("8", matches=[Match(wm_class=["mpv"])]),
          Group("9"),
          ScratchPad("sp1", [
              DropDown("mc", "alacritty -e 'mc'", height=0.6, opacity=1) ]),
          ScratchPad("sp2", [
              DropDown("ranger", "alacritty -e 'ranger'", height=0.6, opacity=1) ])
         ]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
    if i.name == "9":
        break

colors = [
    ["#282a36", "#282a36"],
    ["#1c1f24", "#1c1f24"],
    ["#dfdfdf", "#dfdfdf"],
    ["#ff6c6b", "#ff6c6b"],
    ["#98be65", "#98be65"],
    ["#da8548", "#da8548"],
    ["#51afef", "#51afef"],
    ["#c678dd", "#c678dd"],
    ["#46d9ff", "#46d9ff"],
    ["#a9a1e1", "#a9a1e1"]
]

layout_theme = {
        "border_width": 2,
        "margin": 8,
        "border_focus": "#bd93f9",
        "border_normal": "#1d2330"
        }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
        font = "Hack Nerd Font Mono",
        fontsize = 14,
        sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize = 12,
        border_width = 2,
        bg_color = colors[0],
        active_bg = colors[7],
        active_fg = "000000",
        inactive_bg = colors[9],
        inactive_fg = colors[1],
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
    # Try more layouts by unleashing below layouts.
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    #font = "Ubuntu Bold",
    font = "JetBrainsMono Nerd Font Bold",
    #font = "FontAwesome",
    #font = "Inconsolata Nerd Font Mono",
    #font = "Hack Nerd Font Mono Bold",
    fontsize = 16,
    padding = 2,
    backgound = colors[2]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background = colors[1],
                    scale = 0.6
                ),
                widget.GroupBox(),
                widget.Prompt(),
                widget.Spacer(
                    length = bar.STRETCH
                ),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p",
                    foreground = colors[8]
                ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Sep(
                    linewidth = 2,
                    padding = 4
                ),
                widget.OpenWeather(
                    app_key = '33dbf77ac9d2c2a105a442ab0a5ce6b2',
                    foreground = colors[8],
                    format = '{location_city}: {icon} {temp}{units_temperature} {wind_speed} {units_wind_speed} {wind_direction}',
                    metric = False,
                    padding = 8,
                    update_interval = 1800,
                    zip = 60504
                ),
                widget.Spacer(
                    length = bar.STRETCH
                ),
                widget.Sep(
                    linewidth = 2,
                    padding = 4
                ),
                widget.ThermalSensor(
                    tag_sensor = 'Core 0',
                    foreground = colors[8],
                    format = '{tag}: {temp:.0f}{unit}',
                    padding = 8
                ),
                widget.Sep(
                    linewidth = 2,
                    padding = 4
                ),
                widget.DF(warn_space=99),
                widget.Sep(
                    linewidth = 2,
                    padding = 4
                ),
                widget.Systray(),
                widget.QuickExit(
                    background = colors[1],
                    default_text='[X]',
                    fontsize = 12,
                    countdown_format='[{}]'
                ),
            ],
            background = colors[0],
            opacity = 0.85,
            size = 28
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background = colors[1],
                    scale = 0.6
                ),
                widget.GroupBox(),
                widget.Prompt(),
                #widget.WindowName(),
                widget.Spacer(
                    length = bar.STRETCH
                ),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p",
                    foreground = colors[8],
                    padding = 8
                ),
                widget.Sep(
                    linewidth = 2,
                    padding = 4
                ),
                widget.OpenWeather(
                    app_key = '33dbf77ac9d2c2a105a442ab0a5ce6b2',
                    #cityid = '',
                    foreground = colors[8],
                    format = '{location_city}: {icon} {temp}{units_temperature} {wind_speed} {units_wind_speed} {wind_direction}',
                    metric = False,
                    padding = 8,
                    update_interval = 1800,
                    zip = 60504
                ),
                widget.Spacer(
                    length = bar.STRETCH
                ),
                widget.Sep(
                    linewidth = 2,
                    padding = 4
                ),
                #widget.CPU(
                #    background = colors[5],
                #    foreground = colors[0],
                #    format = 'CPU:{load_percent}%'
                #),
                #widget.Sep(
                #    linewidth = 2,
                #    padding = 4
                #),
                #widget.Memory(
                #    background = colors[4],
                #    foreground = colors[0],
                #    fmt = 'Mem:{}',
                #    format = '{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
                #    measure_mem = 'G'
                #),
                #widget.Sep(
                #    linewidth = 2,
                #    padding = 4
                #),
                #widget.Mpris2(
                #    max_chars = 36,
                #    padding = 8
                #),
                #widget.Sep(
                #    linewidth = 2,
                #    padding = 4
                #),
                widget.ThermalSensor(
                    tag_sensor = 'Core 1',
                    foreground = colors[8],
                    format = '{tag}: {temp:.0f}{unit}',
                    padding = 8,
                ),
                widget.Sep(
                    linewidth = 2,
                    padding = 4
                ),
                #widget.CapsNumLockIndicator(),
                #widget.Sep(
                #    linewidth = 2,
                #    padding = 4
                #),
                widget.DF(warn_space=99),
                widget.QuickExit(
                    background = colors[1],
                    default_text='[X]',
                    fontsize = 12,
                    countdown_format='[{}]'
                ),
            ],
            background=colors[0],
            opacity=0.85,
            size=24
        ),
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="mpv"),  # mpv
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Autostart Hook
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
#wmname = "LG3D"
wmname = f"Qtile {VERSION}"
