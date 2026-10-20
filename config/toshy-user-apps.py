

keymap("User hardware keys", {
    # PUT UNIVERSAL REMAPS FOR HARDWARE KEYS HERE
    # KEYMAP WILL BE ACTIVE IN ALL DESKTOP ENVIRONMENTS/DISTROS


}, when = lambda ctx:
    cnfg.screen_has_focus and
    not ctx_app_is_remote
)

if DESKTOP_ENV == 'cosmic':
    keymap("User COSMIC Terminal tabs", {
        C("LC-Tab"):                [bind,C("C-Tab")],              # Ctrl+Tab: next tab
        C("Shift-LC-Tab"):          [bind,C("Shift-C-Tab")],        # Ctrl+Shift+Tab: prior tab
        C("Shift-RC-Right_Brace"):  [bind,C("C-Tab")],              # Cmd+Shift+]: next tab
        C("Shift-RC-Left_Brace"):   [bind,C("Shift-C-Tab")],        # Cmd+Shift+[: prior tab
        C("Shift-RC-Right"):        [bind,C("C-Tab")],              # Cmd+Shift+Right: next tab
        C("Shift-RC-Left"):         [bind,C("Shift-C-Tab")],        # Cmd+Shift+Left: prior tab
        C("RC-1"):                  C("C-Shift-1"),                 # Cmd+1..9: go to tab by position
        C("RC-2"):                  C("C-Shift-2"),
        C("RC-3"):                  C("C-Shift-3"),
        C("RC-4"):                  C("C-Shift-4"),
        C("RC-5"):                  C("C-Shift-5"),
        C("RC-6"):                  C("C-Shift-6"),
        C("RC-7"):                  C("C-Shift-7"),
        C("RC-8"):                  C("C-Shift-8"),
        C("RC-9"):                  C("C-Shift-9"),
        C("LC-v"):                  C("Alt-v"),                     # Ctrl+V: Claude Code image paste (Ctrl+V is bound to text Paste for Wispr)
    }, when = lambda ctx:
        cnfg.screen_has_focus and
        ctx_ovl_terminal_ergo and
        hmp_is_term_cosmic_term(ctx)
    )

    # Mac Ctrl is "Super" in GUI apps and "LC" in terminals, so both are mapped.
    # Super-C-Alt-m/f are custom COSMIC shortcuts (Minimize, system monitor).
    keymap("User COSMIC window management", {
        C("RC-h"):                  C("Super-C-Alt-m"),             # Cmd+H: minimize
        C("RC-m"):                  C("Super-C-Alt-m"),             # Cmd+M: minimize
        C("Alt-RC-Esc"):            C("Super-C-Alt-f"),             # Cmd+Opt+Esc: force quit (system monitor)
        C("Super-RC-q"):            C("Super-Esc"),                 # Ctrl+Cmd+Q: lock screen
        C("LC-RC-q"):               C("Super-Esc"),                 # Ctrl+Cmd+Q: lock screen
        C("Shift-RC-q"):            C("Super-Shift-Esc"),           # Cmd+Shift+Q: log out
        C("Super-Up"):              C("Super-w"),                   # Ctrl+Up: workspace overview
        C("LC-Up"):                 C("Super-w"),                   # Ctrl+Up: workspace overview
        C("Super-Left"):            [bind,C("Super-C-Left")],       # Ctrl+Left: previous workspace
        C("Super-Right"):           [bind,C("Super-C-Right")],      # Ctrl+Right: next workspace
        C("LC-Left"):               [bind,C("Super-C-Left")],       # Ctrl+Left: previous workspace
        C("LC-Right"):              [bind,C("Super-C-Right")],      # Ctrl+Right: next workspace
        C("Super-RC-Up"):           C("Super-m"),                   # Ctrl+Cmd+Up: maximize toggle
        C("Super-RC-Left"):         C("Super-Shift-Left"),          # Ctrl+Cmd+Left: snap to left half
        C("Super-RC-Right"):        C("Super-Shift-Right"),         # Ctrl+Cmd+Right: snap to right half
        C("LC-RC-Up"):              C("Super-m"),
        C("LC-RC-Left"):            C("Super-Shift-Left"),
        C("LC-RC-Right"):           C("Super-Shift-Right"),
        C("Super-Alt-Left"):        C("Super-Left"),                # Ctrl+Opt+arrows: focus window (tiling)
        C("Super-Alt-Right"):       C("Super-Right"),
        C("Super-Alt-Up"):          C("Super-Up"),
        C("Super-Alt-Down"):        C("Super-Down"),
        C("LC-Alt-Left"):           C("Super-Left"),
        C("LC-Alt-Right"):          C("Super-Right"),
        C("LC-Alt-Up"):             C("Super-Up"),
        C("LC-Alt-Down"):           C("Super-Down"),
        C("Super-Alt-a"):           C("Super-a"),                   # Ctrl+Opt+A: App Library
        C("Super-Alt-f"):           C("Super-f"),                   # Ctrl+Opt+F: Files
        C("Super-Alt-b"):           C("Super-b"),                   # Ctrl+Opt+B: web browser
        C("LC-Alt-a"):              C("Super-a"),
        C("LC-Alt-f"):              C("Super-f"),
        C("LC-Alt-b"):              C("Super-b"),
    }, when = lambda ctx:
        cnfg.screen_has_focus and
        not ctx_app_is_remote
    )

