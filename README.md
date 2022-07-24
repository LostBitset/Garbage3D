# Kaidun

A game (more specifically, a 15-112 term project).

> It's far in the future, and you live on a planet called Terr.
> For a reason you can't clearly remember, you were placed into cryopreservation against your own will.
> When you wake up, humanity has long abandoned this sector, and the once thriving system of planets has been destroyed.
> Just after waking up, you recieve a message asking you to collect information on the mysterious destruction of these planets.
> You enter a planet, collect samples, upload the data you've collected, and try to make your way out.
> If only it was that easy....

### Goals for the project

- Uses only `cmu_112_graphics` (tkinter based)
- Procedural terrain
- Full 3D
- Distance fog and a day-night cycle
- Flybacks are implemented using a motion planner to avoid terrain obstructions

### Gameplay

Your job is to collect samples.
This is done by exploring the surface of abandoned planets, and searching for artifacts.
Sample sites are automatically chosen, but you can select the difficulty ahead of time (how far away they are from your ship).
You cannot switch sample difficulty levels while exploring on the surface.
The planet itself functions as your enemy, massive rifts constantly form and rejoin (right underneath your feet if you're particularly unlucky).
Occasionally, these rifts will form small "islands", which are only barely held in place. 
These islands essentially have stealth mechanics, and running to fast or making sharp turns will cause them to cave in.
Your ship contains the reactor that powers pretty much everything, including your EVA suit.
If you fall into a rift or an island that you're on caves in, your EVA suit will automatically turn on its emergency jetpacks and fly you back to your ship.
These are known, understandably, as flybacks. 
However, this draws so much power that the sample preservation equipment will fail, and a few of the stored samples will be damaged.
If you fail many times in quick succession, more and more samples will be destroyed each time.

Eventually, you gain the ability to repair samples lost on a mission by sacrificing samples obtained from performing this mission successfully.
This is generally only desireable if you failed a lot, as the repair process is far from perfect.

Eventually, you will have completed a sample bank, which can be sent to the mysterious originator of this operation.
The component of your score sent to the sample bank can never be lost, at least, for now.
