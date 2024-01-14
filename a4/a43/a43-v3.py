#!/usr/bin/env python
"""Assignment 4 Part 1 Version 2 template"""
print(__doc__)

from typing import IO, List, NamedTuple
from enum import Enum
import random


class Colour(NamedTuple):
    """Stores the colours stats"""
    red: int
    green: int
    blue: int
    opacity: float


class ShapeKind(str, Enum):
    """Supports shape kinds"""
    CIRCLE = 0
    RECTANGLE = 1
    ELLIPSIS = 2

    def __str__(self) -> str:
        return f'{self.value}'


class Irange(NamedTuple):
    """Range with the min and max colour values"""
    imin: int
    imax: int

    def __str__(self) -> str:
        return f'{self.imin},{self.imax}'


class Extent(NamedTuple):
    """Extent definition based on width and height ranges"""
    width: Irange
    height: Irange


class Frange(NamedTuple):
    """Range with the min and max opacity values"""
    fmin: float
    fmax: float

    def __str__(self) -> str:
        return f'{self.fmin},{self.fmax}'


class CircleCoordinates(NamedTuple):
    """Stores the coordinates of the circle"""
    x_coordinate: int
    y_coordinate: int
    radius: int


def gen_int(r: Irange) -> int:
    """gen_int method"""
    """Generates a randon integer"""
    return random.randint(r.imin, r.imax)


def gen_float(r: Frange) -> float:
    """gen_float method"""
    """Generates a randon float"""
    return random.uniform(r.fmin, r.fmax)


class RectangleCoordinates(NamedTuple):
    """Stores the coordinates of the rectangle"""
    x_coordinate: int
    y_coordinate: int
    width: int
    height: int


class Circle:
    """Circle class"""
    def __init__(self, cir: CircleCoordinates, col: Colour) -> None:
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]


class Rectangle:
    """Rectangle class"""
    def __init__(self, rect: RectangleCoordinates, col: Colour) -> None:
        """Initializes a rectangle"""
        self.x_coord: int = rect[0]
        self.y_coord: int = rect[1]
        self.width: int = rect[2]
        self.height: int = rect[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]


class Random:
    """Random class"""
    def __init__(self, SHA: ShapeKind, RAD: Irange, RWH: Extent, col: Colour):
        self.SHA: int = random.choice(SHA)
        self.X: int = gen_int(Irange(PyArtConfig.XMIN, PyArtConfig.XMAX))
        self.Y: int = gen_int(Irange(PyArtConfig.YMIN, PyArtConfig.YMAX))
        self.RAD: int = gen_int(RAD)
        self.RX: int = gen_int(Irange(PyArtConfig.RXMIN, PyArtConfig.RXMAX))
        self.RY: int = gen_int(Irange(PyArtConfig.RYMIN, PyArtConfig.RYMAX))
        self.W: int = gen_int(RWH[0])
        self.H: int = gen_int(RWH[1])
        self.R: int = gen_int(Irange(PyArtConfig.REDMIN, col[0]))
        self.G: int = gen_int(Irange(PyArtConfig.GREENMIN, col[1]))
        self.B: int = gen_int(Irange(PyArtConfig.BLUEMIN, col[2]))
        self.OP: float = gen_float(Frange(PyArtConfig.OPMIN, col[3]))


