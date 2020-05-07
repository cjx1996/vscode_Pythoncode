



from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    # 监听鼠标点击
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        # Stop listener
        return False
while True:
    try:
            listener.join()
    except KeyboardInterrupt:
     
        break
