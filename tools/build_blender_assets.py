"""Build original Mist Garden assets in Blender 5.x.

Run with:
  blender --background --python tools/build_blender_assets.py

Outputs are written only inside this project under assets/blender/.
"""
from __future__ import annotations

import math
import os
from pathlib import Path

import bpy
from mathutils import Vector


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "blender"
SOURCE = OUT / "source"
EXPORTS = OUT / "exports"
PREVIEWS = OUT / "previews"
for folder in (SOURCE, EXPORTS, PREVIEWS):
    folder.mkdir(parents=True, exist_ok=True)


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.collections, bpy.data.cameras, bpy.data.lights):
        for block in list(datablocks):
            if block.users == 0:
                datablocks.remove(block)


def collection(name):
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def move_to_collection(obj, col):
    for old in list(obj.users_collection):
        old.objects.unlink(obj)
    col.objects.link(obj)
    return obj


def mat(name, color, roughness=0.72, metallic=0.0, alpha=1.0, emission=None):
    material = bpy.data.materials.new(name)
    material.diffuse_color = (*color, alpha)
    material.use_nodes = True
    shader = material.node_tree.nodes.get("Principled BSDF")
    shader.inputs["Base Color"].default_value = (*color, alpha)
    shader.inputs["Roughness"].default_value = roughness
    shader.inputs["Metallic"].default_value = metallic
    shader.inputs["Alpha"].default_value = alpha
    if emission:
        shader.inputs["Emission Color"].default_value = (*emission, 1.0)
        shader.inputs["Emission Strength"].default_value = 1.2
    if alpha < 1:
        try:
            material.surface_render_method = "DITHERED"
        except Exception:
            pass
    return material


M = {
    "wall": mat("Hand-painted moss wallpaper", (0.19, 0.23, 0.18)),
    "wall_light": mat("Wallpaper raised pattern", (0.34, 0.37, 0.27)),
    "wood": mat("Warm hand-worked walnut", (0.25, 0.15, 0.095)),
    "wood_light": mat("Honey wood edges", (0.46, 0.29, 0.16)),
    "wood_top": mat("Tabletop aged maple", (0.40, 0.26, 0.15)),
    "floor": mat("Deep olive floor", (0.18, 0.17, 0.12)),
    "felt": mat("Teal stitched felt", (0.075, 0.28, 0.26)),
    "felt_light": mat("Cape patch sea-glass", (0.16, 0.43, 0.39)),
    "rust": mat("Rust-red cloth", (0.50, 0.19, 0.11)),
    "skin": mat("Warm clay face", (0.78, 0.61, 0.43)),
    "cream": mat("Parchment linen", (0.79, 0.69, 0.50)),
    "dark": mat("Deep cocoa", (0.075, 0.055, 0.04)),
    "brass": mat("Old brass", (0.68, 0.43, 0.13), roughness=0.34, metallic=0.55),
    "gold": mat("Dream coin gold", (0.92, 0.62, 0.16), roughness=0.31, metallic=0.65),
    "glass": mat("Frosted dream glass", (0.36, 0.61, 0.57), roughness=0.18, metallic=0.0, alpha=0.48),
    "soil": mat("Garden soil", (0.16, 0.10, 0.065)),
    "leaf": mat("Soft garden leaf", (0.23, 0.43, 0.23)),
    "leaf_light": mat("New growth", (0.48, 0.62, 0.30)),
    "flower": mat("Starflower buttercream", (0.93, 0.69, 0.25)),
    "blue": mat("Moonbean blue", (0.26, 0.43, 0.54)),
    "path": mat("Worn garden path", (0.44, 0.34, 0.23)),
    "glass_glow": mat("Lantern glow", (1.0, 0.66, 0.22), roughness=0.2, emission=(1.0, 0.45, 0.10)),
}


