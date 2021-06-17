import numpy as np
from matplotlib import pyplot as plt

T = 300  # K
k = 1.380649e-26  # kJ/K
N_A = 6.02214076e23  # avogadro number

distance = []
freeEnergy = []
times = [1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for time in times:
    data = np.loadtxt('fes_' + str(time) + '.dat', unpack=True)
    distance.append(data[0]) # nm
    # change units from kJ/mol to kT:
    freeEnergy.append(data[1] / (k * T * N_A))

free_min = np.min(freeEnergy[-1])

plt.figure(1, figsize=(10, 7))

for i in range(len(times)):
    plt.plot(distance[i], freeEnergy[i] - free_min,
        label=str(times[i]/10) + ' ns')

plt.ylabel('Free Energy [kT]')
plt.xlabel('distance between Na and Cl atoms [nm]')
plt.legend()
plt.savefig('free_energy_metadynamics.png')

dist2, free2, _ = np.loadtxt('histo.dat', unpack=True)
free_reweighted = -np.log(free2)

plt.figure(2, figsize=(10, 7))
plt.plot(distance[-1], freeEnergy[-1] - free_min, label='without reweighting')
plt.plot(dist2, free_reweighted - np.min(free_reweighted), label='rewieghted')

plt.legend()
plt.ylabel('Free Energy [kT]')
plt.xlabel('distance between Na and Cl atoms [nm]')
plt.savefig('comparison.png')