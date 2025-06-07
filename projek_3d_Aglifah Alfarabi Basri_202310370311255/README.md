
# Rocket 3D Scene Visualization

This project uses Plotly to visualize a 3D rocket model standing on a launchpad over a hemisphere, representing a planet.

## Components

### 1. Cone (Rocket Tip)
- Constructed using polar coordinates.
- Creates the pointed nose of the rocket.
- Placed on top of the rocket's body.

### 2. Cylinder (Rocket Body)
- Represents the main vertical body of the rocket.
- Plotted as a vertical cylinder.

### 3. Cube (Rocket Fins)
- Small cubes placed at the base of the rocket body.
- Provide aerodynamic stability (visual only).

### 4. Launchpad
- Base platform using a rectangular prism (Mesh3d).
- Four legs created using small vertical cylinders.

### 5. Hemisphere (Planet Surface)
- A semi-spherical surface representing the ground or planet.
- Added for visual aesthetics.

## Output
The scene is exported to an interactive HTML file with a black background and gray launchpad.

## How to Run
1. Install dependencies:
   ```
   pip install plotly numpy
   ```

2. Run the Python script:
   ```
   python rocket_scene.py
   ```

3. Open the generated `rocket_scene_black_bg.html` in your browser.
