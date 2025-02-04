

import _plotly_utils.basevalidators as _bv


class FillValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='fill',
                       parent_name='scatterternary',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['none', 'toself', 'tonext']),
        **kwargs)