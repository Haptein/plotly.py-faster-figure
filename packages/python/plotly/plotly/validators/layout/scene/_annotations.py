

import _plotly_utils.basevalidators as _bv


class AnnotationsValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='annotations',
                       parent_name='layout.scene',
                       **kwargs):
        super(AnnotationsValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Annotation'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)