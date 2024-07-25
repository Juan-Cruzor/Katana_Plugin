from katana import NodegraphAPI, LayeredMenuAPI, RenderingAPI


def populate_callback(layered_menu):
    """"""
    renderer = RenderingAPI.RenderPlugins.GetDefaultRendererPluginName()
    info = RenderingAPI.RenderPlugins.GetInfoPlugin(renderer)
    shader_type = RenderingAPI.RendererInfo.kRendererObjectTypeShader
    shader_names = info.getRendererObjectNames(shader_type)
    # If it has the word "light" in the string the color will be diferent.
    for shader_name in shader_names:
        if "light" in shader_name:
            color = [0.0, 0.0, 0.8]
        else:
            color = [0.0, 0.8, 0.0]

        layered_menu.addEntry(shader_name, text = shader_name, color = color)

def action_callback(value):
    """"""
    renderer = RenderingAPI.RenderPlugins.GetDefaultRendererPluginName()
    if renderer == "arnold":
        # NodeType is Shading Node.
        node = NodegraphAPI.CreateNode("ArnoldShadingNode")
        node.getParameter("nodeType").setValue(value, 0)
        node.setName(value)
        node.getParameter("name").setValue(node.getName(), 0)
        # Update Dynamic Parameters in node.
        node.checkDynamicParameters()

        return node
    
    else:

        return 
    
    # This will create the keyboard shortcut in the selected key.
    layered_Menu = LayeredMenuAPI.LayeredMenu(populate_callback, action_callback, "s", alwaysPopulate = "false")

    # Register the created Menu
    LayeredMenuAPI.RegisterLayeredMenu(layered_menu, "get_shading_nodes")

    