# Kaidun (by HktOverload)

def moveCamera(app, event):
    cam = app.viewer.cam
    if event == ('kb/p', 'Up'):
        cam.rotate(roll=-0.1)
    elif event == ('kb/p', 'Down'):
        cam.rotate(roll=+0.1)
    elif event == ('kb/p', 'Left'):
        cam.rotate(yaw=+0.1)
    elif event == ('kb/p', 'Right'):
        cam.rotate(yaw=-0.1)
    elif event == ('kb/p', 's'):
        cam.move(2, +0.1)
    elif event == ('kb/p', 'w'):
        cam.move(2, -0.1)
    elif event == ('kb/p', 'd'):
        cam.move(0, +0.1)
    elif event == ('kb/p', 'a'):
        cam.move(0, -0.1)
    elif event == ('kb/p', 'c'):
        cam.move(1, -0.1)
    elif event == ('kb/p', 'e'):
        cam.move(1, +0.1)

def adjustLight(app, event):
    if event == ('kb/p', '<'):
        app.viewer.lighting[0].brightness -= 0.3
    elif event == ('kb/p', '>'):
        app.viewer.lighting[0].brightness += 0.3
