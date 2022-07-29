# Kaidun

A game (more specifically, a 15-112 term project).

**THIS FAILED BECAUSE OF SOME STUPID TKINTER ISSUE NOW ITS JUST A SHITTY 3D ENGINE BYE**

> It's far in the future, and you live on a planet called Terr.
> For a reason you can't clearly remember, you were placed into cryopreservation against your own will.
> When you wake up, humanity has long abandoned this sector, and the majority of nearby planets have been destroyed.
> Just after waking up, you recieve a message asking you to collect information on the mysterious destruction of these worlds.
> You land on a planet, explore it on foot, collect samples from appropriate areas, and try to make your way out.
> If only it was that easy....

### Project Goals

- [ ] Full 3D with only `cmu_112_graphics` (tkinter based)
	- [X] Perspective camera implemented with homogenous coordinates
	- [X] Painter's algorithm to display geometry
	- [X] Flat shading with Lambertian reflectance
	- [ ] Chunk loading
	- [ ] Bump mapping
- [ ] Dynamic fog
	- [ ] Exponential scattering effect
	- [ ] Depth sampling and interpolation
	- [ ] Realistic sample updates
	- [ ] Dynamically control render distance
- [ ] Procedural generation
	- [ ] Generating terrain
	- [ ] Defining where weak sites are
	- [ ] Deformation during RAs
- [ ] Flybacks implemented using a motion planner
	- [ ] Defining the configuration space
	- [ ] Reverse-mode autodiff for calculating gradients
	- [ ] Virtual potential fields

### Intro Sequence

Your first mission is to visit the planet Sora-9, where you discover an intense fog covering the surface.
You discover that motion causes the fog to concentrate at your location, and staying still causes it to disperse.
However, you suddenly find your vision immersed in a wireframe view of the surface.
You can see huge mountains, but occasionally sides of the mountain will drop down, and then rise back up.

### Gameplay

These reversible avalanches (RAs) are triggered when moving on certain "weak sites".
The probability that a site will be a weak site can be identified loosely based on the color of the surface rock.
If you react quickly enough, you can use your emergency jetpack to superjump and recover.
However, this uses up your power reserves (based on how far up you have to go).
If you run out of power and find yourself stuck in a valley, a flyback will be automatically initiated.
Using power beamed from your ship, you will be flown back to it and forced to start all over again.
Additionally, drawing power from your ship means that recent samples will be destroyed.
The only way to keep samples safe without using power is to obtain enough of them to complete a sample bank.
You can then send the samples themselves (not just the analysis) data to the originator of these missions.
