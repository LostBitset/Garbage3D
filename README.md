# Kaidun

A game (more specifically, a 15-112 term project).

> It's far in the future, and you live on a planet called Terr.
> For a reason you can't clearly remember, you were placed into cryopreservation against your own will.
> When you wake up, humanity has long abandoned this sector, and the majority of nearby planets have been destroyed.
> Just after waking up, you recieve a message asking you to collect information on the mysterious destruction of these worlds.
> You land on a planet, explore it on foot, collect samples from appropriate areas, and try to make your way out.
> If only it was that easy....

### Goals for the project

- Uses only `cmu_112_graphics` (tkinter based)
- Procedural terrain
- Full 3D
- Distance fog and a day-night cycle
- Flybacks are implemented using a motion planner to avoid terrain obstructions

### Intro Sequence

Your first mission is to visit the planet Sora-9, where you discover an intense fog covering the surface.
You discover that motion causes the fog to concentrate at your location, and staying still causes it to disperse.
However, you suddenly find your vision immersed in a wireframe view of the surface.
You can see huge mountains, but occasionally sides of the mountain will drop down, and then rise back up.
These (reversible avalanches?) are triggered when moving on certain "weak sites".
The probability that a site will be a weak site can be identified loosely based on the color of the surface rock.
If you react quickly enough, you can use your emergency jetpack to superjump and recover.
However, this uses up your power reserves (based on how far up you have to go).
If you run out of power and find yourself stuck in a valley, a flyback will be automatically initiated.
Using power beamed from your ship, you will be flown back to it and forced to start all over again.
Additionally, drawing power from your ship means that recent samples will be destroyed.
The only way to keep samples safe without using power is to obtain enough of them to complete a sample bank.
You can then send the samples themselves (not just the analysis) data to the originator of these missions.
