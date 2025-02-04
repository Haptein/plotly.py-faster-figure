

import _plotly_utils.basevalidators as _bv


class X0ShiftValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='x0shift',
                       parent_name='layout.shape',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 max=kwargs.pop('max', 1),
                 min=kwargs.pop('min', -1),
        **kwargs)