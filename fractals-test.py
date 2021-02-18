import FreeCAD
from FreeCAD import Vector, Placement, Rotation
import Part


def pyramide(side: int, height: int, s: Vector):
    doc = FreeCAD.activeDocument()
    v = doc.addObject("Part::Vertex","Vertex")
    offset = side / 2
    v.Placement = Placement(Vector(s.x + offset, s.y + offset, s.z + height), Rotation(0, 0, 1))

    vec1 = Vector(s.x, s.y, s.z)
    vec2 = Vector(s.x, s.y + side, s.z)
    vec3 = Vector(s.x + side, s.y + side, s.z)
    vec4 = Vector(s.x + side, s.y, s.z) 

    Part.show(Part.makePolygon([vec1, vec2, vec3, vec4, vec1]))
    obj = doc.Objects[-1]

    loft = doc.addObject("Part::Loft", "Pyramide")
    loft.Sections = [v, obj]
    loft.Solid = True
    loft.Ruled = True
    loft.Closed = False

if __name__ == "__main__":
    pyramide(10, 20, Vector(0, 0, 0))
