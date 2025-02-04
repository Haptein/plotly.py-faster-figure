

import _plotly_utils.basevalidators as _bv


class RoughnessValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='roughness',
                       parent_name='mesh3d.lighting',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 max=kwargs.pop('max', 1),
                 min=kwargs.pop('min', 0),
        **kwargs)