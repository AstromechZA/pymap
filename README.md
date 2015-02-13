pymap
=====

    usage: pymap [--help] [-z ZOOM] [-w WIDTH] [-h HEIGHT] [-g GRID]
                 [-t {watercolor,light,dark,mq,toner,osm}] [-d]
                 latitude longitude output_path

    Generates a png map of the given geographic area.

    positional arguments:
      latitude              The vertical or north-south coordinate of the image
                            center.
      longitude             The horizantal or east-west coordinate of the image
                            center.
      output_path           The output path of the image as a jpg or png.

    optional arguments:
      --help                show this help message and exit
      -z ZOOM, --zoom ZOOM  The zoom level of the image (0-16).
      -w WIDTH, --width WIDTH
                            The width and horizantal span of the map image in
                            pixels.
      -h HEIGHT, --height HEIGHT
                            The height and vertical span of the map image in
                            pixels.
      -g GRID, --grid GRID  Draw a grid with the given size over the image.
      -t {watercolor,light,dark,mq,toner,osm}, --tileset {watercolor,light,dark,mq,toner,osm}
                            Pick a tile set provider.
      -d, --debug           Print debugging text.

Samples
-------

- sample1.png
    - `pymap -28.6150483 23.9310862 --zoom 6 sample1.png --width 1024 --height 1024 --tileset light`
- sample2.png
    - `pymap -34.052805 18.5524338 --zoom 10 sample2.png --tileset watercolor`
- sample3.png
    - `pymap -26.2074685 28.0430648 --zoom 16 sample3.png --tileset dark`
