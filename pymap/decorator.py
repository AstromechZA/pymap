import logging

from wand.drawing import Drawing
from wand.color import Color

log = logging.getLogger(__name__)

GRID_COLOUR = 'rgba(0, 0, 0, 0.6)'

STUB_FRACTION = 40
PIP_FRACTION = 80

def add_grid(image, grid_size):
    width = image.width
    height = image.height
    wd = width / grid_size
    hd = height / grid_size

    log.debug("Draw grid of size %s on image.", grid_size)

    with Drawing() as draw:
        with Color(GRID_COLOUR) as color:
            draw.fill_color = color
            for i in xrange(0, grid_size):
                draw.line((wd * i, 0), (wd * i, height))
                draw.line((0, hd * i), (width, hd * i))
            draw.line((width-1, 0), (width-1, height))
            draw.line((0, height-1), (width, height-1))

            draw.line((width / 2, 0), (width / 2, height / STUB_FRACTION))
            draw.line((width / 2 + 1, 0), (width / 2 + 1, height / STUB_FRACTION))
            draw.line((width / 2, height - height / STUB_FRACTION), (width / 2, height))
            draw.line((width / 2 + 1, height - height / STUB_FRACTION), (width / 2 + 1, height))

            draw.line((0, height / 2), (width / STUB_FRACTION, height / 2))
            draw.line((0, height / 2 + 1), (width / STUB_FRACTION, height / 2 + 1))
            draw.line((width - width / STUB_FRACTION, height / 2), (width, height / 2))
            draw.line((width - width / STUB_FRACTION, height / 2 + 1), (width, height / 2 + 1))


            draw.line((width / 2 - width / PIP_FRACTION, height / 2), (width / 2 + width / PIP_FRACTION, height / 2))
            draw.line((width / 2, height / 2 - height / PIP_FRACTION), (width / 2, height / 2 + height / PIP_FRACTION))

            draw(image)
