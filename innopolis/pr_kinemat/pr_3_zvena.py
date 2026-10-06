import math

L1, L2, L3 = map(float, input().split())
alpha_deg, beta_deg, beta2_deg = map(float, input().split())

alpha = math.radians(alpha_deg)
beta = math.radians(beta_deg)
beta2 = math.radians(beta2_deg)
phi2 = alpha+beta-math.pi
phi3 = phi2+beta2-math.pi

x = L1 * math.cos(alpha) + L2 * math.cos(phi2) + L3 * math.cos(phi3)
z = L1 * math.sin(alpha) + L2 * math.sin(phi2) + L3 * math.sin(phi3)

print(f"{x:.3f} {z:.3f}")