class HtmlDocument:
    """HtmlDocument class"""
    """An HTML document that allows appending SVG content"""
    TAB: str = "   "

    def __init__(self, file_name: str, win_title: str) -> None:
        self.win_title: str = win_title
        self.__tabs: int = 0
        self.__file: IO = open(file_name, "w")
        self.__write_head()

    def increase_indent(self) -> None:
        """increase_indent method"""
        """Increases the number of tab characters used for indentation"""
        self.__tabs += 1

    def decrease_indent(self) -> None:
        """Decreases the number of tab characters used for indentation"""
        self.__tabs -= 1

    def append(self, content: str) -> None:
        """append method"""
        ts: str = HtmlDocument.TAB * self.__tabs
        self.__file.write(f'{ts}{content}\n')

    def __write_head(self) -> None:
        """Append the HTML preamble to this document"""
        self.append('<html>')
        self.append('<head>')
        self.increase_indent()
        self.append(f'<title>{self.win_title}</title>')
        self.decrease_indent()
        self.append('</head>')
        self.append('<body>')

    def __write_comment(self, comment: str) -> None:
        """Appends an HTML comment to this document"""
        self.append(f'<!--{comment}-->')

    def writeHTMLcomment(f: IO[str], t: int, com: str) -> None:
        """writeHTMLcomment method"""
        ts: str = "   " * t
        f.write(f"{ts}<!--{com}-->\n")

    def writeHTMLline(f: IO[str], t: int, line: str) -> None:
        """writeLineHTML method"""
        ts = "   " * t
        f.write(f"{ts}{line}\n")

    def open_svgscope(self , dimension: Extent) -> None:
        """open_svgscope method"""
        self.__write_comment('Define and paint SVG drawing box')
        self.append(f'<svg width="{dimension.width.imax}" '
                    f'height="{dimension.height.imax}">')

    def writeHTMLHeader(f: IO[str], winTitle: str) -> None:
        """writeHeadHTML method"""
        HtmlDocument.writeHTMLline(f, 0, "<html>")
        HtmlDocument.writeHTMLline(f, 0, "<head>")
        HtmlDocument.writeHTMLline(f, 1, f"<title>{winTitle}</title>")
        HtmlDocument.writeHTMLline(f, 0, "</head>")
        HtmlDocument.writeHTMLline(f, 0, "<body>")


class SvgCanvas:
    """SvgCanvas method"""

    def __init__(self, tlx: int, tly: int, rad: int) -> None:
        self.__tlx: int = tlx
        self.__tly: int = tly
        self.__rad: int = rad

    def openSVGcanvas(f: IO[str], t: int, canvas: tuple) -> None:
        """openSVGcanvas method"""
        ts: str = "   " * t
        HtmlDocument.writeHTMLcomment(f, t, "Define SVG drawing box")
        f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

    def genArt(f: IO[str], t: int, styl) -> None:
        """genART method"""

        for shape_count in range(gen_int(Irange(0,PyArtConfig.SHCNT))):
            rand = Random(styl.SHA, styl.RAD, styl.RWH, styl.COL)
            RandomShape.drawRandomLine(f, t, rand)


    def closeSVGcanvas(f: IO[str], t: int) -> None:
        """closeSVGcanvas method"""
        ts: str = "   " * t
        f.write(f"{ts}</svg>\n")
        f.write(f"</body>\n")
        f.write(f"</html>\n")


class CircleShape:
    """A circle shape representing an SVG circle element"""
    ccnt: int = 0  # counting number of circles being constructed

    @classmethod
    def get_circle_count(cls) -> int:
        """get_circle_count method"""
        return CircleShape.ccnt

    def __init__(self, rs) -> None:
        """Initializes a circle"""
        self.sha: int = 0
        self.ctx: int = rs[1]
        self.cty: int = rs[2]
        self.rad: int = rs[3]
        self.red: int = rs[8]
        self.gre: int = rs[9]
        self.blu: int = rs[10]
        self.op: float = rs[11]

    def as_svg(self) -> str:
        """as_svg method"""
        return f'<circle cx="{self.ctx}" cy"{self.cty}" r="{self.rad}" ' \
               f'fill="rgb({self.red},{self.gre},{self.blu})" ' \
               f'fill-opacity={self.op}"></circle>'

    def __str__(self) -> str:
        """String representation of this shape"""
        return f'\nGenerated random circle\n' \
               f'shape = {self.sha}\n' \
               f'radius = {self.rad}\n' \
               f'(centerx, blue) = ({self.ctx},{self.cty})\n' \
               f'(red, green, blue) = ({self.red},{self.gre},{self.blu})\n' \
               f'opacity = {self.op:,1f}\n'

    def drawCircleLine(f: IO[str], t: int, c: Circle) -> None:
        """drawCircle method"""
        ts: str = "   " * t
        line1: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" '
        line2: str = f'fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
        f.write(f"{ts}{line1+line2}\n")


