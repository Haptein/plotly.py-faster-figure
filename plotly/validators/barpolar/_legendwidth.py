

import _plotly_utils.basevalidators as _bv


class LegendwidthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='legendwidth',
                       parent_name='barpolar',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'style'),
                 min=kwargs.pop('min', 0),
        **kwargs)