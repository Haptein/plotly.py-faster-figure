

import _plotly_utils.basevalidators as _bv


class BaseratioValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='baseratio',
                       parent_name='funnelarea',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 max=kwargs.pop('max', 1),
                 min=kwargs.pop('min', 0),
        **kwargs)