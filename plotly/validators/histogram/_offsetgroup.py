

import _plotly_utils.basevalidators as _bv


class OffsetgroupValidator(_bv.StringValidator):
    def __init__(self, plotly_name='offsetgroup',
                       parent_name='histogram',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)