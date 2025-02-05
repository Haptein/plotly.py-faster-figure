

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Tickfont(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'volume.colorbar'
    _path_str = 'volume.colorbar.tickfont'
    _valid_props = {"color", "family", "lineposition", "shadow", "size", "style", "textcase", "variant", "weight"}

    # color
    # -----
    @property
    def color(self):
        """
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # family
    # ------
    @property
    def family(self):
        """
        HTML font family - the typeface that will be applied by the web
        browser. The web browser can only apply a font if it is
        available on the system where it runs. Provide multiple font
        families, separated by commas, to indicate the order in which
        to apply fonts if they aren't available.

        The 'family' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self['family']

    @family.setter
    def family(self, val):
        self['family'] = val

    # lineposition
    # ------------
    @property
    def lineposition(self):
        """
        Sets the kind of decoration line(s) with text, such as an
        "under", "over" or "through" as well as combinations e.g.
        "under+over", etc.

        The 'lineposition' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['under', 'over', 'through'] joined with '+' characters
            (e.g. 'under+over')
            OR exactly one of ['none'] (e.g. 'none')

        Returns
        -------
        Any
        """
        return self['lineposition']

    @lineposition.setter
    def lineposition(self, val):
        self['lineposition'] = val

    # shadow
    # ------
    @property
    def shadow(self):
        """
        Sets the shape and color of the shadow behind text. "auto"
        places minimal shadow and applies contrast text font color. See
        https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow
        for additional options.

        The 'shadow' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['shadow']

    @shadow.setter
    def shadow(self, val):
        self['shadow'] = val

    # size
    # ----
    @property
    def size(self):
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

    # style
    # -----
    @property
    def style(self):
        """
        Sets whether a font should be styled with a normal or italic
        face from its family.

        The 'style' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'italic']

        Returns
        -------
        Any
        """
        return self['style']

    @style.setter
    def style(self, val):
        self['style'] = val

    # textcase
    # --------
    @property
    def textcase(self):
        """
        Sets capitalization of text. It can be used to make text appear
        in all-uppercase or all-lowercase, or with each word
        capitalized.

        The 'textcase' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'word caps', 'upper', 'lower']

        Returns
        -------
        Any
        """
        return self['textcase']

    @textcase.setter
    def textcase(self, val):
        self['textcase'] = val

    # variant
    # -------
    @property
    def variant(self):
        """
        Sets the variant of the font.

        The 'variant' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'small-caps', 'all-small-caps',
                'all-petite-caps', 'petite-caps', 'unicase']

        Returns
        -------
        Any
        """
        return self['variant']

    @variant.setter
    def variant(self, val):
        self['variant'] = val

    # weight
    # ------
    @property
    def weight(self):
        """
        Sets the weight (or boldness) of the font.

        The 'weight' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [1, 1000]
            OR exactly one of ['normal', 'bold'] (e.g. 'bold')

        Returns
        -------
        int
        """
        return self['weight']

    @weight.setter
    def weight(self, val):
        self['weight'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser can only apply a font
            if it is available on the system where it runs. Provide
            multiple font families, separated by commas, to
            indicate the order in which to apply fonts if they
            aren't available.
        lineposition
            Sets the kind of decoration line(s) with text, such as
            an "under", "over" or "through" as well as combinations
            e.g. "under+over", etc.
        shadow
            Sets the shape and color of the shadow behind text.
            "auto" places minimal shadow and applies contrast text
            font color. See https://developer.mozilla.org/en-
            US/docs/Web/CSS/text-shadow for additional options.
        size

        style
            Sets whether a font should be styled with a normal or
            italic face from its family.
        textcase
            Sets capitalization of text. It can be used to make
            text appear in all-uppercase or all-lowercase, or with
            each word capitalized.
        variant
            Sets the variant of the font.
        weight
            Sets the weight (or boldness) of the font.
        """
    def __init__(self,
            arg=None,
            color: str|None = None,
            family: str|None = None,
            lineposition: Any|None = None,
            shadow: str|None = None,
            size: int|float|None = None,
            style: Any|None = None,
            textcase: Any|None = None,
            variant: Any|None = None,
            weight: int|None = None,
            **kwargs
        ):
        """
        Construct a new Tickfont object

        Sets the color bar's tick label font

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.volume.colorbar.Tickfont`
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser can only apply a font
            if it is available on the system where it runs. Provide
            multiple font families, separated by commas, to
            indicate the order in which to apply fonts if they
            aren't available.
        lineposition
            Sets the kind of decoration line(s) with text, such as
            an "under", "over" or "through" as well as combinations
            e.g. "under+over", etc.
        shadow
            Sets the shape and color of the shadow behind text.
            "auto" places minimal shadow and applies contrast text
            font color. See https://developer.mozilla.org/en-
            US/docs/Web/CSS/text-shadow for additional options.
        size

        style
            Sets whether a font should be styled with a normal or
            italic face from its family.
        textcase
            Sets capitalization of text. It can be used to make
            text appear in all-uppercase or all-lowercase, or with
            each word capitalized.
        variant
            Sets the variant of the font.
        weight
            Sets the weight (or boldness) of the font.

        Returns
        -------
        Tickfont
        """
        super().__init__('tickfont')
        if '_parent' in kwargs:
            self._parent = kwargs['_parent']
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError("""\
The first argument to the plotly.graph_objs.volume.colorbar.Tickfont
constructor must be a dict or
an instance of :class:`plotly.graph_objs.volume.colorbar.Tickfont`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('color', arg, color)
        self._init_provided('family', arg, family)
        self._init_provided('lineposition', arg, lineposition)
        self._init_provided('shadow', arg, shadow)
        self._init_provided('size', arg, size)
        self._init_provided('style', arg, style)
        self._init_provided('textcase', arg, textcase)
        self._init_provided('variant', arg, variant)
        self._init_provided('weight', arg, weight)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
