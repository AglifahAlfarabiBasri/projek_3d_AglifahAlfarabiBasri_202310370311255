
import plotly.graph_objects as go
import numpy as np

# === Component 1: Cone (tip of rocket) ===
def create_cone(x_shift=0, y_shift=0, z_shift=0, scale=1):
    theta = np.linspace(0, 2 * np.pi, 30)
    z = np.linspace(0, 1, 20)
    theta, z = np.meshgrid(theta, z)
    x = scale * (1 - z) * np.cos(theta) + x_shift
    y = scale * (1 - z) * np.sin(theta) + y_shift
    z = scale * z + z_shift
    return go.Surface(x=x, y=y, z=z, showscale=False, colorscale="Oranges")

# === Component 2: Cylinder (body of rocket) ===
def create_cylinder(x_shift=0, y_shift=0, z_shift=0, height=2, radius=0.5):
    theta = np.linspace(0, 2 * np.pi, 30)
    z = np.linspace(0, height, 20)
    theta, z = np.meshgrid(theta, z)
    x = radius * np.cos(theta) + x_shift
    y = radius * np.sin(theta) + y_shift
    z = z + z_shift
    return go.Surface(x=x, y=y, z=z, showscale=False, colorscale="Greys")

# === Component 3: Cube (fins) ===
def create_cube(x_shift=0, y_shift=0, z_shift=0, size=0.2):
    x = [0, 0, 1, 1, 0, 0, 1, 1]
    y = [0, 1, 1, 0, 0, 1, 1, 0]
    z = [0, 0, 0, 0, 1, 1, 1, 1]
    x = [i * size + x_shift for i in x]
    y = [i * size + y_shift for i in y]
    z = [i * size + z_shift for i in z]
    return go.Mesh3d(x=x, y=y, z=z,
                     i=[0, 0, 0, 1, 1, 2, 3, 4, 4, 5, 6, 7],
                     j=[1, 2, 3, 2, 5, 3, 0, 5, 6, 6, 7, 6],
                     k=[2, 3, 0, 5, 6, 0, 4, 6, 7, 7, 4, 7],
                     color='gray', opacity=0.9)

# === Component 4: Launchpad (Platform and legs) ===
def create_launchpad():
    traces = []
    traces.append(go.Mesh3d(
        x=[-2, 2, 2, -2, -2, 2, 2, -2],
        y=[-2, -2, 2, 2, -2, -2, 2, 2],
        z=[0, 0, 0, 0, -0.2, -0.2, -0.2, -0.2],
        i=[0, 0, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7],
        j=[1, 2, 2, 3, 3, 0, 0, 5, 6, 6, 7, 7],
        k=[2, 3, 3, 0, 0, 1, 1, 6, 7, 7, 4, 4],
        color='gray', opacity=0.9
    ))
    for (x, y) in [(-1.5, -1.5), (1.5, -1.5), (1.5, 1.5), (-1.5, 1.5)]:
        traces.append(create_cylinder(x, y, -1, height=1, radius=0.1))
    return traces

# === Component 5: Hemisphere (planet under pad) ===
def create_hemisphere(radius=1.0, center=(0, 0, -1.2)):
    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi / 2, 30)
    x = radius * np.outer(np.cos(u), np.sin(v)) + center[0]
    y = radius * np.outer(np.sin(u), np.sin(v)) + center[1]
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
    return go.Surface(x=x, y=y, z=z, colorscale='YlOrBr', showscale=False)

# Compose scene
fig = go.Figure()
fig.add_trace(create_cylinder(z_shift=0))
fig.add_trace(create_cone(z_shift=2))
fig.add_trace(create_cube(x_shift=0.5, y_shift=0, z_shift=0.2))
fig.add_trace(create_cube(x_shift=-0.7, y_shift=0, z_shift=0.2))
fig.add_trace(create_cube(x_shift=0, y_shift=0.5, z_shift=0.2))
for trace in create_launchpad():
    fig.add_trace(trace)
fig.add_trace(create_hemisphere())

# Set background to black
fig.update_layout(scene=dict(
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    zaxis=dict(visible=False),
    bgcolor='black',
), margin=dict(l=0, r=0, b=0, t=0))

fig.write_html("rocket_scene_black_bg.html")
