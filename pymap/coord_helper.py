import math
import io
import urllib2
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

TILE_URL = "http://otile1.mqcdn.com/tiles/1.0.0/map/{zoom}/{x}/{y}.jpg"


def coords_to_tile(lat, lon, zoom=10):
    lat_rad = math.radians(lat)
    n = 2 ** zoom
    xtile = (lon + 180.0) / 360.0 * n
    ytile = (1.0 - math.log(math.tan(lat_rad) + (1.0 / math.cos(lat_rad))) / math.pi) / 2.0 * n
    return (xtile, ytile)

def get_tile_indices(x_center, y_center, cov_width, cov_height):
    left = int(math.floor(x_center) - math.ceil(cov_width / 512.0 - (x_center % 1)))
    right = int(math.floor(x_center) + math.ceil(cov_width / 512.0 + (x_center % 1)))
    top = int(math.floor(y_center) - math.ceil(cov_height / 512.0 - (y_center % 1)))
    bottom = int(math.floor(y_center) + math.ceil(cov_height / 512.0 + (y_center % 1)))

    grid = list()
    for y in xrange(top, bottom):
        row = list()
        for x in xrange(left, right):
            row.append((x, y))
        grid.append(tuple(row))
    return tuple(grid)


def main():
    zoom = 14
    image_width = 777
    image_height = 400
    xtile, ytile = coords_to_tile(40.689167, -74.044444, zoom=zoom)
    grid_indices = get_tile_indices(xtile, ytile, image_width, image_height)

    tile_grid_width = len(grid_indices) * 256
    tile_grid_height = len(grid_indices[0]) * 256

    x_offset = int((xtile % 1) * 256) + int((256 - (image_width / 2.0) % 256))
    y_offset = int((ytile % 1) * 256) + int((256 - (image_height / 2.0) % 256))

    with Image(width=image_width, height=image_height) as final_image:
        total = len(grid_indices) * len(grid_indices[0])
        count = 0
        for x, grid_row in enumerate(grid_indices):
            for y, cell in enumerate(grid_row):
                count += 1
                url = TILE_URL.format(zoom=zoom, x=cell[0], y=cell[1])
                print 'Getting image {}/{}: ({})..'.format(count, total, url)
                tile_image = Image(file=urllib2.urlopen(url))
                print '  Compositing..'
                final_image.composite(image=tile_image, left=x*256-x_offset, top=y*256-y_offset)
                print '  Done.'
        final_image.format = 'png'
        final_image.save(filename='destination.png')

if __name__ == '__main__':
    main()
