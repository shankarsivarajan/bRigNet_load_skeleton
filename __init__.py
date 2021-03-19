# ====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation, version 3.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ======================= END GPL LICENSE BLOCK ========================


bl_info = {
    "name": "bRigNet (Load RigNet skeleton)",
    "version": (0, 0, 1),
    "author": "Shankar Sivarajan", # Mostly Paolo Acampora.
    "blender": (2, 92, 0),
    "description": "bRigNet: load RigNet skeleton",
    "location": "3D View Sidebar > bRigNet tab",
    "doc_url": "https://github.com/pKrime/brignet",
    "category": "Rigging",
}

import bpy

from . import brignet, preferences, loadskeleton

from importlib import reload
try:
    reload(brignet)
    reload(preferences)
    reload(loadskeleton)
except NameError:
    pass

from .preferences import BrignetPrefs
from .loadskeleton import LoadRignetSkeleton, LoadSkeletonPanel


def register():
    from importlib import reload
    try:
        reload(brignet)
        reload(preferences)
        reload(loadskeleton)
    except NameError:
        pass

    brignet.register_properties()
    bpy.utils.register_class(BrignetPrefs)
    
    bpy.utils.register_class(LoadRignetSkeleton)
    bpy.utils.register_class(LoadSkeletonPanel)

    if not BrignetPrefs.append_rignet():
        print("RigNet not found, please set in bRigNet preferences")
    if not BrignetPrefs.append_modules():
        print("Modules path not found, please set in bRigNet preferences")


def unregister():
    try:
        from . import rignetconnect
        rignetconnect.clear()
    except ModuleNotFoundError:
        # if we have failed to load rignetconnect, we have no device to clear
        pass
    
    bpy.utils.unregister_class(BrignetPrefs)
    bpy.utils.unregister_class(LoadSkeletonPanel)
    bpy.utils.unregister_class(LoadRignetSkeleton)
    brignet.unregister_properties()
