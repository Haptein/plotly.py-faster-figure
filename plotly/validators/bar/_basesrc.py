

import _plotly_utils.basevalidators as _bv


class BasesrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='basesrc',
                       parent_name='bar',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)