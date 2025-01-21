from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Title(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "pie"
    _path_str = "pie.title"
    _valid_props = {"font", "position", "text"}

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font used for `title`.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.pie.title.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

        Returns
        -------
        plotly.graph_objs.pie.title.Font
        """
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    # position
    # --------
    @property
    def position(self):
        """
        Specifies the location of the `title`.

        The 'position' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top left', 'top center', 'top right', 'middle center',
                'bottom left', 'bottom center', 'bottom right']

        Returns
        -------
        Any
        """
        return self["position"]

    @position.setter
    def position(self, val):
        self["position"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the title of the chart. If it is empty, no title is
        displayed.

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
            Sets the font used for `title`.
        position
            Specifies the location of the `title`.
        text
            Sets the title of the chart. If it is empty, no title
            is displayed.
        """

    def __init__(self, arg=None, font=None, position=None, text=None, **kwargs):
        """
        Construct a new Title object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.pie.Title`
        font
            Sets the font used for `title`.
        position
            Specifies the location of the `title`.
        text
            Sets the title of the chart. If it is empty, no title
            is displayed.

        Returns
        -------
        Title
        """
        super(Title, self).__init__("title")

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
The first argument to the plotly.graph_objs.pie.Title
constructor must be a dict or
an instance of :class:`plotly.graph_objs.pie.Title`"""
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
        _v = arg.pop("position", None)
        _v = position if position is not None else _v
        if _v is not None:
            self["position"] = _v
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
