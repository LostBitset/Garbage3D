### Kaidun / TODO

Week 4:
- [X] Finalize lighting and get it to work with colored surfaces
- [ ] Implement chunk loading (chunks are just special `Geom` objects)
- [ ] Generate basic terrain that is either a mountain or valley
- [ ] Create a player and make sure the player doesn't fall through the floor
- [ ] Get distance fog to work with a predetermined amount of fog
- [ ] Implement interpolation for drawing the distance fog
- [ ] Perform depth sampling and do the math for light scattering
- [ ] Update distance fog samples in a realistic way when the camera is moved
- [ ] Calculate max percieved render distance with fog
- [ ] Clip tris (and don't even load chunks) that are far enough away
- [ ] Scale the number of samples with the intended amount of fog

Week 5:
- [ ] Write the backend parts for handling sample collections
- [ ] Allow save data to be stored on the disk
- [ ] Create the interface for viewing and managing your sample collection
- [ ] Create the interface for switching planets
- [ ] Have the procedural generation set where weak sites are
- [ ] Have the terrain be colored appropriately
- [ ] Setup the mechanics for RAs
- [ ] Trigger RAs both in response to the player and purely randomly
- [ ] Deform the terrain in response to RAs
- [ ] Detect when the player is stuck in a valley
- [ ] Implement emergency jumps
- [ ] Setup local power reserves and add it to the save data
- [ ] Finalize all stored data formats
- [ ] Have emergency jumps use local power
- [ ] Implement emergency flybacks as teleporting
- [ ] Finalize all interfaces

Week 6:
- [ ] Have terrain generation create a number of different levels
- [ ] Have the terrain include valleys at multiple levels
- [ ] Have the terrain include mountains at multiple levels
- [ ] Finalize terrain generation
- [ ] Convert geometry into C-space obstacles for flybacks
- [ ] Build the basic plumbing of the autodiff system
- [ ] Create the `Tracked` classes and implement basic math
- [ ] Write out the chain rule for reverse-mode autodiff
- [ ] Write the `gradient` function
- [ ] Define the potential fields created by obstacles and the goal
- [ ] Scale the gradient based on a velocity curve
- [ ] Finalize flyback motion
