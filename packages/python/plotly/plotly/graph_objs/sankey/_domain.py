

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Domain(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'sankey'
    _path_str = 'sankey.domain'
    _valid_props = {"column", "row", "x", "y"}

    # column
    # ------
    @property
    def column(self):
        """
        If there is a layout grid, use the domain for this column in
        the grid for this sankey trace .

        The 'column' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['column']

    @column.setter
    def column(self, val):
        self['column'] = val

    # row
    # ---
    @property
    def row(self):
        """
        If there is a layout grid, use the domain for this row in the
        grid for this sankey trace .

        The 'row' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['row']

    @row.setter
    def row(self, val):
        self['row'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the horizontal domain of this sankey trace (in plot
        fraction).

        The 'x' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'x[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'x[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the vertical domain of this sankey trace (in plot
        fraction).

        The 'y' property is an info array that may be specified as:
    
        * a list or tuple of 2 elements where:
    (0) The 'y[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'y[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        column
            If there is a layout grid, use the domain for this
            column in the grid for this sankey trace .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this sankey trace .
        x
            Sets the horizontal domain of this sankey trace (in
            plot fraction).
        y
            Sets the vertical domain of this sankey trace (in plot
            fraction).
        """
    def __init__(self,
            arg=None,
            column=None,
            row=None,
            x=None,
            y=None,
            **kwargs
        ):
        """
        Construct a new Domain object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.sankey.Domain`
        column
            If there is a layout grid, use the domain for this
            column in the grid for this sankey trace .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this sankey trace .
        x
            Sets the horizontal domain of this sankey trace (in
            plot fraction).
        y
            Sets the vertical domain of this sankey trace (in plot
            fraction).

        Returns
        -------
        Domain
        """
        super(Domain, self).__init__('domain')

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
The first argument to the plotly.graph_objs.sankey.Domain
constructor must be a dict or
an instance of :class:`plotly.graph_objs.sankey.Domain`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('column', arg, column)
        self._init_provided('row', arg, row)
        self._init_provided('x', arg, x)
        self._init_provided('y', arg, y)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
