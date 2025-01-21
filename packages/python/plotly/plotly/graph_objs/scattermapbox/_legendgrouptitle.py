from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Legendgrouptitle(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "scattermapbox"
    _path_str = "scattermapbox.legendgrouptitle"
    _valid_props = {"font", "text"}

    # font
    # ----
    @property
    def font(self):
        """
        Sets this legend group's title font.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scattermapbox.legendgrouptitle.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

        Returns
        -------
        plotly.graph_objs.scattermapbox.legendgrouptitle.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the title of the legend group.

        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        font
            Sets this legend group's title font.
        text
            Sets the title of the legend group.
        """

    def __init__(self, arg=None, font=None, text=None, **kwargs):
        """
        Construct a new Legendgrouptitle object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.scattermapbox.
            Legendgrouptitle`
        font
            Sets this legend group's title font.
        text
            Sets the title of the legend group.

        Returns
        -------
        Legendgrouptitle
        """
        super(Legendgrouptitle, self).__init__("legendgrouptitle")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
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
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.scattermapbox.Legendgrouptitle
constructor must be a dict or
an instance of :class:`plotly.graph_objs.scattermapbox.Legendgrouptitle`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
