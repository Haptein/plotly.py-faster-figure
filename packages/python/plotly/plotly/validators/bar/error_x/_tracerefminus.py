

import _plotly_utils.basevalidators as _bv


class TracerefminusValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name='tracerefminus',
                       parent_name='bar.error_x',
                       **kwargs):
        super(TracerefminusValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'style'),
                 min=kwargs.pop('min', 0),
        **kwargs)