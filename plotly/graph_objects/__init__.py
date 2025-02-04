import sys
from _plotly_utils.importers import relative_import
__all__, __getattr__, __dir__ = relative_import(
    __name__,
    ['..graph_objs.waterfall', '..graph_objs.volume', '..graph_objs.violin', '..graph_objs.treemap', '..graph_objs.table', '..graph_objs.surface', '..graph_objs.sunburst', '..graph_objs.streamtube', '..graph_objs.splom', '..graph_objs.scatterternary', '..graph_objs.scattersmith', '..graph_objs.scatterpolargl', '..graph_objs.scatterpolar', '..graph_objs.scattermapbox', '..graph_objs.scattermap', '..graph_objs.scattergl', '..graph_objs.scattergeo', '..graph_objs.scattercarpet', '..graph_objs.scatter3d', '..graph_objs.scatter', '..graph_objs.sankey', '..graph_objs.pie', '..graph_objs.parcoords', '..graph_objs.parcats', '..graph_objs.ohlc', '..graph_objs.mesh3d', '..graph_objs.isosurface', '..graph_objs.indicator', '..graph_objs.image', '..graph_objs.icicle', '..graph_objs.histogram2dcontour', '..graph_objs.histogram2d', '..graph_objs.histogram', '..graph_objs.heatmap', '..graph_objs.funnelarea', '..graph_objs.funnel', '..graph_objs.densitymapbox', '..graph_objs.densitymap', '..graph_objs.contourcarpet', '..graph_objs.contour', '..graph_objs.cone', '..graph_objs.choroplethmapbox', '..graph_objs.choroplethmap', '..graph_objs.choropleth', '..graph_objs.carpet', '..graph_objs.candlestick', '..graph_objs.box', '..graph_objs.barpolar', '..graph_objs.bar', '..graph_objs.layout'],
    ['..graph_objs.Waterfall', '..graph_objs.Volume', '..graph_objs.Violin', '..graph_objs.Treemap', '..graph_objs.Table', '..graph_objs.Surface', '..graph_objs.Sunburst', '..graph_objs.Streamtube', '..graph_objs.Splom', '..graph_objs.Scatterternary', '..graph_objs.Scattersmith', '..graph_objs.Scatterpolargl', '..graph_objs.Scatterpolar', '..graph_objs.Scattermapbox', '..graph_objs.Scattermap', '..graph_objs.Scattergl', '..graph_objs.Scattergeo', '..graph_objs.Scattercarpet', '..graph_objs.Scatter3d', '..graph_objs.Scatter', '..graph_objs.Sankey', '..graph_objs.Pie', '..graph_objs.Parcoords', '..graph_objs.Parcats', '..graph_objs.Ohlc', '..graph_objs.Mesh3d', '..graph_objs.Isosurface', '..graph_objs.Indicator', '..graph_objs.Image', '..graph_objs.Icicle', '..graph_objs.Histogram2dContour', '..graph_objs.Histogram2d', '..graph_objs.Histogram', '..graph_objs.Heatmap', '..graph_objs.Funnelarea', '..graph_objs.Funnel', '..graph_objs.Densitymapbox', '..graph_objs.Densitymap', '..graph_objs.Contourcarpet', '..graph_objs.Contour', '..graph_objs.Cone', '..graph_objs.Choroplethmapbox', '..graph_objs.Choroplethmap', '..graph_objs.Choropleth', '..graph_objs.Carpet', '..graph_objs.Candlestick', '..graph_objs.Box', '..graph_objs.Barpolar', '..graph_objs.Bar', '..graph_objs.Layout', '..graph_objs.Frame', '..graph_objs.Figure', '..graph_objs.Data', '..graph_objs.Annotations', '..graph_objs.Frames', '..graph_objs.AngularAxis', '..graph_objs.Annotation', '..graph_objs.ColorBar', '..graph_objs.Contours', '..graph_objs.ErrorX', '..graph_objs.ErrorY', '..graph_objs.ErrorZ', '..graph_objs.Font', '..graph_objs.Legend', '..graph_objs.Line', '..graph_objs.Margin', '..graph_objs.Marker', '..graph_objs.RadialAxis', '..graph_objs.Scene', '..graph_objs.Stream', '..graph_objs.XAxis', '..graph_objs.YAxis', '..graph_objs.ZAxis', '..graph_objs.XBins', '..graph_objs.YBins', '..graph_objs.Trace', '..graph_objs.Histogram2dcontour']
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

