

from __future__ import annotations
from typing import Any
from numpy.typing import NDArray
from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Slider(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = 'layout'
    _path_str = 'layout.slider'
    _valid_props = {"active", "activebgcolor", "bgcolor", "bordercolor", "borderwidth", "currentvalue", "font", "len", "lenmode", "minorticklen", "name", "pad", "stepdefaults", "steps", "templateitemname", "tickcolor", "ticklen", "tickwidth", "transition", "visible", "x", "xanchor", "y", "yanchor"}

    # active
    # ------
    @property
    def active(self):
        """
        Determines which button (by index starting from 0) is
        considered active.

        The 'active' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['active']

    @active.setter
    def active(self, val):
        self['active'] = val

    # activebgcolor
    # -------------
    @property
    def activebgcolor(self):
        """
        Sets the background color of the slider grip while dragging.

        The 'activebgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['activebgcolor']

    @activebgcolor.setter
    def activebgcolor(self, val):
        self['activebgcolor'] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the slider.

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
        Sets the color of the border enclosing the slider.

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
        Sets the width (in px) of the border enclosing the slider.

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

    # currentvalue
    # ------------
    @property
    def currentvalue(self):
        """
        The 'currentvalue' property is an instance of Currentvalue
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.Currentvalue`
          - A dict of string/value properties that will be passed
            to the Currentvalue constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.Currentvalue
        """
        return self['currentvalue']

    @currentvalue.setter
    def currentvalue(self, val):
        self['currentvalue'] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the font of the slider step labels.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # len
    # ---
    @property
    def len(self):
        """
        Sets the length of the slider This measure excludes the padding
        of both ends. That is, the slider's length is this length minus
        the padding on both ends.

        The 'len' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['len']

    @len.setter
    def len(self, val):
        self['len'] = val

    # lenmode
    # -------
    @property
    def lenmode(self):
        """
        Determines whether this slider length is set in units of plot
        "fraction" or in *pixels. Use `len` to set the value.

        The 'lenmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fraction', 'pixels']

        Returns
        -------
        Any
        """
        return self['lenmode']

    @lenmode.setter
    def lenmode(self, val):
        self['lenmode'] = val

    # minorticklen
    # ------------
    @property
    def minorticklen(self):
        """
        Sets the length in pixels of minor step tick marks

        The 'minorticklen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['minorticklen']

    @minorticklen.setter
    def minorticklen(self, val):
        self['minorticklen'] = val

    # name
    # ----
    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.

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

    # pad
    # ---
    @property
    def pad(self):
        """
        Set the padding of the slider component along each side.

        The 'pad' property is an instance of Pad
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.Pad`
          - A dict of string/value properties that will be passed
            to the Pad constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.Pad
        """
        return self['pad']

    @pad.setter
    def pad(self, val):
        self['pad'] = val

    # steps
    # -----
    @property
    def steps(self):
        """
        The 'steps' property is a tuple of instances of
        Step that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.slider.Step
          - A list or tuple of dicts of string/value properties that
            will be passed to the Step constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.slider.Step]
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
        layout.template.layout.slider.stepdefaults), sets the default
        property values to use for elements of layout.slider.steps

        The 'stepdefaults' property is an instance of Step
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.Step`
          - A dict of string/value properties that will be passed
            to the Step constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.Step
        """
        return self['stepdefaults']

    @stepdefaults.setter
    def stepdefaults(self, val):
        self['stepdefaults'] = val

    # templateitemname
    # ----------------
    @property
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.

        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['templateitemname']

    @templateitemname.setter
    def templateitemname(self, val):
        self['templateitemname'] = val

    # tickcolor
    # ---------
    @property
    def tickcolor(self):
        """
        Sets the color of the border enclosing the slider.

        The 'tickcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color

        Returns
        -------
        str
        """
        return self['tickcolor']

    @tickcolor.setter
    def tickcolor(self, val):
        self['tickcolor'] = val

    # ticklen
    # -------
    @property
    def ticklen(self):
        """
        Sets the length in pixels of step tick marks

        The 'ticklen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['ticklen']

    @ticklen.setter
    def ticklen(self, val):
        self['ticklen'] = val

    # tickwidth
    # ---------
    @property
    def tickwidth(self):
        """
        Sets the tick width (in px).

        The 'tickwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['tickwidth']

    @tickwidth.setter
    def tickwidth(self, val):
        self['tickwidth'] = val

    # transition
    # ----------
    @property
    def transition(self):
        """
        The 'transition' property is an instance of Transition
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.Transition`
          - A dict of string/value properties that will be passed
            to the Transition constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.Transition
        """
        return self['transition']

    @transition.setter
    def transition(self, val):
        self['transition'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not the slider is visible.

        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the x position (in normalized coordinates) of the slider.

        The 'x' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets the slider's horizontal position anchor. This anchor binds
        the `x` position to the "left", "center" or "right" of the
        range selector.

        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self['xanchor']

    @xanchor.setter
    def xanchor(self, val):
        self['xanchor'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the y position (in normalized coordinates) of the slider.

        The 'y' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets the slider's vertical position anchor This anchor binds
        the `y` position to the "top", "middle" or "bottom" of the
        range selector.

        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self['yanchor']

    @yanchor.setter
    def yanchor(self, val):
        self['yanchor'] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        active
            Determines which button (by index starting from 0) is
            considered active.
        activebgcolor
            Sets the background color of the slider grip while
            dragging.
        bgcolor
            Sets the background color of the slider.
        bordercolor
            Sets the color of the border enclosing the slider.
        borderwidth
            Sets the width (in px) of the border enclosing the
            slider.
        currentvalue
            :class:`plotly.graph_objects.layout.slider.Currentvalue
            ` instance or dict with compatible properties
        font
            Sets the font of the slider step labels.
        len
            Sets the length of the slider This measure excludes the
            padding of both ends. That is, the slider's length is
            this length minus the padding on both ends.
        lenmode
            Determines whether this slider length is set in units
            of plot "fraction" or in *pixels. Use `len` to set the
            value.
        minorticklen
            Sets the length in pixels of minor step tick marks
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        pad
            Set the padding of the slider component along each
            side.
        steps
            A tuple of
            :class:`plotly.graph_objects.layout.slider.Step`
            instances or dicts with compatible properties
        stepdefaults
            When used in a template (as
            layout.template.layout.slider.stepdefaults), sets the
            default property values to use for elements of
            layout.slider.steps
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        tickcolor
            Sets the color of the border enclosing the slider.
        ticklen
            Sets the length in pixels of step tick marks
        tickwidth
            Sets the tick width (in px).
        transition
            :class:`plotly.graph_objects.layout.slider.Transition`
            instance or dict with compatible properties
        visible
            Determines whether or not the slider is visible.
        x
            Sets the x position (in normalized coordinates) of the
            slider.
        xanchor
            Sets the slider's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            slider.
        yanchor
            Sets the slider's vertical position anchor This anchor
            binds the `y` position to the "top", "middle" or
            "bottom" of the range selector.
        """
    def __init__(self,
            arg=None,
            active: int|float|None = None,
            activebgcolor: str|None = None,
            bgcolor: str|None = None,
            bordercolor: str|None = None,
            borderwidth: int|float|None = None,
            currentvalue: None|None = None,
            font: None|None = None,
            len: int|float|None = None,
            lenmode: Any|None = None,
            minorticklen: int|float|None = None,
            name: str|None = None,
            pad: None|None = None,
            steps: None|None = None,
            stepdefaults: None|None = None,
            templateitemname: str|None = None,
            tickcolor: str|None = None,
            ticklen: int|float|None = None,
            tickwidth: int|float|None = None,
            transition: None|None = None,
            visible: bool|None = None,
            x: int|float|None = None,
            xanchor: Any|None = None,
            y: int|float|None = None,
            yanchor: Any|None = None,
            **kwargs
        ):
        """
        Construct a new Slider object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Slider`
        active
            Determines which button (by index starting from 0) is
            considered active.
        activebgcolor
            Sets the background color of the slider grip while
            dragging.
        bgcolor
            Sets the background color of the slider.
        bordercolor
            Sets the color of the border enclosing the slider.
        borderwidth
            Sets the width (in px) of the border enclosing the
            slider.
        currentvalue
            :class:`plotly.graph_objects.layout.slider.Currentvalue
            ` instance or dict with compatible properties
        font
            Sets the font of the slider step labels.
        len
            Sets the length of the slider This measure excludes the
            padding of both ends. That is, the slider's length is
            this length minus the padding on both ends.
        lenmode
            Determines whether this slider length is set in units
            of plot "fraction" or in *pixels. Use `len` to set the
            value.
        minorticklen
            Sets the length in pixels of minor step tick marks
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        pad
            Set the padding of the slider component along each
            side.
        steps
            A tuple of
            :class:`plotly.graph_objects.layout.slider.Step`
            instances or dicts with compatible properties
        stepdefaults
            When used in a template (as
            layout.template.layout.slider.stepdefaults), sets the
            default property values to use for elements of
            layout.slider.steps
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        tickcolor
            Sets the color of the border enclosing the slider.
        ticklen
            Sets the length in pixels of step tick marks
        tickwidth
            Sets the tick width (in px).
        transition
            :class:`plotly.graph_objects.layout.slider.Transition`
            instance or dict with compatible properties
        visible
            Determines whether or not the slider is visible.
        x
            Sets the x position (in normalized coordinates) of the
            slider.
        xanchor
            Sets the slider's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            slider.
        yanchor
            Sets the slider's vertical position anchor This anchor
            binds the `y` position to the "top", "middle" or
            "bottom" of the range selector.

        Returns
        -------
        Slider
        """
        super().__init__('sliders')
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
The first argument to the plotly.graph_objs.layout.Slider
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Slider`""")

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop('skip_invalid', False)
        self._validate = kwargs.pop('_validate', True)
        

        # Populate data dict with properties
        # ----------------------------------
        self._init_provided('active', arg, active)
        self._init_provided('activebgcolor', arg, activebgcolor)
        self._init_provided('bgcolor', arg, bgcolor)
        self._init_provided('bordercolor', arg, bordercolor)
        self._init_provided('borderwidth', arg, borderwidth)
        self._init_provided('currentvalue', arg, currentvalue)
        self._init_provided('font', arg, font)
        self._init_provided('len', arg, len)
        self._init_provided('lenmode', arg, lenmode)
        self._init_provided('minorticklen', arg, minorticklen)
        self._init_provided('name', arg, name)
        self._init_provided('pad', arg, pad)
        self._init_provided('steps', arg, steps)
        self._init_provided('stepdefaults', arg, stepdefaults)
        self._init_provided('templateitemname', arg, templateitemname)
        self._init_provided('tickcolor', arg, tickcolor)
        self._init_provided('ticklen', arg, ticklen)
        self._init_provided('tickwidth', arg, tickwidth)
        self._init_provided('transition', arg, transition)
        self._init_provided('visible', arg, visible)
        self._init_provided('x', arg, x)
        self._init_provided('xanchor', arg, xanchor)
        self._init_provided('y', arg, y)
        self._init_provided('yanchor', arg, yanchor)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