class RectangleShape:
    """RectangleShape class"""
    ccnt: int = 0  # counting number of circles being constructed

    @classmethod
    def get_rectangle_count(cls) -> int:
        """get_rectangle_count method"""
        return RectangleShape.ccnt

    def __init__(self, rs) -> None:
        """Initializes a rectangle"""
        self.sha: int = 1
        self.x_coord: int = rs[1]
        self.y_coord: int = rs[2]
        self.width: int = rs[6]
        self.height: int = rs[7]
        self.red: int = rs[8]
        self.gre: int = rs[9]
        self.blu: int = rs[10]
        self.op: float = rs[11]

    def __str__(self) -> str:
        """String representation of this shape"""
        return f'\nGenerated random rectangle\n' \
               f'shape = {self.sha}\n' \
               f'x_coordinate = {self.x_coord}\n' \
               f'y_coordinate = {self.y_coord}\n' \
               f'(width, height) = ({self.width},{self.height})\n' \
               f'(red, green, blue) = ({self.red},{self.gre},{self.blu})\n' \
               f'opacity = {self.op:,1f}\n'

    def as_svg(self) -> str:
        """as_svg method"""
        return f'<rect x="{self.x_coord}" y="{self.y_coord}" width="{self.width}" height="{self.height}' \
               f'fill="rgb({self.red},{self.gre},{self.blu})" ' \
               f'fill-opacity={self.op}"></rect>'

    def drawRectangleLine(f: IO[str], t: int, r: Rectangle) -> None:
        """drawRectangle method"""
        ts: str = "   " * t
        line1: str = f'<rect x="{r.x_coord}" y="{r.y_coord}" width="{r.width}" height="{r.height}" '
        line2: str = f'fill="rgb({r.red}, {r.green}, {r.blue})" fill-opacity="{r.op}"></rect>'
        f.write(f"{ts}{line1+line2}\n")


class PyArtConfig:
    """PyArtConfig class"""

    def __init__(self, can: Extent, sha: List[ShapeKind], rad: Irange, rwh: Extent, col: Colour) -> None:
        """Initializes PyArtConfig class"""
        """Initializes a configuration object"""
        self.SHA: List[ShapeKind] = sha
        self.CAN: Extent = can
        self.RAD: Irange = rad
        self.RWH: Extent = rwh
        self.COL: Colour = col

    def __str__(self) -> str:
        """String representation of this configuration"""
        return f'\nUser-defined art configuration\n' \
               f'Shape types = ({", ".join(self.SHA)})\n' \
               f'CAN(CXMIN, CXMAX, CYMIN, CYMAX) = {self.CAN}\n' \
               f'RAD(RADMIN, RADMAX,) = ({self.RAD})\n' \
               f'RWH(WMIN, WMAX, HMIN, HMAX) = {self.RWH}\n' \
               f'COL(REDMIN, REDMAX, GREMIN, GREMAX, BLUMIN, BLUMAX) = {self.COL}\n' \
               f'COL(OPMIN, OPMAX) = ({self.COL.opacity:1f}, {self.COL.opacity:.1f})\n'

    TAB: str = "   "
    FILENAME: str = "SVGArt.html"
    WINART: str = "Python SVG Art"
    H1ART: str = "Python SVG Art"
    cnt: int = 0                                # shape counter
    SHCNT: int = 10000                          # max number of shapes to be generated
    XMIN: int = 0                     # canvas x min
    YMIN: int = 0                               # canvas y min
    XMAX: int = 700                             # canvas x max
    YMAX: int = 500                             # canvas y max
    TITLERGB: tuple[int, int, int] = (100, 100, 255)    # colour of H1 title
    CANVASRGB: tuple[int, int, int] = (255, 150, 255)   # canvas background colour
    CANVASRECT: tuple[int, int, int, int] = (XMIN, YMIN, XMAX-XMIN, YMAX-YMIN)
    CANVASOP: float = 1.0                       # canvas opacity

    BRED: int = 0                               # border colour red value
    BGREEN: int = 0                             # border colour red value
    BBLUE: int = 0                              # border colour red value
    BWIDTH: int = 10                            # border width

    RADMIN: int = 0                             # circle radius min
    RADMAX: int = 50                            # circle radius max
    CRXMIN: int = XMIN + 10                      # circle center x min
    CRXMAX: int = XMAX - 10                      # circle center x max
    CRYMIN: int = YMIN + 10                      # circle center y min
    CRYMAX: int = YMAX - 10                      # circle center y max

    RXMIN: int = 10         # ellipse center x min
    RXMAX: int = 30         # ellipse center x max
    RYMIN: int = 10         # ellipse center y min
    RYMAX: int = 30         # ellipse center y max

    WMIN: int = 10
    WMAX: int = 100
    HMIN: int = 10
    HMAX: int = 100

    REDMIN: int = 0                           # colour red min value
    REDMAX: int = 255                           # colour red max value
    GREENMIN: int = 0                         # colour green min value
    GREENMAX: int = 255                         # colour green max value
    BLUEMIN: int = 0                         # colour blue min value
    BLUEMAX: int = 255                          # colour blue max value
    OPMIN: float = 0.0                          # colour opacity min value
    OPMAX: float = 1.0                          # colour opacity max value


