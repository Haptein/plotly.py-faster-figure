

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Gauge(_BaseTraceHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'indicator'
    _path_str = 'indicator.gauge'
    _valid_props = {"axis", "bar", "bgcolor", "bordercolor", "borderwidth", "shape", "stepdefaults", "steps", "threshold"}

    # axis
    # ----
    @property
    def axis(self):
        """
        The 'axis' property is an instance of Axis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.gauge.Axis`
          - A dict of string/value properties that will be passed
            to the Axis constructor

        Returns
        -------
        plotly.graph_objs.indicator.gauge.Axis
        """
        return self['axis']

    @axis.setter
    def axis(self, val):
        self['axis'] = val

    # bar
    # ---
    @property
    def bar(self):
        """
        Set the appearance of the gauge's value

        The 'bar' property is an instance of Bar
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.gauge.Bar`
          - A dict of string/value properties that will be passed
            to the Bar constructor

        Returns
        -------
        plotly.graph_objs.indicator.gauge.Bar
        """
        return self['bar']

    @bar.setter
    def bar(self, val):
        self['bar'] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the gauge background color.

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

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the color of the border enclosing the gauge.

        The 'bordercolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['bordercolor']

    @bordercolor.setter
    def bordercolor(self, val):
        self['bordercolor'] = val

    # borderwidth
    # -----------
    @property
    def borderwidth(self):
        """
        Sets the width (in px) of the border enclosing the gauge.

        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['borderwidth']

    @borderwidth.setter
    def borderwidth(self, val):
        self['borderwidth'] = val

    # shape
    # -----
    @property
    def shape(self):
        """
        Set the shape of the gauge

        The 'shape' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['angular', 'bullet']

        Returns
        -------
        Any
        """
        return self['shape']

    @shape.setter
    def shape(self, val):
        self['shape'] = val

    # steps
    # -----
    @property
    def steps(self):
        """
        The 'steps' property is a tuple of instances of
        Step that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.indicator.gauge.Step
          - A list or tuple of dicts of string/value properties that
            will be passed to the Step constructor

        Returns
        -------
        tuple[plotly.graph_objs.indicator.gauge.Step]
        """
        return self['steps']

    @steps.setter
    def steps(self, val):
        self['steps'] = val

    # stepdefaults
    # ------------
    @property
    def stepdefaults(self):
        """
        When used in a template (as
        layout.template.data.indicator.gauge.stepdefaults), sets the
        default property values to use for elements of
        indicator.gauge.steps

        The 'stepdefaults' property is an instance of Step
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.gauge.Step`
          - A dict of string/value properties that will be passed
            to the Step constructor

        Returns
        -------
        plotly.graph_objs.indicator.gauge.Step
        """
        return self['stepdefaults']

    @stepdefaults.setter
    def stepdefaults(self, val):
        self['stepdefaults'] = val

    # threshold
    # ---------
    @property
    def threshold(self):
        """
        The 'threshold' property is an instance of Threshold
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.indicator.gauge.Threshold`
          - A dict of string/value properties that will be passed
            to the Threshold constructor

        Returns
        -------
        plotly.graph_objs.indicator.gauge.Threshold
        """
        return self['threshold']

    @threshold.setter
    def threshold(self, val):
        self['threshold'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        axis
            :class:`plotly.graph_objects.indicator.gauge.Axis`
            instance or dict with compatible properties
        bar
            Set the appearance of the gauge's value
        bgcolor
            Sets the gauge background color.
        bordercolor
            Sets the color of the border enclosing the gauge.
        borderwidth
            Sets the width (in px) of the border enclosing the
            gauge.
        shape
            Set the shape of the gauge
        steps
            A tuple of
            :class:`plotly.graph_objects.indicator.gauge.Step`
            instances or dicts with compatible properties
        stepdefaults
            When used in a template (as
            layout.template.data.indicator.gauge.stepdefaults),
            sets the default property values to use for elements of
            indicator.gauge.steps
        threshold
            :class:`plotly.graph_objects.indicator.gauge.Threshold`
            instance or dict with compatible properties
        """
    def __init__(self,
            arg=None,
            axis=None,
            bar=None,
            bgcolor=None,
            bordercolor=None,
            borderwidth=None,
            shape=None,
            steps=None,
            stepdefaults=None,
            threshold=None,
            **kwargs
        ):
        """
        Construct a new Gauge object

        The gauge of the Indicator plot.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.indicator.Gauge`
        axis
            :class:`plotly.graph_objects.indicator.gauge.Axis`
            instance or dict with compatible properties
        bar
            Set the appearance of the gauge's value
        bgcolor
            Sets the gauge background color.
        bordercolor
            Sets the color of the border enclosing the gauge.
        borderwidth
            Sets the width (in px) of the border enclosing the
            gauge.
        shape
            Set the shape of the gauge
        steps
            A tuple of
            :class:`plotly.graph_objects.indicator.gauge.Step`
            instances or dicts with compatible properties
        stepdefaults
            When used in a template (as
            layout.template.data.indicator.gauge.stepdefaults),
            sets the default property values to use for elements of
            indicator.gauge.steps
        threshold
            :class:`plotly.graph_objects.indicator.gauge.Threshold`
            instance or dict with compatible properties

        Returns
        -------
        Gauge
        """
        super().__init__('gauge')
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
The first argument to the plotly.graph_objs.indicator.Gauge
constructor must be a dict or
an instance of :class:`plotly.graph_objs.indicator.Gauge`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('axis', arg, axis)
        self._init_provided('bar', arg, bar)
        self._init_provided('bgcolor', arg, bgcolor)
        self._init_provided('bordercolor', arg, bordercolor)
        self._init_provided('borderwidth', arg, borderwidth)
        self._init_provided('shape', arg, shape)
        self._init_provided('steps', arg, steps)
        self._init_provided('stepdefaults', arg, stepdefaults)
        self._init_provided('threshold', arg, threshold)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
