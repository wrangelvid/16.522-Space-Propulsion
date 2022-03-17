import numpy as np

# Constants
e0 = 8.8541878e-12  # permittivity of free space [m-3 kg-1 s4 A2]
mu0 = 1.2566371e-6  # permeability of free space [m kg s-2 A-2]
c0 = 2.99792458e8   # speed of light in vacuum [m s-1]
k = 1.38064852e-23  # Boltzmann constant [m2 kg s-2 K-1]
q = 1.60217662e-19  # elementary charge [coulombs]
u = 1.66053906e-27  # atomic mass unit, [kg]
me = 9.1093836e-31  # electron mass [kg]
R = 8.3145  # universal gas constant [J mol-1 K-1]
NA = 6.0221409e23  # Avogadro's number [mol-1]
mi = 39.948  # atomic mass: argon [amu]
# mi = 15.999  # atomic mass: oxygen [amu]


# Assumptions
P = 133.322*1e-5  # Pressure in vacuum chamber [Pa]
T = 300  # ambient temperature [K]
Te = 3/k  # electron temperature [K]
phi = 200  # [V]
B = 1  # Magnetic field strength [Tesla]


# Plasma (lectures 9-10)
# Plasma number density: use assumptions about pressure and temperature in ideal gas law
# Debeye length [m]
lambda_D = np.sqrt((e0*k*Te) / (q**2*ne))
# Plasma frequency [rad/s]
omega_p = np.sqrt((q**2*ne) / (e0*me))
# Speed of sound [m/s]
v_star = lambda_D * omega_p
# Cyclotron frequencies of electron, ion [rad/s]
omega_c_e, omega_c_i = q*B/me, q*B/mi
# Larmor radius of electron, ion [m]
r_L_e, r_L_i = me*omega_0/(q*B), mi*omega_0/(q*B)
# Mean thermal speed of electrons [m/s]
c_bar_e = np.sqrt((8*k*Te)/(np.pi*me))


# Ion exit velocity
vi = np.sqrt(2*q/mi*phi)

# Electron drift velocity
v_theta = E/B

# Hall current
j_theta = -q*ne*v_theta

# Lorentz force density (Thrust?)
f = q*ne*E
