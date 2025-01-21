

import _plotly_utils.basevalidators as _bv


class GridwidthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='gridwidth',
                       parent_name='layout.yaxis.minor',
                       **kwargs):
        super(GridwidthValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'ticks'),
                 min=kwargs.pop('min', 0),
        **kwargs)