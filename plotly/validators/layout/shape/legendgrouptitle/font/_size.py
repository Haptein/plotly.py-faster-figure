

import _plotly_utils.basevalidators as _bv


class SizeValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='size',
                       parent_name='layout.shape.legendgrouptitle.font',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc+arraydraw'),
                 min=kwargs.pop('min', 1),
        **kwargs)