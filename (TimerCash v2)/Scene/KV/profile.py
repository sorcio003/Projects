profile_helper = """
<ProfileScreen>:
    id: profile
    name: 'profile'
    MDTextField: 
        id: nome
        hint_text: "Inserisci Nome"
        helper_text_mode: "persistent"
        pos_hint: {'center_x':0.5, 'center_y':0.8}
        size_hint_x: None
        width: 200
    MDTextField: 
        id: cognome
        hint_text: "Inserisci Cognome"
        helper_text_mode: "persistent"
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        size_hint_x: None
        width: 200
    MDTextField: 
        id: type_work
        hint_text: "Dettagli Lavoro"
        helper_text_mode: "persistent"
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        size_hint_x: None
        width: 200
    MDTextField: 
        id: paga
        hint_text: "Paga Oraria"
        helper_text_mode: "persistent"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint_x: None
        width: 100
    MDLabel:
        text: 'Python Timer Cash'
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.34}
    MDLabel:
        text: 'credit by Drake'
        halign: 'center'
        font_style: "Caption"
        pos_hint: {'center_x':0.5, 'center_y':0.32}
    MDRoundFlatIconButton:
        text: "Add"
        icon: "plus"
        text_color: "white"
        theme_bg_color: "Custom"
        line_color: "black"
        icon_color: "white"
        md_bg_color: "blue"
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press: app.add_worker()
    MDRectangleFlatIconButton:
        icon: "chevron-left"
        text: "Back"
        theme_text_color: "Custom"
        text_color: "black"
        line_color: 0, 0, 0, 0
        theme_icon_color: "Custom"
        icon_color: "orange"
        pos_hint: {'center_x':0.2, 'center_y':0.2}
        on_press: root.manager.current = 'menu'

"""