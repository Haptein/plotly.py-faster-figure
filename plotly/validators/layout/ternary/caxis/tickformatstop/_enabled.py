

import _plotly_utils.basevalidators as _bv


class EnabledValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='enabled',
                       parent_name='layout.ternary.caxis.tickformatstop',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)