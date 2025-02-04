

import _plotly_utils.basevalidators as _bv


class DashValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='dash',
                       parent_name='scatter3d.line',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['dash', 'dashdot', 'dot', 'longdash', 'longdashdot', 'solid']),
        **kwargs)