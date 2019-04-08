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


##------------------------------------------
#Read the input file whose is composed of first general header
#and each individuals in objective space
VSD_MOEA_file_obj = 'VSD_MOEA_obj'
VSD_MOEA_file_var = 'VSD_MOEA_var'
NSGAII_file = 'VSD_MOEA_obj'
Instance = 'Instance WFG5'
SizePool=100
NumberSamples = 1000
NumberObjectives = 2

def FilterData(filename, SizePool):
	with open(filename) as f:
	    data = f.read()
	data = data.split('\n')
	AjustData = list()
		#for line in data:
		   #if 'Current' in line :
		    #  Generation = int(line.split('\t')[3])
		     # if Generation % ReportEachGeneration == 0:
			 #AjustData.extend(data[cont:(cont+1+SizePool)])
			# NReports +=1
		   #cont +=1
	return data

def getObjectives(indexSample, data, SizePool):
    Population = data[indexSample*(SizePool):(indexSample+1)*(SizePool)]
    f1 = []
    f2 = []
    for Str in Population:
       tmp = Str.split('\t')
       f1.append(float(tmp[0]))
       f2.append(float(tmp[1]))
    return f1,f2

data_VSD_MOEA_var = FilterData(VSD_MOEA_file_var, SizePool)
data_VSD_MOEA_obj = FilterData(VSD_MOEA_file_obj, SizePool)
data2 = FilterData(NSGAII_file, SizePool)

#------------------------------------------------------------
# set up figure and animation
fig = plt.figure()

#ObjectiveSpace = fig.add_subplot(121, projection='3d')
#ObjectiveSpace = fig.add_subplot(121)
#VariableSpace = fig.add_subplot(122)
fig, (ObjectiveSpace, VariableSpace) = plt.subplots(2,1)

for space in [ObjectiveSpace, VariableSpace]:
   space = plt.axes(xlim=(0, 5), ylim=(0, 5))
   space.text(0.95, 0.95, 'NSGAII',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ObjectiveSpace.transAxes,
        color='blue', fontsize=15)
   space.text(0.95, 0.90, 'Diversity',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ObjectiveSpace.transAxes,
        color='red', fontsize=15)
   time_text = space.text(0.02, 0.95, '', transform=space.transAxes)

IndexPop=0
individualsVSD_MOEA, = ObjectiveSpace.plot([], [], 'bo', ms=6)
particles2, = VariableSpace.plot([], [], 'ro', ms=6)


def init():
    """initialize animation"""
    individualsVSD_MOEA.set_data([], [])
    particles2.set_data([], [])
    time_text.set_text(Instance)
    return individualsVSD_MOEA, particles2, time_text,

def animate(i):
    """perform animation step"""
    global data_VSD_MOEA_obj,data_VSD_MOEA_var, data2, SizePool
    #Read the second header....
    fi1, fi2 = getObjectives(i, data_VSD_MOEA_obj, SizePool)
    fj1, fj2 = getObjectives(i, data2, SizePool)
    individualsVSD_MOEA.set_data(fi1, fi2)
    particles2.set_data(fj1, fj2)
	#Generation=1
    #time_text.set_text(Instance+' Generation: %d' % Generation  )
    return individualsVSD_MOEA, particles2, time_text,

ani = animation.FuncAnimation(fig, animate, frames= NumberSamples,
                              interval=20, blit=True, init_func=init)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#ani.save('particle_box.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
