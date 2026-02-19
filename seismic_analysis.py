import numpy as np
import matplotlib.pyplot as plt
from area_trapezoidal import area_trapezoidal
from pendiente_central import pendiente_central

plt.close('all')

filename = 'PRMY10-n.70006vll.HNE.--.acc.V2c'
raw_acceleration = np.loadtxt(filename, skiprows=54)

g = 981
sampling_rate = 200
dt = 1 / sampling_rate


acceleration_g = raw_acceleration / g

mean_acc = np.mean(acceleration_g)
print(f"Baseline offset removed: {mean_acc:.6f} g")
acceleration_g = acceleration_g - mean_acc

num_points = np.size(acceleration_g)

t_start, t_end = 0, (num_points - 1) * dt
time = np.linspace(t_start, t_end, num_points)

velocity = area_trapezoidal(time, acceleration_g * g, 1)
velocity = np.hstack([0, velocity])

displacement = area_trapezoidal(time, velocity, 1)
displacement = np.hstack([0, displacement])

jerk = pendiente_central(time, acceleration_g * g)
jerk = np.hstack([0, jerk])

max_disp_abs = np.max(np.abs(displacement))
idx_disp = np.where(np.abs(displacement) == max_disp_abs)
max_disp = displacement[idx_disp]
t_max_disp = time[idx_disp]
text_disp = f"max D={max_disp[0]:.3f} cm @ {t_max_disp[0]:.2f} s"

max_vel_abs = np.max(np.abs(velocity))
idx_vel = np.where(np.abs(velocity) == max_vel_abs)
max_vel = velocity[idx_vel]
t_max_vel = time[idx_vel]
text_vel = f"max V={max_vel[0]:.3f} cm/s @ {t_max_vel[0]:.2f} s"

max_acc_abs = np.max(np.abs(acceleration_g))
idx_acc = np.where(np.abs(acceleration_g) == max_acc_abs)
max_acc = acceleration_g[idx_acc]
t_max_acc = time[idx_acc]
text_acc = f"max A={max_acc[0]:.3f} g @ {t_max_acc[0]:.2f} s"

max_jerk_abs = np.max(np.abs(jerk))
idx_jerk = np.where(np.abs(jerk) == max_jerk_abs)
max_jerk = jerk[idx_jerk]
t_max_jerk = time[idx_jerk]
text_jerk = f"max J={max_jerk[0]:.3f} cm/s3 @ {t_max_jerk[0]:.2f} s"
plt.figure()

plt.subplot(411)
plt.plot(time[1:], jerk, '-b', t_max_jerk, max_jerk, 'oy', lw=0.5)
plt.xlabel('time [s]')
plt.ylabel('J [cm/s3]')
plt.text(1.1 * t_max_jerk[0], max_jerk[0], text_jerk)

plt.subplot(412)
plt.plot(time, acceleration_g, '-b', t_max_acc, max_acc, 'oy', lw=0.5)
plt.xlabel('time [s]')
plt.ylabel('a [g]')
plt.text(1.1 * t_max_acc[0], max_acc[0], text_acc)

plt.subplot(413)
plt.plot(time, velocity, '-b', t_max_vel, max_vel, 'oy', lw=0.5)
plt.xlabel('time [s]')
plt.ylabel('v [cm/s]')
plt.text(1.1 * t_max_vel[0], 0.85 * max_vel[0], text_vel)

plt.subplot(414)
plt.plot(time, displacement, '-b', t_max_disp, max_disp, 'oy', lw=0.5)
plt.xlabel('time [s]')
plt.ylabel('d [cm]')
plt.text(1.1 * t_max_disp[0], max_disp[0], text_disp)

output_table = np.array([time[1:], velocity[1:], acceleration_g[1:], jerk]).T

header_text = """raw data from UPRM
processed for INGE-3016
time[s], velocity[cm/s], acceleration[g], jerk[cm/s3]"""

output_filename = 'MyFirstPythonOutputFile.uprm'
np.savetxt(
    output_filename,
    output_table,
    fmt='%.4f',
    delimiter=',',
    header=header_text,
    comments='#'
)
plt.savefig("seismic_signals.png", dpi=300, bbox_inches='tight')
plt.show()

