

import _plotly_utils.basevalidators as _bv


class HoverformatValidator(_bv.StringValidator):
    def __init__(self, plotly_name='hoverformat',
                       parent_name='layout.scene.xaxis',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)