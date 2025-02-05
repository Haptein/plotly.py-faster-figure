

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Autorangeoptions(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'layout.scene.zaxis'
    _path_str = 'layout.scene.zaxis.autorangeoptions'
    _valid_props = {"clipmax", "clipmin", "include", "includesrc", "maxallowed", "minallowed"}

    # clipmax
    # -------
    @property
    def clipmax(self):
        """
        Clip autorange maximum if it goes beyond this value. Has no
        effect when `autorangeoptions.maxallowed` is provided.

        The 'clipmax' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['clipmax']

    @clipmax.setter
    def clipmax(self, val):
        self['clipmax'] = val

    # clipmin
    # -------
    @property
    def clipmin(self):
        """
        Clip autorange minimum if it goes beyond this value. Has no
        effect when `autorangeoptions.minallowed` is provided.

        The 'clipmin' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['clipmin']

    @clipmin.setter
    def clipmin(self, val):
        self['clipmin'] = val

    # include
    # -------
    @property
    def include(self):
        """
        Ensure this value is included in autorange.

        The 'include' property accepts values of any type

        Returns
        -------
        Any|NDArray
        """
        return self['include']

    @include.setter
    def include(self, val):
        self['include'] = val

    # includesrc
    # ----------
    @property
    def includesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `include`.

        The 'includesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['includesrc']

    @includesrc.setter
    def includesrc(self, val):
        self['includesrc'] = val

    # maxallowed
    # ----------
    @property
    def maxallowed(self):
        """
        Use this value exactly as autorange maximum.

        The 'maxallowed' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['maxallowed']

    @maxallowed.setter
    def maxallowed(self, val):
        self['maxallowed'] = val

    # minallowed
    # ----------
    @property
    def minallowed(self):
        """
        Use this value exactly as autorange minimum.

        The 'minallowed' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['minallowed']

    @minallowed.setter
    def minallowed(self, val):
        self['minallowed'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        clipmax
            Clip autorange maximum if it goes beyond this value.
            Has no effect when `autorangeoptions.maxallowed` is
            provided.
        clipmin
            Clip autorange minimum if it goes beyond this value.
            Has no effect when `autorangeoptions.minallowed` is
            provided.
        include
            Ensure this value is included in autorange.
        includesrc
            Sets the source reference on Chart Studio Cloud for
            `include`.
        maxallowed
            Use this value exactly as autorange maximum.
        minallowed
            Use this value exactly as autorange minimum.
        """
    def __init__(self,
            arg=None,
            clipmax: Any|None = None,
            clipmin: Any|None = None,
            include: Any|None = None,
            includesrc: str|None = None,
            maxallowed: Any|None = None,
            minallowed: Any|None = None,
            **kwargs
        ):
        """
        Construct a new Autorangeoptions object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.scene.z
            axis.Autorangeoptions`
        clipmax
            Clip autorange maximum if it goes beyond this value.
            Has no effect when `autorangeoptions.maxallowed` is
            provided.
        clipmin
            Clip autorange minimum if it goes beyond this value.
            Has no effect when `autorangeoptions.minallowed` is
            provided.
        include
            Ensure this value is included in autorange.
        includesrc
            Sets the source reference on Chart Studio Cloud for
            `include`.
        maxallowed
            Use this value exactly as autorange maximum.
        minallowed
            Use this value exactly as autorange minimum.

        Returns
        -------
        Autorangeoptions
        """
        super().__init__('autorangeoptions')
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
The first argument to the plotly.graph_objs.layout.scene.zaxis.Autorangeoptions
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.scene.zaxis.Autorangeoptions`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('clipmax', arg, clipmax)
        self._init_provided('clipmin', arg, clipmin)
        self._init_provided('include', arg, include)
        self._init_provided('includesrc', arg, includesrc)
        self._init_provided('maxallowed', arg, maxallowed)
        self._init_provided('minallowed', arg, minallowed)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
