

import _plotly_utils.basevalidators


class VariantsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name='variantsrc',
                       parent_name='scatterpolar.hoverlabel.font',
                       **kwargs):
        super(VariantsrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)