def cube(name, loc, dims, material, bevel=0.0, col=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if material:
        obj.data.materials.append(material)
    if bevel:
        modifier = obj.modifiers.new("Soft hand-rounded edges", "BEVEL")
        modifier.width = bevel
        modifier.segments = 3
        obj.modifiers.new("Soft weighted normals", "WEIGHTED_NORMAL")
    if col:
        move_to_collection(obj, col)
    return obj


def sphere(name, loc, scale, material, col=None, segments=16, rings=10):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if material:
        obj.data.materials.append(material)
    for poly in obj.data.polygons:
        poly.use_smooth = True
    if col:
        move_to_collection(obj, col)
    return obj


def cylinder(name, loc, radius, depth, material, col=None, vertices=16, rotation=None, bevel=0.0):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc)
    obj = bpy.context.object
    obj.name = name
    if rotation:
        obj.rotation_euler = rotation
    if bevel:
        modifier = obj.modifiers.new("Soft rim", "BEVEL")
        modifier.width = bevel
        modifier.segments = 2
        obj.modifiers.new("Weighted normals", "WEIGHTED_NORMAL")
    if material:
        obj.data.materials.append(material)
    if col:
        move_to_collection(obj, col)
    return obj


def cone(name, loc, radius_bottom, radius_top, depth, material, col=None, vertices=16, bevel=0.0):
    bpy.ops.mesh.primitive_cone_add(
        vertices=vertices,
        radius1=radius_bottom,
        radius2=radius_top,
        depth=depth,
        location=loc,
    )
    obj = bpy.context.object
    obj.name = name
    if material:
        obj.data.materials.append(material)
    if bevel:
        modifier = obj.modifiers.new("Soft cloth hem", "BEVEL")
        modifier.width = bevel
        modifier.segments = 3
        obj.modifiers.new("Weighted normals", "WEIGHTED_NORMAL")
    if col:
        move_to_collection(obj, col)
    return obj


def curve_line(name, points, radius, material, col):
    data = bpy.data.curves.new(name, "CURVE")
    data.dimensions = "3D"
    data.resolution_u = 2
    data.bevel_depth = radius
    data.bevel_resolution = 3
    spline = data.splines.new("POLY")
    spline.points.add(len(points) - 1)
    for point, co in zip(spline.points, points):
        point.co = (*co, 1)
    obj = bpy.data.objects.new(name, data)
    col.objects.link(obj)
    data.materials.append(material)
    return obj


def arch_door(name, center_x, front_y, bottom_z, width, straight_height, arch_radius, depth, material, col):
    outline = [(-width / 2, bottom_z), (width / 2, bottom_z), (width / 2, bottom_z + straight_height)]
    for step in range(13):
        angle = math.pi * step / 12
        outline.append((arch_radius * math.cos(angle), bottom_z + straight_height + arch_radius * math.sin(angle)))
    outline.append((-width / 2, bottom_z))
    outline = outline[:-1]
    n = len(outline)
    verts = []
    for y in (front_y, front_y + depth):
        verts.extend((center_x + x, y, z) for x, z in outline)
    faces = [tuple(range(n)), tuple(range(2 * n - 1, n - 1, -1))]
    for i in range(n):
        j = (i + 1) % n
        faces.append((i, j, n + j, n + i))
    mesh = bpy.data.meshes.new(name + " mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.materials.append(material)
    obj = bpy.data.objects.new(name, mesh)
    col.objects.link(obj)
    bevel = obj.modifiers.new("Soft door edges", "BEVEL")
    bevel.width = 0.035
    bevel.segments = 3
    obj.modifiers.new("Weighted normals", "WEIGHTED_NORMAL")
    return obj


def ico(name, loc, radius, material, col, subdivisions=1):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=subdivisions, radius=radius, location=loc)
    obj = bpy.context.object
    obj.name = name
    if material:
        obj.data.materials.append(material)
    if col:
        move_to_collection(obj, col)
    return obj


def create_shelf(col, x, y, z, width=1.6):
    cube("Shelf board", (x, y, z), (width, 0.5, 0.14), M["wood_top"], 0.05, col)
    cube("Shelf bracket L", (x - width * 0.35, y + 0.16, z - 0.21), (0.10, 0.18, 0.33), M["wood"], 0.025, col)
    cube("Shelf bracket R", (x + width * 0.35, y + 0.16, z - 0.21), (0.10, 0.18, 0.33), M["wood"], 0.025, col)


