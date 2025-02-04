

import _plotly_utils.basevalidators as _bv


class OpacityValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='opacity',
                       parent_name='choroplethmapbox.selected.marker',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 max=kwargs.pop('max', 1),
                 min=kwargs.pop('min', 0),
        **kwargs)