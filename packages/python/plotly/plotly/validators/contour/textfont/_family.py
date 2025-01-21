

import _plotly_utils.basevalidators as _bv


class FamilyValidator(_bv.StringValidator):
    def __init__(self, plotly_name='family',
                       parent_name='contour.textfont',
                       **kwargs):
        super(FamilyValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 no_blank=kwargs.pop('no_blank', True),
                 strict=kwargs.pop('strict', True),
        **kwargs)