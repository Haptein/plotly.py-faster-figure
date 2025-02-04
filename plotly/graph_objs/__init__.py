import sys
from _plotly_utils.importers import relative_import
__all__, __getattr__, __dir__ = relative_import(
    __name__,
    ['.bar', '.barpolar', '.box', '.candlestick', '.carpet', '.choropleth', '.choroplethmap', '.choroplethmapbox', '.cone', '.contour', '.contourcarpet', '.densitymap', '.densitymapbox', '.funnel', '.funnelarea', '.heatmap', '.histogram', '.histogram2d', '.histogram2dcontour', '.icicle', '.image', '.indicator', '.isosurface', '.layout', '.mesh3d', '.ohlc', '.parcats', '.parcoords', '.pie', '.sankey', '.scatter', '.scatter3d', '.scattercarpet', '.scattergeo', '.scattergl', '.scattermap', '.scattermapbox', '.scatterpolar', '.scatterpolargl', '.scattersmith', '.scatterternary', '.splom', '.streamtube', '.sunburst', '.surface', '.table', '.treemap', '.violin', '.volume', '.waterfall'],
    ['._bar.Bar', '._barpolar.Barpolar', '._box.Box', '._candlestick.Candlestick', '._carpet.Carpet', '._choropleth.Choropleth', '._choroplethmap.Choroplethmap', '._choroplethmapbox.Choroplethmapbox', '._cone.Cone', '._contour.Contour', '._contourcarpet.Contourcarpet', '._densitymap.Densitymap', '._densitymapbox.Densitymapbox', '._deprecations.AngularAxis', '._deprecations.Annotation', '._deprecations.Annotations', '._deprecations.ColorBar', '._deprecations.Contours', '._deprecations.Data', '._deprecations.ErrorX', '._deprecations.ErrorY', '._deprecations.ErrorZ', '._deprecations.Font', '._deprecations.Frames', '._deprecations.Histogram2dcontour', '._deprecations.Legend', '._deprecations.Line', '._deprecations.Margin', '._deprecations.Marker', '._deprecations.RadialAxis', '._deprecations.Scene', '._deprecations.Stream', '._deprecations.Trace', '._deprecations.XAxis', '._deprecations.XBins', '._deprecations.YAxis', '._deprecations.YBins', '._deprecations.ZAxis', '._figure.Figure', '._frame.Frame', '._funnel.Funnel', '._funnelarea.Funnelarea', '._heatmap.Heatmap', '._histogram.Histogram', '._histogram2d.Histogram2d', '._histogram2dcontour.Histogram2dContour', '._icicle.Icicle', '._image.Image', '._indicator.Indicator', '._isosurface.Isosurface', '._layout.Layout', '._mesh3d.Mesh3d', '._ohlc.Ohlc', '._parcats.Parcats', '._parcoords.Parcoords', '._pie.Pie', '._sankey.Sankey', '._scatter.Scatter', '._scatter3d.Scatter3d', '._scattercarpet.Scattercarpet', '._scattergeo.Scattergeo', '._scattergl.Scattergl', '._scattermap.Scattermap', '._scattermapbox.Scattermapbox', '._scatterpolar.Scatterpolar', '._scatterpolargl.Scatterpolargl', '._scattersmith.Scattersmith', '._scatterternary.Scatterternary', '._splom.Splom', '._streamtube.Streamtube', '._sunburst.Sunburst', '._surface.Surface', '._table.Table', '._treemap.Treemap', '._violin.Violin', '._volume.Volume', '._waterfall.Waterfall']
)


__all__.append("FigureWidget")
orig_getattr = __getattr__
def __getattr__(import_name):
    if import_name == "FigureWidget":
        try:
            import ipywidgets
            from packaging.version import Version

            if Version(ipywidgets.__version__) >= Version("7.0.0"):
                from ..graph_objs._figurewidget import FigureWidget
                return FigureWidget
            else:
                raise ImportError()
        except Exception:
            from ..missing_anywidget import FigureWidget
            return FigureWidget

    return orig_getattr(import_name)

