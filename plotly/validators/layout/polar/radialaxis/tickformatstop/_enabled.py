

import _plotly_utils.basevalidators as _bv


class EnabledValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='enabled',
                       parent_name='layout.polar.radialaxis.tickformatstop',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)