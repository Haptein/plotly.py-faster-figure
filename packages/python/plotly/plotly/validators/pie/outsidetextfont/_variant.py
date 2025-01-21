

import _plotly_utils.basevalidators as _bv


class VariantValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='variant',
                       parent_name='pie.outsidetextfont',
                       **kwargs):
        super(VariantValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', ['normal', 'small-caps', 'all-small-caps', 'all-petite-caps', 'petite-caps', 'unicase']),
        **kwargs)