def make_book(col, loc, color):
    base = cube("Hand-bound book", loc, (0.32, 0.44, 0.10), color, 0.035, col)
    cube("Book page block", (loc[0], loc[1] - 0.01, loc[2] + 0.055), (0.28, 0.39, 0.018), M["cream"], 0.008, col)
    return base


def make_coin_stack(col, x, y, z, count=3):
    for i in range(count):
        coin = cylinder("Dream coin", (x, y, z + i * 0.085), 0.18, 0.07, M["gold"], col, vertices=24, bevel=0.018)
        cylinder("Coin stamped star", (x, y, z + i * 0.085 + 0.039), 0.055, 0.012, M["brass"], col, vertices=8)


def make_jar(col, x, y, z, icon_material, icon_kind="leaf"):
    cylinder("Frosted jar body", (x, y, z + 0.35), 0.28, 0.66, M["glass"], col, vertices=16, bevel=0.035)
    cylinder("Jar shoulder", (x, y, z + 0.68), 0.21, 0.06, M["cream"], col, vertices=16, bevel=0.012)
    cylinder("Brass jar lid", (x, y, z + 0.74), 0.23, 0.10, M["wood_light"], col, vertices=16, bevel=0.018)
    cube("Icon label", (x, y - 0.278, z + 0.34), (0.34, 0.028, 0.28), M["cream"], 0.035, col)
    if icon_kind == "heart":
        sphere("Heart icon left", (x - 0.055, y - 0.31, z + 0.38), (0.07, 0.035, 0.07), icon_material, col)
        sphere("Heart icon right", (x + 0.055, y - 0.31, z + 0.38), (0.07, 0.035, 0.07), icon_material, col)
        ico("Heart icon point", (x, y - 0.31, z + 0.29), 0.075, icon_material, col)
    elif icon_kind == "star":
        ico("Star icon", (x, y - 0.31, z + 0.36), 0.105, icon_material, col, subdivisions=1)
    else:
        cylinder("Sprout stem", (x, y - 0.31, z + 0.35), 0.018, 0.12, icon_material, col, vertices=8)
        sphere("Sprout leaf L", (x - 0.05, y - 0.32, z + 0.39), (0.06, 0.035, 0.035), icon_material, col)
        sphere("Sprout leaf R", (x + 0.05, y - 0.32, z + 0.42), (0.06, 0.035, 0.035), icon_material, col)


