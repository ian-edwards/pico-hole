from led import led_error

def on_error(error_message):
    print(error_message)
    led_error()