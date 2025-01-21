

import _plotly_utils.basevalidators as _bv


class LatsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='latsrc',
                       parent_name='scattermap',
                       **kwargs):
        super(LatsrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)