import logging

from wand.drawing import Drawing
from wand.color import Color

log = logging.getLogger(__name__)

GRID_COLOUR = 'rgba(0, 0, 0, 0.6)'

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
            draw(image)
