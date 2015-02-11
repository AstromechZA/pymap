import math
import logging

log = logging.getLogger(__name__)


def coords_to_tile(lat, lon, zoom):
    lat_rad = math.radians(lat)
    n = 2 ** zoom
    xtile = (lon + 180.0) / 360.0 * n
    ytile = (1.0 - math.log(math.tan(lat_rad) + (1.0 / math.cos(lat_rad))) / math.pi) / 2.0 * n
    log.info("lat: %s, lon: %s => x: %s, y: %s", lat, lon, xtile, ytile)
    return (xtile, ytile)

def gen_tile_indices(x_center, y_center, cov_width, cov_height):
    left = int(math.floor(x_center) - math.ceil(cov_width / 512.0 - (x_center % 1)))
    right = int(math.floor(x_center) + math.ceil(cov_width / 512.0 + (x_center % 1)))
    top = int(math.floor(y_center) - math.ceil(cov_height / 512.0 - (y_center % 1)))
    bottom = int(math.floor(y_center) + math.ceil(cov_height / 512.0 + (y_center % 1)))
    return tuple([tuple([(x, y) for x in xrange(left, right)]) for y in xrange(top, bottom)])