def build_savings_room(col):
    # Floor and tall old-house walls
    cube("Room 1 floor", (0, 1.4, -0.17), (12, 9.2, 0.34), M["floor"], 0.10, col)
    cube("Room 1 back wall", (0, 5.9, 3.0), (12, 0.28, 6.0), M["wall"], 0.05, col)
    # Keep both side edges open so the browser camera can read the set clearly.
    for x in (-5.65, 5.65):
        cube("Open-set corner post", (x, 4.7, 3.0), (0.22, 0.24, 6.0), M["wood"], 0.06, col)
    # Wallpaper rhythm and wall rails
    for x in range(-5, 6, 2):
        cube("Wallpaper vertical seam", (x, 5.72, 3.0), (0.025, 0.018, 5.4), M["wall_light"], 0.008, col)
        for z in (1.0, 2.0, 3.0, 4.0, 5.0):
            ico("Wallpaper stitched diamond", (x + 0.48, 5.69, z), 0.11, M["wall_light"], col)
    cube("Back wall dado rail", (0, 5.68, 1.05), (11.6, 0.10, 0.14), M["wood_light"], 0.035, col)
    # Tall arched door and warm keyhole
    arch_door("Arched dream door", 0, 5.48, 0.0, 2.25, 3.05, 1.12, 0.18, M["wood"], col)
    for x in (-1.25, 1.25):
        cube("Door jamb", (x, 5.36, 1.75), (0.18, 0.28, 3.5), M["wood_light"], 0.05, col)
    curve_line("Door arch frame", [(1.25 * math.cos(a), 5.34, 3.05 + 1.25 * math.sin(a)) for a in [math.pi * i / 24 for i in range(25)]], 0.09, M["wood_light"], col)
    sphere("Keyhole circle", (0, 5.22, 2.1), (0.13, 0.055, 0.13), M["glass_glow"], col)
    cube("Keyhole stem", (0, 5.21, 1.96), (0.08, 0.055, 0.22), M["brass"], 0.025, col)
    for x in (-0.66, 0.66):
        cube("Door inset panel", (x, 5.24, 1.46), (0.56, 0.05, 1.78), M["wood_light"], 0.075, col)
        cube("Door inset shadow", (x, 5.20, 1.46), (0.43, 0.035, 1.55), M["wood"], 0.055, col)
    cube("Door lower rail", (0, 5.20, 0.36), (1.85, 0.07, 0.14), M["wood_light"], 0.04, col)
    # Work table
    cube("Savings table top", (0, 0.25, 1.18), (4.7, 1.35, 0.20), M["wood_top"], 0.09, col)
    for x in (-2.0, 2.0):
        for y in (-0.23, 0.73):
            cube("Carved table leg", (x, y, 0.62), (0.22, 0.22, 1.0), M["wood"], 0.07, col)
    cube("Table apron", (0, 0.25, 0.90), (4.2, 1.05, 0.30), M["wood"], 0.06, col)
    # Needs / wish / savings jars with non-text icons
    make_jar(col, -1.25, 0.03, 1.29, M["rust"], "heart")
    make_jar(col, 0.0, 0.03, 1.29, M["gold"], "star")
    make_jar(col, 1.25, 0.03, 1.29, M["leaf"], "leaf")
    make_coin_stack(col, -0.15, -0.62, 1.31, 3)
    make_coin_stack(col, 0.38, -0.60, 1.31, 2)
    # Bookshelves and small props
    create_shelf(col, -4.45, 5.45, 4.2, 2.0)
    create_shelf(col, -4.45, 5.45, 3.25, 2.0)
    create_shelf(col, 4.40, 5.45, 4.55, 1.8)
    for i, color in enumerate((M["rust"], M["felt"], M["wood_light"], M["blue"])):
        make_book(col, (-5.05 + i * 0.34, 5.19, 4.43), color)
        make_book(col, (-4.95 + i * 0.35, 5.18, 3.47), color)
    cube("Ledger cover", (2.15, -0.01, 1.31), (0.68, 0.50, 0.08), M["felt"], 0.035, col)
    cube("Ledger pages", (2.15, -0.025, 1.36), (0.60, 0.44, 0.025), M["cream"], 0.012, col)
    # A gentle hanging lamp
    cylinder("Lamp canopy", (-3.25, 1.8, 5.2), 0.25, 0.12, M["wood"], col, vertices=12)
    curve_line("Lamp cord", [(-3.25, 1.8, 5.2), (-3.25, 1.8, 4.2)], 0.018, M["dark"], col)
    sphere("Warm lamp globe", (-3.25, 1.8, 4.03), (0.20, 0.20, 0.25), M["glass_glow"], col)


def add_plant(col, x, y, z, height, leaf_mat, flower_mat=None):
    cylinder("Velvety plant stem", (x, y, z + height / 2), 0.045, height, M["leaf"], col, vertices=10)
    for side, h in ((-1, 0.38), (1, 0.62), (-1, 0.79)):
        sphere("Soft leaf", (x + side * 0.16, y - 0.02, z + height * h), (0.19, 0.09, 0.08), leaf_mat, col)
    if flower_mat:
        sphere("Flower heart", (x, y, z + height + 0.06), (0.09, 0.08, 0.09), M["gold"], col)
        for i in range(6):
            a = math.tau * i / 6
            sphere("Soft flower petal", (x + math.cos(a) * 0.13, y + math.sin(a) * 0.10, z + height + 0.06), (0.10, 0.075, 0.06), flower_mat, col)


