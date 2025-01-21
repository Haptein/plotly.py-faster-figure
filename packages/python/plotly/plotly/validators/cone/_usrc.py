

import _plotly_utils.basevalidators as _bv


class UsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='usrc',
                       parent_name='cone',
                       **kwargs):
        super(UsrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)