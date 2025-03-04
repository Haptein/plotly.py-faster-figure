import os
import json
from pathlib import Path
import importlib.metadata as importlib_metadata
from packaging.version import Version
import tempfile

import plotly
from plotly.io._utils import validate_coerce_fig_to_dict

try:
    import kaleido

    kaleido_available = True
    kaleido_major = Version(importlib_metadata.version("kaleido")).major

    if kaleido_major < 1:
        # Kaleido v0
        from kaleido.scopes.plotly import PlotlyScope

        scope = PlotlyScope()
        # Compute absolute path to the 'plotly/package_data/' directory
        root_dir = os.path.dirname(os.path.abspath(plotly.__file__))
        package_dir = os.path.join(root_dir, "package_data")
        scope.plotlyjs = os.path.join(package_dir, "plotly.min.js")
        if scope.mathjax is None:
            scope.mathjax = (
                "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js"
            )
except ImportError as e:
    kaleido_available = False
    kaleido_major = -1
    PlotlyScope = None
    scope = None


def to_image(
    fig, format=None, width=None, height=None, scale=None, validate=True, engine=None
):
    """
    Convert a figure to a static image bytes string

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure

    format: str or None
        The desired image format. One of
            - 'png'
            - 'jpg' or 'jpeg'
            - 'webp'
            - 'svg'
            - 'pdf'
            - 'eps' (Requires the poppler library to be installed and on the PATH)

        If not specified, will default to `plotly.io.kaleido.scope.default_format`

    width: int or None
        The width of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the width of the exported image
        in physical pixels.

        If not specified, will default to `plotly.io.kaleido.scope.default_width`

    height: int or None
        The height of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the height of the exported image
        in physical pixels.

        If not specified, will default to `plotly.io.kaleido.scope.default_height`

    scale: int or float or None
        The scale factor to use when exporting the figure. A scale factor
        larger than 1.0 will increase the image resolution with respect
        to the figure's layout pixel dimensions. Whereas as scale factor of
        less than 1.0 will decrease the image resolution.

        If not specified, will default to `plotly.io.kaleido.scope.default_scale`

    validate: bool
        True if the figure should be validated before being converted to
        an image, False otherwise.

    engine (deprecated): str
        No longer used. Kaleido is the only supported engine.

    Returns
    -------
    bytes
        The image data
    """

    # Raise informative error message if Kaleido is not installed
    if not kaleido_available:
        raise ValueError(
            """
Image export using the "kaleido" engine requires the kaleido package,
which can be installed using pip:
    $ pip install -U kaleido
"""
        )

    # Convert figure to dict (and validate if requested)
    fig_dict = validate_coerce_fig_to_dict(fig, validate)

    # Request image bytes
    if kaleido_major > 0:
        # Kaleido v1
        opts = {
            k: v
            for k, v in dict(
                format=format,
                width=width,
                height=height,
                scale=scale,
            ).items()
            if v is not None
        }
        img_bytes = kaleido.calc_fig_sync(
            fig_dict,
            path=None,
            opts=opts,
        )
    else:
        # Kaleido v0
        img_bytes = scope.transform(
            fig_dict, format=format, width=width, height=height, scale=scale
        )

    return img_bytes


