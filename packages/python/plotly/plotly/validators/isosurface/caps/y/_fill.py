

import _plotly_utils.basevalidators as _bv


class FillValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='fill',
                       parent_name='isosurface.caps.y',
                       **kwargs):
        super(FillValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 max=kwargs.pop('max', 1),
                 min=kwargs.pop('min', 0),
        **kwargs)