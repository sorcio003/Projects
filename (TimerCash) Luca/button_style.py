start_btn = '''
MDRoundFlatIconButton:
    text: "Start"
    icon: "android"
    text_color: "white"
    theme_bg_color: "Custom"
    line_color: "black"
    icon_color: "white"
    md_bg_color: "green"
    pos_hint: {'center_x':0.55, 'center_y':0.4}
    on_press: app.start()
'''

end_btn = '''
MDRoundFlatIconButton:
    text: "End"
    icon: "close"
    text_color: "white"
    theme_bg_color: "Custom"
    line_color: "black"
    icon_color: "white"
    md_bg_color: "red"
    pos_hint: {'center_x':0.4, 'center_y':0.4}
    on_press: app.stop()
'''

receiver_btn = '''
MDRoundFlatIconButton:
    text: "Receiver"
    icon: "plus"
    text_color: "black"
    pos_hint: {'center_x':0.8, 'center_y':0.45}
    on_press: app.receiver()
'''

add_worker_btn = '''
MDRoundFlatIconButton:
    text: "Add Worker"
    icon: "plus"
    text_color: "black"
    pos_hint: {'center_x':0.8, 'center_y':0.8}
    on_press: app.add_worker()
'''