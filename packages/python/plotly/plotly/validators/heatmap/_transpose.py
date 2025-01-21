

import _plotly_utils.basevalidators as _bv


class TransposeValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='transpose',
                       parent_name='heatmap',
                       **kwargs):
        super(TransposeValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)