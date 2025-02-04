

import _plotly_utils.basevalidators as _bv


class ZValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name='z',
                       parent_name='densitymap',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)