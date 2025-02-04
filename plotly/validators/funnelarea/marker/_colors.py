

import _plotly_utils.basevalidators as _bv


class ColorsValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name='colors',
                       parent_name='funnelarea.marker',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)