

import _plotly_utils.basevalidators as _bv


class AspectratioValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='aspectratio',
                       parent_name='funnelarea',
                       **kwargs):
        super(AspectratioValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 min=kwargs.pop('min', 0),
        **kwargs)