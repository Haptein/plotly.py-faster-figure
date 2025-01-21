

import _plotly_utils.basevalidators as _bv


class HovertemplateValidator(_bv.StringValidator):
    def __init__(self, plotly_name='hovertemplate',
                       parent_name='mesh3d',
                       **kwargs):
        super(HovertemplateValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)