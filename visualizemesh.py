import polyscope as ps

import igl


INPUT_MESH = "./data/Stanford_Bunny.stl"


ps.set_up_dir("z_up")
ps.set_ground_plane_mode("none")

# Initialize polyscope
ps.init()

### Register a point cloud
# `my_points` is a Nx3 numpy array
mesh_v, mesh_f = igl.read_triangle_mesh(INPUT_MESH)

### Register a mesh
# `verts` is a Nx3 numpy array of vertex positions
# `faces` is a Fx3 array of indices, or a nested list
ps.register_surface_mesh("Stanford Bunny", mesh_v, mesh_f, smooth_shade=True)

# View the point cloud and mesh we just registered in the 3D UI
ps.show()