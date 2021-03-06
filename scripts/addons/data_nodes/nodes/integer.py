import bpy
from bpy.types import NodeTree, Node, NodeSocket
from ..utils import send_value


class Integer(Node):
    """Integer node"""
    bl_idname = 'IntegerNodeType'
    bl_label = 'Integer'

    def update_props(self, context):
        self.update()

    int_prop: bpy.props.IntProperty(
        name='Int', default=1, update=update_props)

    def init(self, context):
        self.outputs.new('NodeSocketInt', 'Int')

    def update(self):
        send_value(self.outputs, self.int_prop)

    def draw_buttons(self, context, layout):
        layout.prop(self, 'int_prop')

    def draw_label(self):
        return 'Int'
