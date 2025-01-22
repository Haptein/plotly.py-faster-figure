

import _plotly_utils.basevalidators


class XrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name='xref',
                       parent_name='choroplethmap.colorbar',
                       **kwargs):
        super(XrefValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'colorbars'),
                 values=kwargs.pop('values', ['container', 'paper']),
        **kwargs)