

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Ternary(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'layout'
    _path_str = 'layout.ternary'
    _valid_props = {"aaxis", "baxis", "bgcolor", "caxis", "domain", "sum", "uirevision"}

    # aaxis
    # -----
    @property
    def aaxis(self):
        """
        The 'aaxis' property is an instance of Aaxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.ternary.Aaxis`
          - A dict of string/value properties that will be passed
            to the Aaxis constructor

        Returns
        -------
        plotly.graph_objs.layout.ternary.Aaxis
        """
        return self['aaxis']

    @aaxis.setter
    def aaxis(self, val):
        self['aaxis'] = val

    # baxis
    # -----
    @property
    def baxis(self):
        """
        The 'baxis' property is an instance of Baxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.ternary.Baxis`
          - A dict of string/value properties that will be passed
            to the Baxis constructor

        Returns
        -------
        plotly.graph_objs.layout.ternary.Baxis
        """
        return self['baxis']

    @baxis.setter
    def baxis(self, val):
        self['baxis'] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Set the background color of the subplot

        The 'bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['bgcolor']

    @bgcolor.setter
    def bgcolor(self, val):
        self['bgcolor'] = val

    # caxis
    # -----
    @property
    def caxis(self):
        """
        The 'caxis' property is an instance of Caxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.ternary.Caxis`
          - A dict of string/value properties that will be passed
            to the Caxis constructor

        Returns
        -------
        plotly.graph_objs.layout.ternary.Caxis
        """
        return self['caxis']

    @caxis.setter
    def caxis(self, val):
        self['caxis'] = val

    # domain
    # ------
    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.ternary.Domain`
          - A dict of string/value properties that will be passed
            to the Domain constructor

        Returns
        -------
        plotly.graph_objs.layout.ternary.Domain
        """
        return self['domain']

    @domain.setter
    def domain(self, val):
        self['domain'] = val

    # sum
    # ---
    @property
    def sum(self):
        """
        The number each triplet should sum to, and the maximum range of
        each axis

        The 'sum' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['sum']

    @sum.setter
    def sum(self, val):
        self['sum'] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in axis `min` and
        `title`, if not overridden in the individual axes. Defaults to
        `layout.uirevision`.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['uirevision']

    @uirevision.setter
    def uirevision(self, val):
        self['uirevision'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        aaxis
            :class:`plotly.graph_objects.layout.ternary.Aaxis`
            instance or dict with compatible properties
        baxis
            :class:`plotly.graph_objects.layout.ternary.Baxis`
            instance or dict with compatible properties
        bgcolor
            Set the background color of the subplot
        caxis
            :class:`plotly.graph_objects.layout.ternary.Caxis`
            instance or dict with compatible properties
        domain
            :class:`plotly.graph_objects.layout.ternary.Domain`
            instance or dict with compatible properties
        sum
            The number each triplet should sum to, and the maximum
            range of each axis
        uirevision
            Controls persistence of user-driven changes in axis
            `min` and `title`, if not overridden in the individual
            axes. Defaults to `layout.uirevision`.
        """
    def __init__(self,
            arg=None,
            aaxis=None,
            baxis=None,
            bgcolor=None,
            caxis=None,
            domain=None,
            sum=None,
            uirevision=None,
            **kwargs
        ):
        """
        Construct a new Ternary object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.Ternary`
        aaxis
            :class:`plotly.graph_objects.layout.ternary.Aaxis`
            instance or dict with compatible properties
        baxis
            :class:`plotly.graph_objects.layout.ternary.Baxis`
            instance or dict with compatible properties
        bgcolor
            Set the background color of the subplot
        caxis
            :class:`plotly.graph_objects.layout.ternary.Caxis`
            instance or dict with compatible properties
        domain
            :class:`plotly.graph_objects.layout.ternary.Domain`
            instance or dict with compatible properties
        sum
            The number each triplet should sum to, and the maximum
            range of each axis
        uirevision
            Controls persistence of user-driven changes in axis
            `min` and `title`, if not overridden in the individual
            axes. Defaults to `layout.uirevision`.

        Returns
        -------
        Ternary
        """
        super(Ternary, self).__init__('ternary')

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
The first argument to the plotly.graph_objs.layout.Ternary
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Ternary`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('aaxis', arg, aaxis)
        self._init_provided('baxis', arg, baxis)
        self._init_provided('bgcolor', arg, bgcolor)
        self._init_provided('caxis', arg, caxis)
        self._init_provided('domain', arg, domain)
        self._init_provided('sum', arg, sum)
        self._init_provided('uirevision', arg, uirevision)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
