

import _plotly_utils.basevalidators as _bv


class BgcolorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name='bgcolor',
                       parent_name='isosurface.hoverlabel',
                       **kwargs):
        super(BgcolorValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)