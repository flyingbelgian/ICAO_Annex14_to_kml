import FreeCAD as App
import Part


DOC = App.activeDocument()
DOC_NAME = "Annex14"


if DOC is None:
    App.newDocument(DOC_NAME)
    App.setActiveDocument(DOC_NAME)
    DOC = App.activeDocument()
else:
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)


def setview():
    """Rearrange View"""
    App.Gui.SendMsgToActiveView("ViewFit")
    App.Gui.activeDocument().activeView().viewIsometric()
    App.Gui.activeDocument().activeView().setAxisCross(True)


def makeSurfLines(V1, V2, V3, V4):
    """Make a surface bound by 4 vertices"""
    L1 = Part.LineSegment(V1, V2)
    L3 = Part.LineSegment(V3, V4)
    E1 = Part.Edge(L1)
    E3 = Part.Edge(L3)
    surf = Part.makeRuledSurface(E1, E3)
    return surf


def makeSurfArcs(Arc1, Arc2):
    surf = Part.makeRuledSurface(Arc1, Arc2)
    return surf


def fuseObjects(name, objects):
    obj = DOC.addObject("Part::MultiFuse", name)
    obj.Shapes = objects
    return obj


m = 1

rwy_end_w_x = 596775.95 * m
rwy_end_w_y = 6219547.72 * m
rwy_end_w_z = 166 * m
rwy_end_w = App.Vector(rwy_end_w_x, rwy_end_w_y, rwy_end_w_z)
rwy_end_e_x = 597856.34 * m
rwy_end_e_y = 6219933.48 * m
rwy_end_e_z = 167 * m
rwy_end_e = App.Vector(rwy_end_e_x, rwy_end_e_y, rwy_end_e_z)

rwy_length = 1147.95 * m
rwy_angle = 69.68

inner_horizontal_radius = 2500 * m
inner_horizontal_height = 45 * m
conical_radius = inner_horizontal_radius + 1100 * m
conical_height = inner_horizontal_height + 55 * m

V1 = App.Vector(-inner_horizontal_radius, 0, inner_horizontal_height)
V2 = App.Vector(-inner_horizontal_radius, rwy_length, inner_horizontal_height)
V3 = App.Vector(0, rwy_length + inner_horizontal_radius, inner_horizontal_height)
V4 = App.Vector(inner_horizontal_radius, rwy_length, inner_horizontal_height)
V5 = App.Vector(inner_horizontal_radius, 0, inner_horizontal_height)
V6 = App.Vector(0, -inner_horizontal_radius, inner_horizontal_height)
V7 = App.Vector(-conical_radius, 0, conical_height)
V8 = App.Vector(-conical_radius, rwy_length, conical_height)
V9 = App.Vector(0, rwy_length + conical_radius, conical_height)
V10 = App.Vector(conical_radius, rwy_length, conical_height)
V11 = App.Vector(conical_radius, 0, conical_height)
V12 = App.Vector(0, -conical_radius, conical_height)

line_w_inner = Part.LineSegment(V1, V2)
line_w_outer = Part.LineSegment(V7, V8)
line_e_inner = Part.LineSegment(V4, V5)
line_e_outer = Part.LineSegment(V10, V11)

arc_start_inner = Part.Arc(V1, V6, V5)
arc_start_outer = Part.Arc(V7, V12, V11)
arc_end_inner = Part.Arc(V2, V3, V4)
arc_end_outer = Part.Arc(V8, V9, V10)

conical_inner = Part.Shape([line_w_inner, arc_end_inner, line_e_inner, arc_start_inner])
conical_outer = Part.Shape([line_w_outer, arc_end_outer, line_e_outer, arc_start_outer])

wire_inner = Part.Wire(conical_inner.Edges)
wire_outer = Part.Wire(conical_outer.Edges)

inner_horizontal = DOC.addObject("Part::Feature", "Inner_Horizontal")
inner_horizontal.Shape = Part.Face(wire_inner)

conical = DOC.addObject("Part::Feature", "Conical")
conical.Shape = Part.makeRuledSurface(wire_inner, wire_outer)

inner_horizontal.Placement = App.Placement(
    rwy_end_w, App.Rotation(-rwy_angle, 0, 0), App.Vector(0, 0, 0))
conical.Placement = App.Placement(rwy_end_w, App.Rotation(-rwy_angle, 0, 0), App.Vector(0, 0, 0))

DOC.recompute()
setview()
