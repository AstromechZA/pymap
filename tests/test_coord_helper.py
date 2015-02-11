
from pymap import coord_helper

def test_gen_tile_indices():
    # centered in single tile
    assert coord_helper.gen_tile_indices(1.5, 2.5, 256, 256) == (((1, 2),),)

    # centered on corner
    assert coord_helper.gen_tile_indices(6, 10, 400, 400) == (
        ((5, 9 ), (6, 9 )),
        ((5, 10), (6, 10))
    )

    # centered and overlapping area
    assert coord_helper.gen_tile_indices(6.5, 7.5, 400, 400) == (
        ((5, 6), (6, 6), (7, 6)),
        ((5, 7), (6, 7), (7, 7)),
        ((5, 8), (6, 8), (7, 8))
    )

    # centered and overlapping area
    assert coord_helper.gen_tile_indices(6.1, 7.9, 400, 800) == (
        ((5, 6), (6, 6)),
        ((5, 7), (6, 7)),
        ((5, 8), (6, 8)),
        ((5, 9), (6, 9)),
    )
