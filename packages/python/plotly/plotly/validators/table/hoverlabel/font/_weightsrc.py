

import _plotly_utils.basevalidators as _bv


class WeightsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='weightsrc',
                       parent_name='table.hoverlabel.font',
                       **kwargs):
        super(WeightsrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)