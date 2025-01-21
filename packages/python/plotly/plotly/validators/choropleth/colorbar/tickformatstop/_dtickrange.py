

import _plotly_utils.basevalidators as _bv


class DtickrangeValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name='dtickrange',
                       parent_name='choropleth.colorbar.tickformatstop',
                       **kwargs):
        super(DtickrangeValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'colorbars'),
                 items=kwargs.pop('items', [{'editType': 'colorbars', 'valType': 'any'}, {'editType': 'colorbars', 'valType': 'any'}]),
        **kwargs)