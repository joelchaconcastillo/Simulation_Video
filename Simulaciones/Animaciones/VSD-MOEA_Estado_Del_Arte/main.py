# coding=utf-8
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
ObjectivesFiles = ['Sample_Visual_Video/VSD_MOEA_obj','Sample_Visual_Video/NSGAII_obj', 'Sample_Visual_Video/MOEAD_obj', 'Sample_Visual_Video/R2_EMOA_obj']
VariablesFiles = ['Sample_Visual_Video/VSD_MOEA_var','Sample_Visual_Video/NSGAII_var', 'Sample_Visual_Video/MOEAD_var', 'Sample_Visual_Video/R2_EMOA_var']


names = ['VSD-MOEA', 'NSGA-II', 'MOEA\D', 'R2-EMOA']
colr =['blue', 'red','green', 'black']
Instance = 'Instance WFG5'
SizePool=100
NumberSamples = 1000
NumberObjectives = 2
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
    for Str in Population:
       tmp = Str.split()
       f1.append(float(tmp[0]))
       f2.append(float(tmp[1]))
    return f1,f2
data_obj = {}
data_var = {}
for NameFile in ObjectivesFiles:
   data_obj[NameFile] = FilterData(NameFile, SizePool)
for NameFile in VariablesFiles:
   data_var[NameFile] = FilterData(NameFile, SizePool)

#------------------------------------------------------------
# set up figure and animation
fig = plt.figure(figsize=(15,10))
fig.text(0.51, 0.14, 'Local \n optimum', ha='center', va='center')
fig.text(0.51, 0.73, 'Local \n optimum', ha='center', va='center')
fig.text(0.51, 0.34, 'Global \n optimum', ha='center', va='center')
#fig.set_size_inches(100, 100)
#mng = plt.get_current_fig_manager()
#fig.frame.Maximize(True)

ObjectiveSpace = fig.add_subplot(121)
VariableSpace = fig.add_subplot(122)
y = 0.95
i = 0
for tmp in ObjectivesFiles:
   ObjectiveSpace.set_ylim(0, 5.5)
   ObjectiveSpace.set_xlim(0, 5)
   ObjectiveSpace.set_xlabel('$f_1(x)$')
   ObjectiveSpace.set_ylabel('$f_2(x)$')
   ObjectiveSpace.text(0.95, y, names[i],
        verticalalignment='bottom', horizontalalignment='right',
        transform=ObjectiveSpace.transAxes,
        color=colr[i], fontsize=15)
   ObjectiveSpace.grid()
   time_textObj = ObjectiveSpace.text(0.02, 0.92, '', transform=ObjectiveSpace.transAxes)
   y = y - 0.05
   i = i+1
y = 0.95
i = 0
for tmp in VariablesFiles:
   VariableSpace.set_ylim(-0.2, 5)
   VariableSpace.set_xlim(0, 3)
   VariableSpace.set_xlabel('$x_1$')
   VariableSpace.set_ylabel('$x_2$')
   VariableSpace.text(0.95, y, names[i],
        verticalalignment='bottom', horizontalalignment='right',
        transform=VariableSpace.transAxes,
        color=colr[i], fontsize=15)
   VariableSpace.plot([0, 2.2], [1.4, 1.4], color='r')
   VariableSpace.plot([0, 2.2], [4, 4], color='b')
   VariableSpace.plot([0, 2.2], [0, 0], color='b')
   VariableSpace.grid()
   time_textVar = VariableSpace.text(0.02, 0.92, '', transform=VariableSpace.transAxes)
   y = y - 0.05
   i = i+1



IndexPop=0
individualsObj = {}
individualsVar = {}
#Colours = ['bo','ro', 'go', 'mo', 'co', 'wo']
Colours = ['bo','ro', 'go', 'ko']
i = 0
for NameFile in ObjectivesFiles:
	individualsObj[NameFile], = ObjectiveSpace.plot([], [], Colours[i], ms=6)
	i = i+1
i = 0
for NameFile in VariablesFiles:
	individualsVar[NameFile], = VariableSpace.plot([], [], Colours[i], ms=6)
	i = i+1

def init():
    """initialize animation"""
    for NameFile in ObjectivesFiles:
       individualsObj[NameFile].set_data([], [])
    for NameFile in VariablesFiles:
       individualsVar[NameFile].set_data([], [])
    time_textObj.set_text(Instance)
    time_textVar.set_text(Instance)
    return individualsObj['Sample_Visual_Video/VSD_MOEA_obj'], individualsObj['Sample_Visual_Video/NSGAII_obj'], individualsObj['Sample_Visual_Video/MOEAD_obj'], individualsObj['Sample_Visual_Video/R2_EMOA_obj'], individualsVar['Sample_Visual_Video/VSD_MOEA_var'], individualsVar['Sample_Visual_Video/NSGAII_var'], individualsVar['Sample_Visual_Video/MOEAD_var'], individualsVar['Sample_Visual_Video/R2_EMOA_var'], time_textObj, time_textVar,


def animate(i):
    """perform animation step"""
    global Generation
    #Read the second header....
    for NameFile in ObjectivesFiles:
       fi, fj = getObjectives(i, data_obj[NameFile], SizePool)
       individualsObj[NameFile].set_data(fi, fj)
    for NameFile in VariablesFiles:
       fi, fj = getObjectives(i, data_var[NameFile], SizePool)
       individualsVar[NameFile].set_data(fi, fj)
    Generation = i
    gn = Generation + 1
    time_textObj.set_text(u'Objective Space \nCurrent Generation: %d \n' % gn )
    time_textVar.set_text(u'Decision Variable Space \nCurrent Generation: %d \n' % gn )
    return individualsObj['Sample_Visual_Video/VSD_MOEA_obj'], individualsObj['Sample_Visual_Video/NSGAII_obj'], individualsObj['Sample_Visual_Video/MOEAD_obj'], individualsObj['Sample_Visual_Video/R2_EMOA_obj'],individualsVar['Sample_Visual_Video/VSD_MOEA_var'],individualsVar['Sample_Visual_Video/NSGAII_var'], individualsVar['Sample_Visual_Video/MOEAD_var'], individualsVar['Sample_Visual_Video/R2_EMOA_var'], time_textObj, time_textVar,

ani = animation.FuncAnimation(fig, animate, frames= NumberSamples,
                              interval=200, blit=True, init_func=init)

#animate(999)
# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#ani.save('particle_box.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
ani.save('Simulation_WFG5.mp4')
#plt.savefig('Simulacion_Algoritmo_5.eps', format='eps', dpi=1000)
plt.show()
