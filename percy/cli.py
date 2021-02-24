import click
from .version import __version__
from .percy import create_percy


@click.group()
@click.version_option(version=__version__)
def cli():
    """
    Image Downloader for Percy, the Mars Rover
    """


@cli.command()
@click.option('-r', '--resolution',
              help="Parameter for left column",
              nargs=1,
              type=str,
              required=True)
@click.option('-p', '--path',
              default="./perseverance",
              help="Parameter for left column",
              nargs=1,
              required=True)
@click.option('-n', '--number',
              default=0,
              help="Page Number from which images are to be downloaded",
              type=int,
              nargs=1)
def download(resolution, path, number):
    percy = create_percy(resolution=resolution,
                         basepath=path,
                         page_num=number)
    percy.download()
