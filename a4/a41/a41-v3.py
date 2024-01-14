#!/usr/bin/env python
"""Assignment 4 Part 1 Version 2 template"""
print(__doc__)

from typing import IO
from typing import NamedTuple
from enum import Enum


class Colour(NamedTuple):
    """Stores the colours stats"""
    red: int
    green: int
    blue: int
    opacity: float


class Irange(NamedTuple):
    """Range with the min and max colour values"""
    imin: int
    imax: int

    def __str__(self) -> str:
        return f'{self.imin},{self.imax}'


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


class RectangleCoordinates(NamedTuple):
    """Stores the coordinates of the rectangle"""
    x_coordinate: int
    y_coordinate: int
    width: int
    height: int


class ShapeKind(str, Enum):
    """Supported shape kinds"""
    CIRCLE = 0
    RECTANGLE = 1


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


class HtmlDocument:
    """HtmlDocument class"""

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
        """decrease_indent method"""
        """Decreases the number of tab characters used for indentation"""
        self.__tabs -= 1

    def append(self, content: str) -> None:
        """append method"""
        """Appends the given HTML content to this document"""
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

    def writeHTMLHeader(f: IO[str], winTitle: str) -> None:
        """writeHeadHTML method"""
        HtmlDocument.writeHTMLline(f, 0, "<html>")
        HtmlDocument.writeHTMLline(f, 0, "<head>")
        HtmlDocument.writeHTMLline(f, 1, f"<title>{winTitle}</title>")
        HtmlDocument.writeHTMLline(f, 0, "</head>")
        HtmlDocument.writeHTMLline(f, 0, "<body>")


class SvgCanvas:
    """SvgCanvas class"""
    def __init__(self, tlx: int, tly: int, rad: int) -> None:
        """Initializes a SvgCanvas"""
        self.__tlx: int = tlx
        self.__tly: int = tly
        self.__rad: int = rad

    def openSVGcanvas(f: IO[str], t: int, canvas: tuple) -> None:
        """openSVGcanvas method"""
        ts: str = "   " * t
        HtmlDocument.writeHTMLcomment(f, t, "Define SVG drawing box")
        f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

    def genArt(f: IO[str], t: int) -> None:
        """genART method"""
        CircleShape.drawCircleLine(f, t, Circle(CircleCoordinates(50, 50, 50), Colour(255, 0, 0, 1.0)))
        CircleShape.drawCircleLine(f, t, Circle(CircleCoordinates(150, 50, 50), Colour(255, 0, 0, 1.0)))
        CircleShape.drawCircleLine(f, t, Circle(CircleCoordinates(250, 50, 50), Colour(255, 0, 0, 1.0)))
        CircleShape.drawCircleLine(f, t, Circle(CircleCoordinates(350, 50, 50), Colour(255, 0, 0, 1.0)))
        CircleShape.drawCircleLine(f, t, Circle(CircleCoordinates(450, 50, 50), Colour(255, 0, 0, 1.0)))
        CircleShape.drawCircleLine(f, t, Circle(CircleCoordinates(50, 250, 50), Colour(0, 0, 255, 1.0)))
        CircleShape.drawCircleLine(f, t, Circle(CircleCoordinates(150, 250, 50), Colour(0, 0, 255, 1.0)))
        CircleShape.drawCircleLine(f, t, Circle(CircleCoordinates(250, 250, 50), Colour(0, 0, 255, 1.0)))
        CircleShape.drawCircleLine(f, t, Circle(CircleCoordinates(350, 250, 50), Colour(0, 0, 255, 1.0)))
        CircleShape.drawCircleLine(f, t, Circle(CircleCoordinates(450, 250, 50), Colour(0, 0, 255, 1.0)))

    def closeSVGcanvas(f: IO[str], t: int) -> None:
        """closeSVGcanvas method"""
        ts: str = "   " * t
        f.write(f"{ts}</svg>\n")
        f.write(f"</body>\n")
        f.write(f"</html>\n")


class CircleShape:
    """CircleShape class"""
    """A circle shape representing an SVG circle element"""
    ccnt: int = 0  # counting number of circles being constructed

    @classmethod
    def get_circle_count(cls) -> int:
        """get_circle_count method"""
        return CircleShape.ccnt

    def __init__(self, cir: CircleCoordinates, col: Colour) -> None:
        """Initializes a circle"""
        self.sha: int = 0
        self.ctx: int = cir[0]
        self.cty: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.gre: int = col[1]
        self.blu: int = col[2]
        self.op: float = col[3]

    def as_svg(self) -> str:
        """as_svg method"""
        """Produces the SVG code representing this shape"""
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
    """A rectangle shape representing an SVG circle element"""
    ccnt: int = 0  # counting number of circles being constructed

    @classmethod
    def get_rectangle_count(cls) -> int:
        """get_rectangle_count method"""
        return RectangleShape.ccnt

    def __init__(self, rect: RectangleCoordinates, col: Colour) -> None:
        """Initializes a rectangle"""
        self.sha: int = 1
        self.x_coord: int = rect[0]
        self.y_coord: int = rect[1]
        self.width: int = rect[2]
        self.height: int = rect[3]
        self.red: int = col[0]
        self.gre: int = col[1]
        self.blu: int = col[2]
        self.op: float = col[3]

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
        """Produces the SVG code representing this shape"""
        return f'<rect x="{self.x_coord}" y="{self.y_coord}" width="{self.width}" height="{self.height}' \
               f'fill="rgb({self.red},{self.gre},{self.blu})" ' \
               f'fill-opacity={self.op}"></circle>'

    def drawRectangleLine(f: IO[str], t: int, r: Rectangle) -> None:
        """drawRectangle method"""
        ts: str = "   " * t
        line1: str = f'x="{r.x_coord}" y="{r.y_coord}" width="{r.width}" height="{r.height}" '
        line2: str = f'fill="rgb({r.red}, {r.green}, {r.blue})" fill-opacity="{r.op}"></rectangle>'
        f.write(f"{ts}{line1+line2}\n")
        

def writeHTMLfile() -> None:
    """writeHTMLfile method"""
    fnam: str = "a41.html"
    winTitle = "My Art"
    f: IO[str] = open(fnam, "w")
    HtmlDocument.writeHTMLHeader(f, winTitle)
    SvgCanvas.openSVGcanvas(f, 1, (500, 300))
    SvgCanvas.genArt(f, 2)
    SvgCanvas.closeSVGcanvas(f, 1)
    f.close()


def main() -> None:
    """main method"""
    writeHTMLfile()


if __name__ == "__main__":
    main()
