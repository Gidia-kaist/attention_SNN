import wandb

# Initialize
r_surf = 0.0
r_0 = 5.0
l = 40.0
p = 0
P = 0
R = 0
x = 1

# Function
for p in range(0, 10, 1):

    for R in range(0, 10, 1):
        P = p * 0.1
        R = R * 0.1
        wandb.init(reinit=True, name="P_" + str(round(P, 1)) + "_R_" + str(round(R, 1)), project="interconnect_simul",
                   config={"r_0": r_0,
                           "l": l,
                           "P": P,
                           "R": R,
                           })
        for x in range(1, 120):
            r_surf = r_0 + r_0 * l * ((3 * (1 - P)) / (4 * x)) + r_0 * l * ((3 * R) / (2 + x + (1 - R)))
            wandb.log({"r_surf": r_surf, "X": x, "P": round(P, 1), "R": round(R, 1)})
        wandb.join()
