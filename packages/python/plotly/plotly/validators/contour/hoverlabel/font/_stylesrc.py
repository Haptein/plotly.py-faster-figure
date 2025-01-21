

import _plotly_utils.basevalidators as _bv


class StylesrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='stylesrc',
                       parent_name='contour.hoverlabel.font',
                       **kwargs):
        super(StylesrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)