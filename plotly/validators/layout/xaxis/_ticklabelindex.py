

import _plotly_utils.basevalidators as _bv


class TicklabelindexValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name='ticklabelindex',
                       parent_name='layout.xaxis',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)