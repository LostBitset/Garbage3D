# Kaidun (by HktOverload)

def moveCamera(app, event):
    if event == ('kb/down', 'Up'):
        app.viewer.cam.rotate(roll=-0.1)
    elif event == ('kb/down', 'Down'):
        app.viewer.cam.rotate(roll=+0.1)
    elif event == ('kb/down', 'a'):
        app.viewer.cam.ctr[0] -= 0.1
    elif event == ('kb/down', 'd'):
        app.viewer.cam.ctr[0] += 0.1