def build_mist_garden(col):
    cube("Garden floor", (0, 1.5, -0.17), (12, 9.3, 0.34), M["floor"], 0.10, col)
    cube("Greenhouse back wall", (0, 5.8, 3.0), (12, 0.24, 6.0), M["wall"], 0.05, col)
    # Frame a greenhouse arch; keep the front open for clear gameplay visibility.
    for x in (-5.5, -3.6, -1.8, 0, 1.8, 3.6, 5.5):
        curve_line("Greenhouse brass rib", [(x, 4.2, 0.15), (x, 4.2, 3.8), (x * 0.78, 4.2, 5.5)], 0.045, M["wood_light"], col)
    for z in (1.2, 2.4, 3.6, 4.7):
        cube("Greenhouse cross rail", (0, 4.18, z), (10.8, 0.11, 0.08), M["wood_light"], 0.025, col)
    # Soft winding path
    cube("Garden path stone 1", (0, -0.2, 0.025), (1.5, 1.0, 0.08), M["path"], 0.12, col)
    cube("Garden path stone 2", (0.12, 1.0, 0.03), (1.4, 0.85, 0.08), M["path"], 0.12, col)
    cube("Garden path stone 3", (-0.08, 2.05, 0.03), (1.55, 0.8, 0.08), M["path"], 0.12, col)
    # Two distinct seed beds: moonbeans and starflowers
    for x, bed_name, leaf_mat, flower_mat in (
        (-2.0, "Moonbean bed", M["leaf"], M["blue"]),
        (2.0, "Starflower bed", M["leaf_light"], M["flower"]),
    ):
        cube(bed_name + " carved planter", (x, 1.30, 0.42), (2.75, 2.15, 0.62), M["wood_top"], 0.12, col)
        cube(bed_name + " soil", (x, 1.30, 0.76), (2.48, 1.90, 0.12), M["soil"], 0.05, col)
        for row in range(2):
            for plant in range(3):
                px = x - 0.72 + plant * 0.72
                py = 0.72 + row * 1.05
                add_plant(col, px, py, 0.83, 0.72 + 0.08 * ((plant + row) % 2), leaf_mat, flower_mat)
        for dx in (-1.15, -0.75, 0.75, 1.15):
            cube("Planter stitched patch", (x + dx, 0.18, 0.43), (0.12, 0.035, 0.12), M["felt_light"], 0.03, col)
    # Decorative greenhouse lanterns and hanging stars
    for x in (-4.25, 4.25):
        cylinder("Garden lantern post", (x, 1.5, 1.0), 0.07, 1.7, M["wood"], col, vertices=12)
        cube("Lantern cap", (x, 1.5, 1.95), (0.40, 0.40, 0.12), M["brass"], 0.06, col)
        sphere("Garden lantern globe", (x, 1.5, 1.72), (0.20, 0.20, 0.24), M["glass_glow"], col)
    for x in (-4.6, -2.8, 2.9, 4.7):
        curve_line("Hanging vine", [(x, 4.0, 5.4), (x + 0.12, 3.98, 4.8), (x - 0.08, 3.95, 4.3)], 0.025, M["leaf"], col)
        sphere("Vine leaf", (x + 0.14, 3.92, 4.77), (0.12, 0.05, 0.055), M["leaf_light"], col)
    # A warm arched door, visually connecting both rooms
    arch_door("Garden exit door", 0, 5.48, 0.0, 2.1, 2.9, 1.05, 0.16, M["wood"], col)
    for x in (-1.16, 1.16):
        cube("Garden door frame", (x, 5.34, 1.55), (0.17, 0.25, 3.1), M["wood_light"], 0.05, col)
    curve_line("Garden door arch trim", [(1.16 * math.cos(a), 5.31, 2.9 + 1.16 * math.sin(a)) for a in [math.pi * i / 24 for i in range(25)]], 0.08, M["wood_light"], col)
    sphere("Garden door keyhole", (0, 5.18, 1.98), (0.12, 0.05, 0.12), M["glass_glow"], col)


