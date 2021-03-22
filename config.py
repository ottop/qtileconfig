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

#Configuration by Otto Petäjä

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401
from os.path import expanduser
from subprocess import call

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod],"Return", lazy.spawn("xterm")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod,"shift"],"Escape", lazy.spawn("rofi -show power-menu -modi power-menu:~/.local/bin/rofi-power-menu: ")),
    
    Key([mod], "Escape", lazy.spawn("rofi -show drun")),
    Key([], "Print", lazy.spawn("gnome-screenshot --delay=3")),
    Key([mod],"Right",lazy.screen.next_group()),
    Key([mod],"Left",lazy.screen.prev_group()),
    Key([],"XF86AudioLowerVolume",lazy.spawn("pactl set-sink-volume 0 -3%")),
    Key([],"XF86AudioRaiseVolume",lazy.spawn("pactl set-sink-volume 0 +3%")),
    Key([],"XF86AudioMute",lazy.spawn("pactl set-sink-mute 0 toggle")),
]

groups = [Group(i) for i in "1234"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.RatioTile(border_width=0),
    layout.Max(),
    #layout.Stack(num_stacks=4),
    # Try more layouts by unleashing below layouts.
    #layout.Bsp(),
    #layout.Columns(),
    #layout.Matrix(),
    #layout.MonadTall(),
    #layout.MonadWide(),

    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font='mono',
    fontsize=12,
    padding=3,
    foreground="c0c0c0"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(borderwidth=8,background="323232",inactive="ffffff",margin_x=0,rounded=False,highlight_method="block",this_current_screen_border="242424"),
                widget.TaskList(background="323232",border="242424",max_title_width=200,rounded=False,margin_y=0,margin_x=0,margin=0,icon_size=9,highlight_method="block"),
                widget.Clipboard(background="323232"),
                widget.CPUGraph(background="323232",width=20,graph_color="58c928",border_width=0,margin_x=2.5),
                widget.MemoryGraph(background="323232",width=20,graph_color="b9c928",border_width=0,margin_x=2.5),
                widget.HDDBusyGraph(background="323232",width=20,graph_color="c99928",border_width=0,margin_x=2.5),
                widget.NetGraph(background="323232",width=20,graph_color="c94328",border_width=0,margin_x=2.5),
                widget.Spacer(length=2,background="323232"),
                widget.Sep(background="323232",foreground="666666",padding=5),
                widget.Clock(format='%m.%d.%Y - %H:%M',background="323232",),
                widget.Spacer(length=2,background="323232"),
            ],
            18,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_width=0,float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup
def autostart():
    home = expanduser('~/.config/qtile/autostart.sh')
    call([home])
