

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseFrameHierarchyType as _BaseFrameHierarchyType
import copy as _copy


class Frame(_BaseFrameHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = ''
    _path_str = 'frame'
    _valid_props = {"baseframe", "data", "group", "layout", "name", "traces"}

    # baseframe
    # ---------
    @property
    def baseframe(self):
        """
        The name of the frame into which this frame's properties are
        merged before applying. This is used to unify properties and
        avoid needing to specify the same values for the same
        properties in multiple frames.

        The 'baseframe' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['baseframe']

    @baseframe.setter
    def baseframe(self, val):
        self['baseframe'] = val

    # data
    # ----
    @property
    def data(self):
        """
        A list of traces this frame modifies. The format is identical
        to the normal trace definition.

        Returns
        -------
        Any
        """
        return self['data']

    @data.setter
    def data(self, val):
        self['data'] = val

    # group
    # -----
    @property
    def group(self):
        """
        An identifier that specifies the group to which the frame
        belongs, used by animate to select a subset of frames.

        The 'group' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['group']

    @group.setter
    def group(self, val):
        self['group'] = val

    # layout
    # ------
    @property
    def layout(self):
        """
        Layout properties which this frame modifies. The format is
        identical to the normal layout definition.

        Returns
        -------
        Any
        """
        return self['layout']

    @layout.setter
    def layout(self, val):
        self['layout'] = val

    # name
    # ----
    @property
    def name(self):
        """
        A label by which to identify the frame

        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

    # traces
    # ------
    @property
    def traces(self):
        """
        A list of trace indices that identify the respective traces in
        the data attribute

        The 'traces' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['traces']

    @traces.setter
    def traces(self, val):
        self['traces'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        baseframe
            The name of the frame into which this frame's
            properties are merged before applying. This is used to
            unify properties and avoid needing to specify the same
            values for the same properties in multiple frames.
        data
            A list of traces this frame modifies. The format is
            identical to the normal trace definition.
        group
            An identifier that specifies the group to which the
            frame belongs, used by animate to select a subset of
            frames.
        layout
            Layout properties which this frame modifies. The format
            is identical to the normal layout definition.
        name
            A label by which to identify the frame
        traces
            A list of trace indices that identify the respective
            traces in the data attribute
        """
    def __init__(self,
            arg=None,
            baseframe: str|None = None,
            data: Any|None = None,
            group: str|None = None,
            layout: Any|None = None,
            name: str|None = None,
            traces: Any|None = None,
            **kwargs
        ):
        """
        Construct a new Frame object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Frame`
        baseframe
            The name of the frame into which this frame's
            properties are merged before applying. This is used to
            unify properties and avoid needing to specify the same
            values for the same properties in multiple frames.
        data
            A list of traces this frame modifies. The format is
            identical to the normal trace definition.
        group
            An identifier that specifies the group to which the
            frame belongs, used by animate to select a subset of
            frames.
        layout
            Layout properties which this frame modifies. The format
            is identical to the normal layout definition.
        name
            A label by which to identify the frame
        traces
            A list of trace indices that identify the respective
            traces in the data attribute

        Returns
        -------
        Frame
        """
        super().__init__('frames')
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
The first argument to the plotly.graph_objs.Frame
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Frame`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('baseframe', arg, baseframe)
        self._init_provided('data', arg, data)
        self._init_provided('group', arg, group)
        self._init_provided('layout', arg, layout)
        self._init_provided('name', arg, name)
        self._init_provided('traces', arg, traces)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
