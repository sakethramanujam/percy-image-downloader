# :arrow_down: percy-image-downloader
Unofficial image downloader for Nasa Perseverance Raw Images [website](https://mars.nasa.gov/mars2020/multimedia/raw-images/)
Image credits: NASA/JPL-Caltech unless otherwise noted.

## :stars: Updates in v0.2
- The downloader has basic tests setup.
- Fixes a bug with respect to page number specification.
- Image Format issues for `full` scale images are now resolved.

## Installation
> Requires python>=3.6

Download the zip and execute the following in your terminal

```bash
python setup.py install
```

## Usage Instructions

Currently supports downloading images of chosen resolution type from a specific page, defaults to `0`th page.

```
percy [OPTIONS] COMMAND [ARGS]...

  Image Downloader for Percy, the Mars Rover

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  download
```

### Downloading Images

```
percy download [OPTIONS]

Options:
  -r, --resolution TEXT  Parameter for left column  [required]
  -p, --path TEXT        Parameter for left column  [required]
  -n, --number INTEGER   Page Number from which images are to be downloaded,
                         defaults to 0

  --help                 Show this message and exit.
```

### Supported Resolution Tags

| Keyword  | Resolution as per NASA Website |
| :------: | :----------------------------: |
|  `full`  |        Full Size Image         |
| `large`  |       Large Scale Image        |
| `medium` |       Medium Scale Image       |
| `small`  |     Small/Thumbnail Image      |


#### Example

```bash
percy download -r large -p ./ -n 1
```

Found an bug/need a feature? 
- Report/Request, raise an issue [here](https://github.com/sakethramanujam/percy-image-downloader/issues/new)