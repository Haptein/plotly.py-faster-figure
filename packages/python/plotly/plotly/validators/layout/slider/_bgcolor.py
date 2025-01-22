

import _plotly_utils.basevalidators


class BgcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(self, plotly_name='bgcolor',
                       parent_name='layout.slider',
                       **kwargs):
        super(BgcolorValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'arraydraw'),
        **kwargs)