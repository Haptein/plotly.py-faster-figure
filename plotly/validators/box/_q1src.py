

import _plotly_utils.basevalidators as _bv


class Q1SrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='q1src',
                       parent_name='box',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)