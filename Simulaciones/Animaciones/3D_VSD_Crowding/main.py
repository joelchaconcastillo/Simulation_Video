"""
Description:
		Animation Two objectives convergence individuals
author: Joel Chacon Castillo
"""
import numpy as np
from scipy.spatial.distance import pdist, squareform

import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
##------------------------------------------
#Read the input file whose is composed of first general header
#and each individuals in objective space
ObjectivesFiles = ['UF10/B','UF10/Distancia_Mejoria']#, 'UF10/Distancia_Proyecciones']#, 'UF10/MOEAD_obj', 'UF10/SMSEMOA_obj', 'UF10/MOMBI2_obj']


names = ['VSD-MOEA', 'NSGA-II', 'GDE3']#, 'MOEAD', 'SMSEMOA', 'MOMBI-II']
colr =['blue', 'red','green','magenta', 'cyan', 'gray']
Instance = 'Instance WFG5'
SizePool=100
NumberSamples = 100
NumberObjectives = 3
Generation = 1
def FilterData(filename, SizePool):
	with open(filename) as f:
	    data = f.read()
	data = data.split('\n')
	AjustData = list()
	return data

def getObjectives(indexSample, data, SizePool):
    Population = data[indexSample*(SizePool):(indexSample+1)*(SizePool)]
    f1 = []
    f2 = []
    f3 = []
    for Str in Population:
       tmp = Str.split()
       f1.append(float(tmp[0]))
       f2.append(float(tmp[1]))
       f3.append(float(tmp[2]))
    return f1,f2,f3,
data_obj = {}
for NameFile in ObjectivesFiles:
   data_obj[NameFile] = FilterData(NameFile, SizePool)

#------------------------------------------------------------
# set up figure and animation
fig = plt.figure(figsize=(15,10))
#fig.set_size_inches(100, 100)
#mng = plt.get_current_fig_manager()
#fig.frame.Maximize(True)

ObjectiveSpace = fig.add_subplot(111, projection='3d')
#ObjectiveSpace = p3.Axes3D(fig)
y = 0.95
i = 0
for tmp in ObjectivesFiles:
   ObjectiveSpace.set_xlim3d([0, 5])
   ObjectiveSpace.set_ylim3d([0, 5])
   ObjectiveSpace.set_zlim3d([0, 5])
   #ObjectiveSpace.text(0.95, y, names[i], verticalalignment='bottom', horizontalalignment='right',transform=ObjectiveSpace.transAxes, color=colr[i], fontsize=15)
   #ObjectiveSpace.text3D(0.95, 3,'aa')
#   ObjectiveSpace.text(4.0, 5.9, 'aaasas', fontsize=15,color= 'c' )
   ObjectiveSpace.grid()
   #time_textObj = ObjectiveSpace.text(0.02, 0.92, '', transform=ObjectiveSpace.transAxes)
   y = y - 0.05
   i = i+1
y = 0.95


IndexPop=0
individualsObj = {}
Colours = ['bo','rx', 'go', 'mo', 'co', 'wo']
i = 0
for NameFile in ObjectivesFiles:
	#individualsObj[NameFile], = ObjectiveSpace.plot([], [],[], Colours[i], ms=6)
	individualsObj[NameFile], = ObjectiveSpace.plot([], [],[], marker="o", linestyle="")
	i = i+1

def init():
    """initialize animation"""
    for NameFile in ObjectivesFiles:
       individualsObj[NameFile].set_data([], [])
       individualsObj[NameFile].set_3d_properties([])
#    time_textObj.set_text(Instance)
    return individualsObj['UF10/B'], individualsObj['UF10/Distancia_Mejoria'],# individualsObj['UF10/Distancia_Proyecciones'],# individualsObj['UF10/MOEAD_obj'], individualsObj['UF10/SMSEMOA_obj'], individualsObj['UF10/MOMBI2_obj'],time_textObj,


def animate(i):
    """perform animation step"""
    global Generation
    #Read the second header....
    for NameFile in ObjectivesFiles:
       fi, fj, fk = getObjectives(i, data_obj[NameFile], SizePool)
       individualsObj[NameFile].set_data(fi, fj)
       individualsObj[NameFile].set_3d_properties( fk)
    Generation = i#Generation+1
    #time_textObj.set_text('Objective Space \nGeneration: %d \n' % Generation  )
    return individualsObj['UF10/B'], individualsObj['UF10/Distancia_Mejoria'], #individualsObj['UF10/Distancia_Proyecciones'],# individualsObj['UF10/MOEAD_obj'], individualsObj['UF10/SMSEMOA_obj'], individualsObj['UF10/MOMBI2_obj'],time_textObj,

ani = animation.FuncAnimation(fig, animate, frames= NumberSamples,
                              interval=200, blit=True, init_func=init)

#animate(9)
# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#ani.save('particle_box.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
ani.save('Simulation_WFG5.mp4')

plt.show()
