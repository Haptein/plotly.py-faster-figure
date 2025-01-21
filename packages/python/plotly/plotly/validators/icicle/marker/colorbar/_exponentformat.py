

import _plotly_utils.basevalidators as _bv


class ExponentformatValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='exponentformat',
                       parent_name='icicle.marker.colorbar',
                       **kwargs):
        super(ExponentformatValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'colorbars'),
                 values=kwargs.pop('values', ['none', 'e', 'E', 'power', 'SI', 'B']),
        **kwargs)