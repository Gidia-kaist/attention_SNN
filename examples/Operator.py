import os
import wandb

wandb.init(project="interconnect_simul", config={"r_0": r_0,
                                                 "l": l,
                                                 "p": p,
                                                 "R": R,
                                                 })

os.system("python3.6 Interconnect.py --p 1 --R 1")
'''
for p in range(0, 10, 1):
    for R in range(0, 10, 1):
        os.system("python3.6 Interconnect.py --p " + str(p) +" "+ "--R " + str(R))
        '''