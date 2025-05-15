menu_helper = """
<MenuScreen>:
    id: menu
    name: 'menu'
    Image:
        source: "Assets/logo.png"
        opacity: 0.2
    MDLabel:
        text: 'Python Timer Cash'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.9}
    MDTextField: 
        id: lavoratore
        hint_text: "Inserisci EMAIL Lavoratore"
        mode: "round"
        helper_text_mode: "persistent"
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        size_hint_x: None
        width: 350
    MDTextField: 
        id: datore
        hint_text: "Inserisci EMAIL Datore (o cliente)"
        mode: "round"
        helper_text_mode: "persistent"
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        size_hint_x: None
        width: 350
    MDRectangleFlatButton:
        text: 'Add Worker'
        pos_hint: {'center_x':0.2, 'center_y':0.2}
        on_press: root.manager.current = 'profile'
    MDRoundFlatIconButton:
        text: "Start"
        icon: "send"
        text_color: "white"
        theme_bg_color: "Custom"
        line_color: "black"
        icon_color: "white"
        md_bg_color: "green"
        pos_hint: {'center_x':0.7, 'center_y':0.5}
        on_press: app.start()
    MDRoundFlatIconButton:
        text: "Stop"
        icon: "window-close"
        text_color: "white"
        theme_bg_color: "Custom"
        line_color: "black"
        icon_color: "white"
        md_bg_color: "red"
        pos_hint: {'center_x':0.3, 'center_y':0.5}
        on_press: app.stop()

"""