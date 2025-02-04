

import _plotly_utils.basevalidators as _bv


class TicktextValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name='ticktext',
                       parent_name='parcoords.dimension',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)