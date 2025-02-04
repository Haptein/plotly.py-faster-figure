

import _plotly_utils.basevalidators as _bv


class DxValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='dx',
                       parent_name='funnel',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)