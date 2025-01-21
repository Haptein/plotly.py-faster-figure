

import _plotly_utils.basevalidators as _bv


class Mesh3DValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='mesh3d',
                       parent_name='layout.template.data',
                       **kwargs):
        super(Mesh3DValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Mesh3d'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)