def write_image(
    fig,
    file,
    format=None,
    scale=None,
    width=None,
    height=None,
    validate=True,
    engine="auto",
):
    """
    Convert a figure to a static image and write it to a file or writeable
    object

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure

    file: str or writeable
        A string representing a local file path or a writeable object
        (e.g. a pathlib.Path object or an open file descriptor)

    format: str or None
        The desired image format. One of
          - 'png'
          - 'jpg' or 'jpeg'
          - 'webp'
          - 'svg'
          - 'pdf'
          - 'eps' (Requires the poppler library to be installed and on the PATH)

        If not specified and `file` is a string then this will default to the
        file extension. If not specified and `file` is not a string then this
        will default to:
            - `plotly.io.kaleido.scope.default_format` if engine is "kaleido"
            - `plotly.io.orca.config.default_format` if engine is "orca"

    width: int or None
        The width of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the width of the exported image
        in physical pixels.

        If not specified, will default to`plotly.io.kaleido.scope.default_width`

    height: int or None
        The height of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the height of the exported image
        in physical pixels.

        If not specified, will default to `plotly.io.kaleido.scope.default_height`

    scale: int or float or None
        The scale factor to use when exporting the figure. A scale factor
        larger than 1.0 will increase the image resolution with respect
        to the figure's layout pixel dimensions. Whereas as scale factor of
        less than 1.0 will decrease the image resolution.

        If not specified, will default to `plotly.io.kaleido.scope.default_scale`

    validate: bool
        True if the figure should be validated before being converted to
        an image, False otherwise.

    engine (deprecated): str
        No longer used. Kaleido is the only supported engine.

    Returns
    -------
    None
    """
    # Try to cast `file` as a pathlib object `path`.
    # ----------------------------------------------
    if isinstance(file, str):
        # Use the standard Path constructor to make a pathlib object.
        path = Path(file)
    elif isinstance(file, Path):
        # `file` is already a Path object.
        path = file
    else:
        # We could not make a Path object out of file. Either `file` is an open file
        # descriptor with a `write()` method or it's an invalid object.
        path = None

    # Infer format if not specified
    # -----------------------------
    if path is not None and format is None:
        ext = path.suffix
        if ext:
            format = ext.lstrip(".")
        else:
            raise ValueError(
                """
Cannot infer image type from output path '{file}'.
Please add a file extension or specify the type using the format parameter.
For example:

    >>> import plotly.io as pio
    >>> pio.write_image(fig, file_path, format='png')
""".format(
                    file=file
                )
            )

    # Request image
    # -------------
    # Do this first so we don't create a file if image conversion fails
    img_data = to_image(
        fig,
        format=format,
        scale=scale,
        width=width,
        height=height,
        validate=validate,
        engine=engine,
    )

    # Open file
    # ---------
    if path is None:
        # We previously failed to make sense of `file` as a pathlib object.
        # Attempt to write to `file` as an open file descriptor.
        try:
            file.write(img_data)
            return
        except AttributeError:
            pass
        raise ValueError(
            """
The 'file' argument '{file}' is not a string, pathlib.Path object, or file descriptor.
""".format(
                file=file
            )
        )
    else:
        # We previously succeeded in interpreting `file` as a pathlib object.
        # Now we can use `write_bytes()`.
        path.write_bytes(img_data)


def full_figure_for_development(fig, warn=True, as_dict=False):
    """
    Compute default values for all attributes not specified in the input figure and
    returns the output as a "full" figure. This function calls Plotly.js via Kaleido
    to populate unspecified attributes. This function is intended for interactive use
    during development to learn more about how Plotly.js computes default values and is
    not generally necessary or recommended for production use.

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure

    warn: bool
        If False, suppress warnings about not using this in production.

    as_dict: bool
        If True, output is a dict with some keys that go.Figure can't parse.
        If False, output is a go.Figure with unparseable keys skipped.

    Returns
    -------
    plotly.graph_objects.Figure or dict
        The full figure
    """

    # Raise informative error message if Kaleido is not installed
    if not kaleido_available:
        raise ValueError(
            """
Full figure generation requires the kaleido package,
which can be installed using pip:
    $ pip install -U kaleido
"""
        )

    if warn:
        import warnings

        warnings.warn(
            "full_figure_for_development is not recommended or necessary for "
            "production use in most circumstances. \n"
            "To suppress this warning, set warn=False"
        )

    if kaleido_major > 0:
        # Kaleido v1
        try:
            json_file = Path(tempfile.mkstemp(suffix=".json")[1])
            kaleido.write_fig_sync(
                fig,
                json_file,
                dict(format="json"),
            )
            with open(json_file, "r") as f:
                fig = json.load(f)
        finally:
            # Cleanup: remove temp file
            json_file.unlink()
    else:
        # Kaleido v0
        fig = json.loads(scope.transform(fig, format="json").decode("utf-8"))

    if as_dict:
        return fig
    else:
        import plotly.graph_objects as go

        return go.Figure(fig, skip_invalid=True)


__all__ = ["to_image", "write_image", "scope", "full_figure_for_development"]
