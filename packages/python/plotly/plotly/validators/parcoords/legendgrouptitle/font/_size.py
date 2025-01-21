

import _plotly_utils.basevalidators as _bv


class SizeValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='size',
                       parent_name='parcoords.legendgrouptitle.font',
                       **kwargs):
        super(SizeValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'style'),
                 min=kwargs.pop('min', 1),
        **kwargs)