class RandomShape:
    """RandomShape class"""

    def __init__(self, SHA: ShapeKind, RAD: Irange, RWH: Extent, col: Colour):
        self.SHA: int = random.choice(SHA)
        self.X: int = gen_int(Irange(PyArtConfig.XMIN, PyArtConfig.XMAX))
        self.Y: int = gen_int(Irange(PyArtConfig.YMIN, PyArtConfig.YMAX))
        self.RAD: int = gen_int(RAD)
        self.RX: int = gen_int(Irange(PyArtConfig.RXMIN, PyArtConfig.RXMAX))
        self.RY: int = gen_int(Irange(PyArtConfig.RYMIN, PyArtConfig.RYMAX))
        self.W: int = gen_int(RWH[0])
        self.H: int = gen_int(RWH[1])
        self.R: int = gen_int(Irange(PyArtConfig.REDMIN, col[0]))
        self.G: int = gen_int(Irange(PyArtConfig.GREENMIN, col[1]))
        self.B: int = gen_int(Irange(PyArtConfig.BLUEMIN, col[2]))
        self.OP: float = gen_float(Frange(PyArtConfig.OPMIN, col[3]))

    def __str__(self) -> str:
        """Str output of RandomShape"""
        return f'Random_Shape(SHA: {self.SHA}, X: {self.X}, Y: {self.Y}, RAD: {self.RAD}, RX: {self.RX}, \
               RY: {self.RY}, W: {self.W}, H: {self.H}, R: {self.R}, G: {self.G}, B: {self.B}, OP: {self.OP})'

    def as_Part2_line(CNT: int) -> str:
        """as_Part2_line() method"""

        SHA: int = gen_int(Irange(0, 2))
        X: int = gen_int(Irange(PyArtConfig.XMIN, PyArtConfig.XMAX))
        Y: int = gen_int(Irange(PyArtConfig.YMIN, PyArtConfig.YMAX))
        RAD: int = gen_int(Irange(PyArtConfig.RADMIN, PyArtConfig.RADMAX))
        RX: int = gen_int(Irange(PyArtConfig.RXMIN, PyArtConfig.RXMAX))
        RY: int = gen_int(Irange(PyArtConfig.RYMIN, PyArtConfig.RYMAX))
        W: int = gen_int(Irange(PyArtConfig.WMIN, PyArtConfig.WMAX))
        H: int = gen_int(Irange(PyArtConfig.HMIN, PyArtConfig.HMAX))
        R: int = gen_int(Irange(PyArtConfig.REDMIN, PyArtConfig.REDMAX))
        G: int = gen_int(Irange(PyArtConfig.GREENMIN, PyArtConfig.GREENMAX))
        B: int = gen_int(Irange(PyArtConfig.BLUEMIN, PyArtConfig.BLUEMAX))
        OP: float = gen_float(Frange(PyArtConfig.OPMIN, PyArtConfig.OPMAX))

        return f"{CNT:>5} {SHA:>5} {X:>5} {Y:>5} {RAD:>5} {RX:>5} {RY:>5} {W:>5} {H:>5} {R:>5} {G:>5} {B:>5} {OP:>5.1f}"

    def as_svg(self) -> str:
        """as_svg method"""

        if self.SHA == 0:
            return f'<circle cx="{self.X}" cy"{self.Y}" r="{self.RAD}" ' \
                   f'fill="rgb({self.R},{self.G},{self.B})" ' \
                   f'fill-opacity={self.OP}"></circle>'
        else:
            """Produces the SVG code representing this shape"""
            return f'<rect x="{self.X}" y="{self.Y}" width="{self.W}" height="{self.H}' \
                   f'fill="rgb({self.R},{self.G},{self.B})" ' \
                   f'fill-opacity={self.OP}"></rect>'

    def drawRandomLine(f: IO[str], t: int, r: Random) -> None:
        """drawRandom method"""
        ts: str = "   " * t
        if r.SHA == ShapeKind.CIRCLE:
            line1: str = f'<circle cx="{r.X}" cy="{r.Y}" r="{r.RAD}" '
            line2: str = f'fill="rgb({r.R}, {r.G}, {r.B})" fill-opacity="{r.OP}"></circle>'
            f.write(f"{ts}{line1 + line2}\n")
        else:
            line1: str = f'<rect x="{r.X}" y="{r.Y}" width="{r.W}" height="{r.H}" '
            line2: str = f'fill="rgb({r.R}, {r.G}, {r.B})" fill-opacity="{r.OP}"></rect>'
            f.write(f"{ts}{line1 + line2}\n")

