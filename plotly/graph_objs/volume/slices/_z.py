

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Z(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'volume.slices'
    _path_str = 'volume.slices.z'
    _valid_props = {"fill", "locations", "locationssrc", "show"}

    # fill
    # ----
    @property
    def fill(self):
        """
        Sets the fill ratio of the `slices`. The default fill value of
        the `slices` is 1 meaning that they are entirely shaded. On the
        other hand Applying a `fill` ratio less than one would allow
        the creation of openings parallel to the edges.

        The 'fill' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['fill']

    @fill.setter
    def fill(self, val):
        self['fill'] = val

    # locations
    # ---------
    @property
    def locations(self):
        """
        Specifies the location(s) of slices on the axis. When not
        specified slices would be created for all points of the axis z
        except start and end.

        The 'locations' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        NDArray
        """
        return self['locations']

    @locations.setter
    def locations(self, val):
        self['locations'] = val

    # locationssrc
    # ------------
    @property
    def locationssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `locations`.

        The 'locationssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['locationssrc']

    @locationssrc.setter
    def locationssrc(self, val):
        self['locationssrc'] = val

    # show
    # ----
    @property
    def show(self):
        """
        Determines whether or not slice planes about the z dimension
        are drawn.

        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['show']

    @show.setter
    def show(self, val):
        self['show'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fill
            Sets the fill ratio of the `slices`. The default fill
            value of the `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.
        locations
            Specifies the location(s) of slices on the axis. When
            not specified slices would be created for all points of
            the axis z except start and end.
        locationssrc
            Sets the source reference on Chart Studio Cloud for
            `locations`.
        show
            Determines whether or not slice planes about the z
            dimension are drawn.
        """
    def __init__(self,
            arg=None,
            fill: int|float|None = None,
            locations: NDArray|None = None,
            locationssrc: str|None = None,
            show: bool|None = None,
            **kwargs
        ):
        """
        Construct a new Z object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.volume.slices.Z`
        fill
            Sets the fill ratio of the `slices`. The default fill
            value of the `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.
        locations
            Specifies the location(s) of slices on the axis. When
            not specified slices would be created for all points of
            the axis z except start and end.
        locationssrc
            Sets the source reference on Chart Studio Cloud for
            `locations`.
        show
            Determines whether or not slice planes about the z
            dimension are drawn.

        Returns
        -------
        Z
        """
        super().__init__('z')
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
The first argument to the plotly.graph_objs.volume.slices.Z
constructor must be a dict or
an instance of :class:`plotly.graph_objs.volume.slices.Z`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('fill', arg, fill)
        self._init_provided('locations', arg, locations)
        self._init_provided('locationssrc', arg, locationssrc)
        self._init_provided('show', arg, show)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
