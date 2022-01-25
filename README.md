# Pi-in-the-Sky
Task: Launch Raspberry Pi into the sky, collect data, and do something at the apex of the Pi's flight. Additionally, make sure landing is safe enough to protect the Pi.

## Table of Contents
* [Planning](#Planning)
  * [Initial Ideas](#Initial-Ideas)
  * [To-Do](#To-Do)

<br>
<br>

# Planning
## Initial Ideas
  * Supersonic Potato Cannon
    * Pros - High altitude, powerful
    * Cons - Difficult to materialize, expensive, extremely dangerous, difficult to transfer
  * Hot Air Balloon
    * Pros - Floats for a long time, high altitude
    * Cons - Slow, hard to heat and contain air
  * Bottle Rocket
    * Pros - High altitude, lightweight, easy to construct, flexible
    * Cons - Maximum PSI limits potential height, mildly dangerous due to high pressure

## Final Design Plan
We decided to make a Bottle Rocket due to the inexpensive, easy construction, and the flexibility of the design. The maximum PSI will not limit the height drastically, and the path of the flight could be controlled by varying the pressure and angle at lauch. Additionally, we will use a barometric pressure sensor to determine the altitude and release a parachute when the rocket is at its apex. [Multi-stage bottle rocket explanation](http://www.aircommandrockets.com/howitworks_1.htm)

<img src="Media/1-10-22rocket.jpg" width="300px" height="400" /> 

#  ***To-Do***
* ***Design parachute release mechanism***
* ***Create stronger rocket***
  * Create and print fins
  * Possibly create two staged rocket (Helmstetter)
  * Possible mid-air propulsion system
* ***Design place for Pi on the rocket***
* ***Code accelerometer***
  * Find max height
  * Get information at max height
  * Gather information during the flight
* ***Code parachute deploy***
  * Create system to deploy parachute
* ***Code barometric pressure altitude sensor***
* ***CAD***
  * Fins
  * Pi Holder
  * Camera mount
  * Parachute release
  * Possible connector or valve for multi-stage 

# Tentative Schedule
 * Week of 1.10 - Finish sleeve to go around rocket
 * Week of 1.17 - Determine method of attaching payload
 * Week of 1.24 - Design and  work on creation of payload
 * Week of 1.31 - Coding and fabrication of payload electronics and cone
 * Week of 2.7 - Finish fabrication and test rocket launch
 * Week of 2.14 -  If not finished with fabrication, finish fabrication and test rocket. If test from Week of 2.7 successful, begin implementation of electronics
 * Week of 2.21 - Test electronics, if successful, try launching with electronics. If not, get electronics working
 * Week of 2.28 - If electronics working, test launching with electronics. If launch successful, ADD BOOSTERS.
 * Week of 3.7 - Get boosters working
 * Week of 3.14 - Get boosters working better.
 * Week of 3.21 - Documentation and getting boosters and electronics working
# 1.11.22
 ### Work done -
 * Found diameter of bottle laser cutting circles with successively larger diameters until it fit snugly, which happened with a 107mm circle, meaning the real diameter of the bottle is closer to ~ 107.14mm due to the 0.14mm kerf of the laser. This measurement will be used to 3d print a friction fit sleeve on which the fins will be mounted.

# 1.13.22
  ### Work done - 
  * 3d printed mock sleeve to friction fit full sleeve eventually, spoke with Mr. Helmstetter about future multistage two body propulsion of the rocket, and created a prototype sleeve for the rocket
  <img src="Media/BottleSleeve.png" width="300" height="277" /> 

# 1.19.22
  ### Work done - 
  * Wrote test barometric pressure altimeter code which prints pressure, altitude, and temperature read from the MPL3115A2 barometric pressure altimeter

# 1.21.22
 ### Work done -
 * Determined method for attaching payload to rocket and securing payload container to rocket. <br/>
   <img src="Media/BottleDiagram.png" width="300" height="277" /> 
