

import _plotly_utils.basevalidators


class LinepositionValidator(_plotly_utils.basevalidators.FlaglistValidator):
    def __init__(self, plotly_name='lineposition',
                       parent_name='pie.outsidetextfont',
                       **kwargs):
        super(LinepositionValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 extras=kwargs.pop('extras', ['none']),
                 flags=kwargs.pop('flags', ['under', 'over', 'through']),
        **kwargs)