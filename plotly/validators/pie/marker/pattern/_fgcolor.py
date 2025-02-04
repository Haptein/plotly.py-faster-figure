

import _plotly_utils.basevalidators as _bv


class FgcolorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name='fgcolor',
                       parent_name='pie.marker.pattern',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'style'),
        **kwargs)