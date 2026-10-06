import math

L1, L2, alpha_deg, beta_deg = map(float, input().split())

alpha = math.radians(alpha_deg)
beta = math.radians(beta_deg)
phi2 = alpha+beta-math.pi

x = L1 * math.cos(alpha) + L2 * math.cos(phi2)
z = L1 * math.sin(alpha) + L2 * math.sin(phi2)

print(f"{x:.3f} {z:.3f}")
