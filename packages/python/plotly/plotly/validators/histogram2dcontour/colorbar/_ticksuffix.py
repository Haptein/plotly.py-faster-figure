

import _plotly_utils.basevalidators as _bv


class TicksuffixValidator(_bv.StringValidator):
    def __init__(self, plotly_name='ticksuffix',
                       parent_name='histogram2dcontour.colorbar',
                       **kwargs):
        super(TicksuffixValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'colorbars'),
        **kwargs)