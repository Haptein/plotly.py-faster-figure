

import _plotly_utils.basevalidators as _bv


class ZsmoothValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='zsmooth',
                       parent_name='histogram2d',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['fast', 'best', False]),
        **kwargs)