def create_character(col):
    arm_data = bpy.data.armatures.new("Dream Keeper rig data")
    rig = bpy.data.objects.new("Dream Keeper puppet rig", arm_data)
    col.objects.link(rig)
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    bones = {
        "root": ((0, 0, 0.0), (0, 0, 0.35), None),
        "body": ((0, 0, 0.38), (0, 0, 0.88), "root"),
        "head": ((0, 0, 0.82), (0, 0, 1.36), "body"),
        "cape": ((0, 0, 0.80), (0, 0, 0.42), "body"),
        "arm.L": ((-0.24, 0, 0.79), (-0.55, -0.02, 0.57), "body"),
        "arm.R": ((0.24, 0, 0.79), (0.54, -0.02, 0.57), "body"),
        "lantern": ((-0.55, -0.02, 0.57), (-0.59, -0.02, 0.38), "arm.L"),
        "leg.L": ((-0.14, 0, 0.46), (-0.16, 0, 0.08), "root"),
        "leg.R": ((0.14, 0, 0.46), (0.16, 0, 0.08), "root"),
    }
    edit_bones = {}
    for name, (head, tail, parent) in bones.items():
        b = arm_data.edit_bones.new(name)
        b.head = head
        b.tail = tail
        if parent:
            b.parent = edit_bones[parent]
        edit_bones[name] = b
    bpy.ops.object.mode_set(mode="OBJECT")
    rig.show_in_front = True
    rig.display_type = "WIRE"

    def part(obj, bone):
        world = obj.matrix_world.copy()
        obj.parent = rig
        obj.parent_type = "BONE"
        obj.parent_bone = bone
        obj.matrix_world = world
        return obj

    # Hood and rounded face
    part(sphere("Patchwork hood", (0, 0.02, 1.18), (0.48, 0.45, 0.57), M["felt"], col, 20, 14), "head")
    part(sphere("Dream Keeper clay face", (0, -0.275, 1.19), (0.34, 0.20, 0.40), M["skin"], col, 20, 14), "head")
    part(sphere("Eye L", (-0.10, -0.455, 1.25), (0.035, 0.025, 0.045), M["dark"], col), "head")
    part(sphere("Eye R", (0.10, -0.455, 1.25), (0.035, 0.025, 0.045), M["dark"], col), "head")
    # Felt cape torso, rounded hem and tiny stitched patches
    part(cone("Teal patchwork cape", (0, 0.01, 0.66), 0.48, 0.25, 0.82, M["felt"], col, vertices=16, bevel=0.04), "body")
    part(sphere("Cape shoulder", (0, 0.00, 0.92), (0.42, 0.36, 0.22), M["felt_light"], col), "body")
    for x, z in ((-0.26, 0.55), (0.24, 0.68), (-0.12, 0.82)):
        part(cube("Sewn cape patch", (x, -0.30, z), (0.13, 0.025, 0.12), M["rust"], 0.025, col), "cape")
    for x, z in ((-0.32, 0.66), (0.31, 0.61), (-0.28, 0.84), (0.28, 0.82)):
        part(sphere("Cape stitch", (x, -0.32, z), (0.018, 0.015, 0.018), M["cream"], col, 8, 6), "cape")
    # Arms, hands, leggings, and soft boots
    for side, bone in ((-1, "arm.L"), (1, "arm.R")):
        arm = cylinder("Sleeve", (side * 0.40, 0.00, 0.68), 0.12, 0.46, M["felt_light"], col, vertices=12)
        arm.rotation_euler[1] = side * -0.65
        part(arm, bone)
        part(sphere("Clay hand", (side * 0.56, -0.06, 0.54), (0.105, 0.10, 0.10), M["skin"], col), bone)
    for side, bone in ((-1, "leg.L"), (1, "leg.R")):
        part(cylinder("Rust leggings", (side * 0.14, 0, 0.31), 0.105, 0.34, M["rust"], col, vertices=12), bone)
        part(sphere("Rounded felt boot", (side * 0.16, -0.08, 0.10), (0.16, 0.25, 0.13), M["wood"], col), bone)
    # Satchel and brass firefly lantern
    part(cube("Dream Keeper round satchel", (0.34, -0.19, 0.56), (0.30, 0.20, 0.32), M["wood_light"], 0.10, col), "body")
    part(curve_line("Satchel strap", [(0.20, -0.37, 0.98), (0.36, -0.37, 0.80), (0.46, -0.31, 0.59)], 0.025, M["rust"], col), "body")
    part(cylinder("Lantern brass body", (-0.60, -0.10, 0.40), 0.14, 0.30, M["brass"], col, vertices=12, bevel=0.025), "lantern")
    part(sphere("Firefly lantern glass", (-0.60, -0.12, 0.40), (0.095, 0.09, 0.12), M["glass_glow"], col), "lantern")
    part(curve_line("Lantern handle", [(-0.70, -0.10, 0.54), (-0.60, -0.10, 0.67), (-0.50, -0.10, 0.54)], 0.018, M["brass"], col), "lantern")
    # Actions use pose-to-pose timing with eased curves.
    rig.animation_data_create()
    poses = {
        "Idle": [
            (1, 0.00, 0.00, 0.00, 0.00, 0.00),
            (13, 0.035, 0.035, -0.06, 0.05, 0.02),
            (25, 0.00, 0.00, 0.00, 0.00, 0.00),
        ],
        "Walk": [
            (1, 0.00, -0.05, -0.35, 0.35, -0.20),
            (7, 0.055, 0.06, 0.35, -0.35, 0.20),
            (13, 0.00, -0.05, -0.35, 0.35, -0.20),
            (19, 0.055, 0.06, 0.35, -0.35, 0.20),
            (25, 0.00, -0.05, -0.35, 0.35, -0.20),
        ],
        "Reach": [
            (1, 0.00, 0.00, 0.00, 0.00, 0.00),
            (8, 0.025, -0.10, -0.12, -0.95, 0.12),
            (16, 0.025, -0.10, -0.12, -0.95, 0.12),
            (24, 0.00, 0.00, 0.00, 0.00, 0.00),
        ],
        "KeyUnlock": [
            (1, 0.00, 0.00, 0.00, 0.00, 0.00),
            (7, 0.15, 0.02, -0.90, 0.90, 0.0),
            (13, 0.08, 0.02, -0.90, 0.90, 0.0),
            (25, 0.00, 0.00, 0.00, 0.00, 0.0),
        ],
    }
    for action_name, frames in poses.items():
        action = bpy.data.actions.new(action_name)
        rig.animation_data.action = action
        for frame, bob, sway, left_arm, right_arm, leg in frames:
            root_bone = rig.pose.bones["root"]
            root_bone.location = (0, 0, bob)
            root_bone.rotation_mode = "XYZ"
            root_bone.rotation_euler = (0, sway, 0)
            rig.pose.bones["arm.L"].rotation_mode = "XYZ"
            rig.pose.bones["arm.L"].rotation_euler = (0, left_arm, 0)
            rig.pose.bones["arm.R"].rotation_mode = "XYZ"
            rig.pose.bones["arm.R"].rotation_euler = (0, right_arm, 0)
            rig.pose.bones["leg.L"].rotation_mode = "XYZ"
            rig.pose.bones["leg.L"].rotation_euler = (0, leg, 0)
            rig.pose.bones["leg.R"].rotation_mode = "XYZ"
            rig.pose.bones["leg.R"].rotation_euler = (0, -leg, 0)
            for bone_name in ("root", "arm.L", "arm.R", "leg.L", "leg.R"):
                rig.pose.bones[bone_name].keyframe_insert("location", frame=frame, group=bone_name)
                rig.pose.bones[bone_name].keyframe_insert("rotation_euler", frame=frame, group=bone_name)
        for fcurve in getattr(action, "fcurves", []):
            for key in fcurve.keyframe_points:
                key.interpolation = "BEZIER"
        action.use_fake_user = True
    rig.animation_data.action = bpy.data.actions.get("Idle")
    bpy.context.scene.frame_end = 25
    return rig


