import logging
import urllib2
from wand.image import Image

from .coord_helper import gen_tile_indices, coords_to_tile

TILE_URL = "http://otile1.mqcdn.com/tiles/1.0.0/map/{zoom}/{x}/{y}.jpg"

log = logging.getLogger(__name__)


def stitch_map_tiles(grid, zoom):
    full_image_width  = len(grid[0])
    full_image_height = len(grid)
    total, count = full_image_width * full_image_height, 1

    full_image = Image(width=full_image_width*256, height=full_image_height*256, format='png')
    for y, grid_row in enumerate(grid):
        for x, cell in enumerate(grid_row):
            url = TILE_URL.format(zoom=zoom, x=cell[0], y=cell[1])
            log.debug('Getting image %s/%s: (%s)..', count, total, url)
            tile_image = Image(file=urllib2.urlopen(url))
            log.debug('Compositing into full image.')
            full_image.composite(image=tile_image, left=x*256, top=y*256)
            tile_image.destroy()
            count += 1

    return full_image


def create_tile_map(x_tile_center, y_tile_center, image_width, image_height, zoom):
    grid = gen_tile_indices(x_tile_center, y_tile_center, image_width, image_height)
    log.debug('\n' + '\n'.join([str(r) for r in grid]))
    full_image = stitch_map_tiles(grid, zoom)

    x_offset = int(((x_tile_center % 1)) * 256 - (image_width / 2.0) % 256)
    y_offset = int(((y_tile_center % 1)) * 256 - (image_height / 2.0) % 256)

    log.info("Cropping to %s,%s w=%s h=%s", x_offset, y_offset, image_width, image_height)
    full_image.crop(x_offset, y_offset, width=image_width, height=image_height)

    return full_image


def create_map(latitude, longitude, zoom, image_width, image_height):
    x_tile_center, y_tile_center = coords_to_tile(latitude, longitude, zoom)
    map_image = create_tile_map(x_tile_center, y_tile_center, image_width, image_height, zoom)
    return map_image
