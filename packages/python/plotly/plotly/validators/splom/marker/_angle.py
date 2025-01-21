

import _plotly_utils.basevalidators as _bv


class AngleValidator(_bv.AngleValidator):
    def __init__(self, plotly_name='angle',
                       parent_name='splom.marker',
                       **kwargs):
        super(AngleValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)