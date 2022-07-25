# Kaidun (by HktOverload)

def moveCamera(app, event):
    if event == ('kb/p', 'Up'):
        app.viewer.cam.rotate(roll=-0.1)
    elif event == ('kb/p', 'Down'):
        app.viewer.cam.rotate(roll=+0.1)
    elif event == ('kb/p', 'Left'):
        app.viewer.cam.rotate(pitch=+0.1)
    elif event == ('kb/p', 'Right'):
        app.viewer.cam.rotate(pitch=-0.1)
    elif event == ('kb/p', 'w'):
        app.viewer.cam.ctr[1] -= 0.1
    elif event == ('kb/p', 's'):
        app.viewer.cam.ctr[1] += 0.1
    elif event == ('kb/p', 'a'):
        app.viewer.cam.ctr[0] -= 0.1
    elif event == ('kb/p', 'd'):
        app.viewer.cam.ctr[0] += 0.1
    elif event == ('kb/p', 'e'):
        app.viewer.cam.ctr[2] -= 0.1
    elif event == ('kb/p', 'c'):
        app.viewer.cam.ctr[2] += 0.1

def adjustLight(app, event):
    if event == ('kb/p', '<'):
        app.viewer.lighting[0].brightness -= 0.3
    elif event == ('kb/p', '>'):
        app.viewer.lighting[0].brightness += 0.3
