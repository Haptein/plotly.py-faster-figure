

import _plotly_utils.basevalidators as _bv


class GriddashValidator(_bv.DashValidator):
    def __init__(self, plotly_name='griddash',
                       parent_name='layout.polar.radialaxis',
                       **kwargs):
        super(GriddashValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']),
        **kwargs)