def setup_lighting(camera_col):
    def area(name, loc, energy, color, size, target=(0, 2.0, 1.6)):
        data = bpy.data.lights.new(name, "AREA")
        data.energy = energy
        data.color = color
        data.shape = "DISK"
        data.size = size
        obj = bpy.data.objects.new(name, data)
        camera_col.objects.link(obj)
        obj.location = loc
        obj.rotation_euler = (Vector(target) - obj.location).to_track_quat("-Z", "Y").to_euler()
        return obj
    area("Soft warm key", (-4.5, -5.0, 7.5), 1050, (1.0, 0.65, 0.34), 4.5)
    area("Cool moon fill", (5.0, 0.0, 6.0), 320, (0.44, 0.64, 0.78), 6.0)
    area("Door amber rim", (0.0, 4.2, 4.5), 440, (1.0, 0.42, 0.16), 2.5)
    camera_data = bpy.data.cameras.new("Miniature set camera")
    camera = bpy.data.objects.new("Miniature set camera", camera_data)
    camera_col.objects.link(camera)
    camera.location = (7.6, -15.0, 8.0)
    target = Vector((0.0, 1.8, 2.2))
    camera.rotation_euler = (target - camera.location).to_track_quat("-Z", "Y").to_euler()
    camera_data.type = "ORTHO"
    camera_data.ortho_scale = 13.0
    bpy.context.scene.camera = camera


