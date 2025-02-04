

import _plotly_utils.basevalidators as _bv


class DashValidator(_bv.DashValidator):
    def __init__(self, plotly_name='dash',
                       parent_name='scattergeo.line',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']),
        **kwargs)