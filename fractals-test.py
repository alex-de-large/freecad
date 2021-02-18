import FreeCAD
from FreeCAD import Vector, Placement, Rotation
import Part


def pyramid(side: int, height: int, s: Vector):
    doc = FreeCAD.activeDocument()
    v = doc.addObject("Part::Vertex", "Vertex")
    offset = side / 2
    v.Placement = Placement(Vector(s.x + offset, s.y + offset, s.z + height), Rotation(0, 0, 1))

    vec1 = Vector(s.x, s.y, s.z)
    vec2 = Vector(s.x, s.y + side, s.z)
    vec3 = Vector(s.x + side, s.y + side, s.z)
    vec4 = Vector(s.x + side, s.y, s.z)

    Part.show(Part.makePolygon([vec1, vec2, vec3, vec4, vec1]))
    obj = doc.Objects[-1]

    loft = doc.addObject("Part::Loft", "Pyramid")
    loft.Sections = [v, obj]
    loft.Solid = True
    loft.Ruled = True
    loft.Closed = False


def sierpinski_3d(n: int):

    def sierpinski_supp(i, side, height, s: Vector):
        if i == 0:
            pyramid(side, height, s)
            return

        new_side = side / 2
        new_height = height / 2

        vec1 = Vector(s.x, s.y, s.z)
        vec2 = Vector(s.x, s.y + new_side, s.z)
        vec3 = Vector(s.x + new_side, s.y + new_side, s.z)
        vec4 = Vector(s.x + new_side, s.y, s.z)
        vec5 = Vector(s.x + new_side / 2, s.y + new_side / 2, s.z + new_height)
        vecs = [vec1, vec2, vec3, vec4, vec5]
        for vec in vecs:
            sierpinski_supp(i - 1, new_side, new_height, vec)

    sierpinski_supp(n, 1000, 1000, Vector(0, 0, 0))


if __name__ == "__main__":
    sierpinski_3d(5)