def export_objects(objects, filepath, animations=False):
    bpy.ops.object.select_all(action="DESELECT")
    selected = []
    for obj in objects:
        if obj.type not in {"CAMERA", "LIGHT"}:
            obj.select_set(True)
            selected.append(obj)
    if not selected:
        raise RuntimeError(f"No export objects for {filepath}")
    bpy.context.view_layer.objects.active = selected[0]
    options = dict(
        filepath=str(filepath),
        export_format="GLB",
        use_selection=True,
        export_animations=animations,
        export_image_format="AUTO",
    )
    if animations:
        options["export_animation_mode"] = "ACTIONS"
        options["export_nla_strips"] = False
    bpy.ops.export_scene.gltf(**options)
    bpy.ops.object.select_all(action="DESELECT")


def render_preview(scene, active_col, other_col, filepath):
    for obj in other_col.objects:
        obj.hide_render = True
    for obj in active_col.objects:
        obj.hide_render = False
    scene.render.filepath = str(filepath)
    scene.camera.data.ortho_scale = 13.0
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 900
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_percentage = 80
    scene.render.film_transparent = False
    scene.render.image_settings.color_mode = "RGBA"
    scene.world.use_nodes = True
    scene.world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.075, 0.065, 0.045, 1)
    scene.world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.25
    scene.view_settings.view_transform = "AgX"
    try:
        scene.view_settings.look = "AgX - Medium High Contrast"
    except Exception:
        pass
    bpy.ops.render.render(write_still=True)
    for obj in other_col.objects:
        obj.hide_render = False


def main():
    clear_scene()
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 900
    scene.render.resolution_percentage = 80
    room1 = collection("01 — Savings Room")
    room2 = collection("02 — Mist Garden")
    character_col = collection("Character — Dream Keeper")
    staging = collection("Render camera and lights")
    build_savings_room(room1)
    build_mist_garden(room2)
    rig = create_character(character_col)
    setup_lighting(staging)
    rig.location = (-3.0, -0.55, 0.0)

    # Preview and export each room as a separate reusable GLB.
    render_preview(scene, room1, room2, PREVIEWS / "savings-room.png")
    export_objects(list(room1.objects), EXPORTS / "savings-room.glb", animations=False)
    render_preview(scene, room2, room1, PREVIEWS / "mist-garden.png")
    export_objects(list(room2.objects), EXPORTS / "mist-garden.glb", animations=False)

    # Render the character near the shared gameplay area for review.
    for obj in room1.objects:
        obj.hide_render = False
    for obj in room2.objects:
        obj.hide_render = True
    rig.location = (-3.0, -0.55, 0.0)
    scene.frame_set(1)
    bpy.context.view_layer.update()
    scene.render.filepath = str(PREVIEWS / "dream-keeper-character.png")
    bpy.ops.render.render(write_still=True)
    # Keep the character asset at the origin for Godot instancing.
    rig.location = (0, 0, 0)
    export_objects(list(character_col.objects), EXPORTS / "dream-keeper.glb", animations=True)

    # Save editable Blender source with the full set, lights, camera, and actions.
    bpy.ops.object.select_all(action="DESELECT")
    bpy.ops.wm.save_as_mainfile(filepath=str(SOURCE / "mist-garden-source.blend"))
    print("ASSET_BUILD_OK")
    print("SOURCE", SOURCE / "mist-garden-source.blend")
    print("GLB", EXPORTS / "savings-room.glb")
    print("GLB", EXPORTS / "mist-garden.glb")
    print("GLB", EXPORTS / "dream-keeper.glb")
    print("PREVIEW", PREVIEWS / "savings-room.png")
    print("PREVIEW", PREVIEWS / "mist-garden.png")
    print("PREVIEW", PREVIEWS / "dream-keeper-character.png")


if __name__ == "__main__":
    main()
