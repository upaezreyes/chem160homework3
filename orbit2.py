from math import sqrt
from drawtraj import drawtraj   # to draw the trajectory
def force(x,y,m,msun):   # x and y are the position of earth and the sun
    r2=x**2+y**2
    r32=r2*sqrt(r2)     # distance bwt the earth and the sun
    fx=-x*m*msun/r32   # force on the x-direction
    fy=-y*m*msun/r32   # force on the y-direction
    return fx,fy       # solve fx and fy
def integrate(x,y,vx,vy,fx,fy,m,dt):
   ax,ay = fx/m, fy/m   # aceleration on the x and y directions
   vx += ax*dt    # updating velocity on the x-direction
   vy += ay*dt    # updating velocity on the y-direction
   x += vx*dt     # updating position on the x-direction
   y += vy*dt     # updation position on the y-direction
   return x, y, vx, vy

# Main part of the program
mstar = 300000    # mass of the sun (300000 bigger than the earth)
m = 1        # mass of the earth
nsteps = 100000  # steps
dt = 0.01    # space steps of time
r = 1550    # radius (distance from the planet and star)
x,y = 0,r   # positions of the earth and the sun
vx,vy = 2.2,0.0 # Initial velocities
trajx,trajy=[],[]
starx,stary=[],[]

for t in range(nsteps):
    fx,fy = force(x,y,m,mstar)  # calculates fx & fy using the force function
    x,y,vx,vy, = integrate(x,y,vx,vy,fx,fy,m,dt)
    trajx.append(x)
    trajy.append(y)
    starx.append(x)
    stary.append(y)

drawtraj(starx,stary,starx,stary,4*r)  #side of the box