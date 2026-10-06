import math

L1, L2, h = map(float, input().split())
alpha_deg, beta_deg, gamma_deg = map(float, input().split())

alpha = math.radians(alpha_deg)
beta = math.radians(beta_deg)
gamma = math.radians(gamma_deg)
phi2 = alpha+beta-math.pi

x = (L1 * math.cos(alpha) + L2 * math.cos(phi2))*math.cos(gamma)
y = (L1 * math.cos(alpha) + L2 * math.cos(phi2))*math.sin(gamma)
z = h + L1 * math.sin(alpha) + L2 * math.sin(phi2)

print(f"{x:.3f} {y:.3f} {z:.3f}")