def writeHTMLfile(file_name: str, can_width, can_height, styl: PyArtConfig) -> None:
    """writeHTMLfile method"""
    fnam: str = file_name
    winTitle = "My Art"
    f: IO[str] = open(fnam, "w")
    HtmlDocument.writeHTMLHeader(f, winTitle)
    SvgCanvas.openSVGcanvas(f, 1, (can_width, can_height))
    SvgCanvas.genArt(f, 2, styl)
    SvgCanvas.closeSVGcanvas(f, 1)
    f.close()


def make_random_number_table(CNT: int) -> None:
    """make_random_number_table method"""

    header = ("CNT", "SHA", "X", "Y", "RAD", "RX", "RY", "W", "H", "R", "G", "B", "OP")

    print((f"{header[0]:>5} {header[1]:>5} {header[2]:>5} {header[3]:>5} {header[4]:>5} {header[5]:>5} \
{header[6]:>5} {header[7]:>5} {header[8]:>5} {header[9]:>5} {header[10]:>5} {header[11]:>5} {header[12]:>5}"))
    for line in range(CNT):
        print(RandomShape.as_Part2_line(line))


def main() -> None:
    """main method"""
    art_1: PyArtConfig = PyArtConfig(Extent(Irange(0, 700), Irange(0, 500)), [ShapeKind.CIRCLE, ShapeKind.RECTANGLE],
                                     Irange(0, 50), Extent(Irange(10, 100), Irange(10, 100)), Colour(255, 255, 255, 1.0))
    writeHTMLfile("a431.html", gen_int(art_1.CAN[0]), gen_int(art_1.CAN[1]), art_1)

    art_2: PyArtConfig = PyArtConfig(Extent(Irange(0, 500), Irange(0, 700)), [ShapeKind.CIRCLE],
                                     Irange(0, 50), Extent(Irange(10, 100), Irange(0, 20)), Colour(255, 0, 0, 0.1))
    writeHTMLfile("a432.html", gen_int(art_2.CAN[0]), gen_int(art_2.CAN[1]), art_2)

    art_3: PyArtConfig = PyArtConfig(Extent(Irange(0, 800), Irange(0, 700)), [ShapeKind.RECTANGLE],
                                     Irange(0, 50), Extent(Irange(10, 100), Irange(50, 200)), Colour(200, 200, 200, 0.5))
    writeHTMLfile("a433.html", gen_int(art_2.CAN[0]), gen_int(art_2.CAN[1]), art_3)


if __name__ == "__main__":
    main()
