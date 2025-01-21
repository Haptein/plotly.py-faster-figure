

import _plotly_utils.basevalidators as _bv


class InsiderangeValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name='insiderange',
                       parent_name='layout.yaxis',
                       **kwargs):
        super(InsiderangeValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 items=kwargs.pop('items', [{'editType': 'plot', 'valType': 'any'}, {'editType': 'plot', 'valType': 'any'}]),
        **kwargs)