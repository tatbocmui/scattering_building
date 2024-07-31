def on_mouse_wheel(event, canvas):
    if event.delta:
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")
    else:
        canvas.yview_scroll(-1 * int(event.delta / 30), "units")

def bind_scroll_events(canvas):
    canvas.bind_all("<MouseWheel>", lambda event: on_mouse_wheel(event, canvas))  # Windows and Linux
    canvas.bind_all("<Shift-MouseWheel>", lambda event: on_mouse_wheel(event, canvas))
    canvas.bind_all("<Button-4>", lambda event: on_mouse_wheel(event, canvas))  # For Linux
    canvas.bind_all("<Button-5>", lambda event: on_mouse_wheel(event, canvas))  # For Linux
    canvas.bind_all("<Command-Shift-Button-1>", lambda event: on_mouse_wheel(event, canvas))  # macOS
    canvas.bind_all("<Shift-Button-1>", lambda event: on_mouse_wheel(event, canvas))
    canvas.bind_all("<Control-Shift-Button-1>", lambda event: on_mouse_wheel(event, canvas))
