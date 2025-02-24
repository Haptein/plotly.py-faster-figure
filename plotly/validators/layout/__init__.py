import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._yaxis.YaxisValidator",
        "._xaxis.XaxisValidator",
        "._width.WidthValidator",
        "._waterfallmode.WaterfallmodeValidator",
        "._waterfallgroupgap.WaterfallgroupgapValidator",
        "._waterfallgap.WaterfallgapValidator",
        "._violinmode.ViolinmodeValidator",
        "._violingroupgap.ViolingroupgapValidator",
        "._violingap.ViolingapValidator",
        "._updatemenudefaults.UpdatemenudefaultsValidator",
        "._updatemenus.UpdatemenusValidator",
        "._uniformtext.UniformtextValidator",
        "._uirevision.UirevisionValidator",
        "._treemapcolorway.TreemapcolorwayValidator",
        "._transition.TransitionValidator",
        "._title.TitleValidator",
        "._ternary.TernaryValidator",
        "._template.TemplateValidator",
        "._sunburstcolorway.SunburstcolorwayValidator",
        "._spikedistance.SpikedistanceValidator",
        "._smith.SmithValidator",
        "._sliderdefaults.SliderdefaultsValidator",
        "._sliders.SlidersValidator",
        "._showlegend.ShowlegendValidator",
        "._shapedefaults.ShapedefaultsValidator",
        "._shapes.ShapesValidator",
        "._separators.SeparatorsValidator",
        "._selectiondefaults.SelectiondefaultsValidator",
        "._selections.SelectionsValidator",
        "._selectionrevision.SelectionrevisionValidator",
        "._selectdirection.SelectdirectionValidator",
        "._scene.SceneValidator",
        "._scattermode.ScattermodeValidator",
        "._scattergap.ScattergapValidator",
        "._polar.PolarValidator",
        "._plot_bgcolor.Plot_BgcolorValidator",
        "._piecolorway.PiecolorwayValidator",
        "._paper_bgcolor.Paper_BgcolorValidator",
        "._newshape.NewshapeValidator",
        "._newselection.NewselectionValidator",
        "._modebar.ModebarValidator",
        "._minreducedwidth.MinreducedwidthValidator",
        "._minreducedheight.MinreducedheightValidator",
        "._metasrc.MetasrcValidator",
        "._meta.MetaValidator",
        "._margin.MarginValidator",
        "._mapbox.MapboxValidator",
        "._map.MapValidator",
        "._legend.LegendValidator",
        "._imagedefaults.ImagedefaultsValidator",
        "._images.ImagesValidator",
        "._iciclecolorway.IciclecolorwayValidator",
        "._hoversubplots.HoversubplotsValidator",
        "._hovermode.HovermodeValidator",
        "._hoverlabel.HoverlabelValidator",
        "._hoverdistance.HoverdistanceValidator",
        "._hidesources.HidesourcesValidator",
        "._hiddenlabelssrc.HiddenlabelssrcValidator",
        "._hiddenlabels.HiddenlabelsValidator",
        "._height.HeightValidator",
        "._grid.GridValidator",
        "._geo.GeoValidator",
        "._funnelmode.FunnelmodeValidator",
        "._funnelgroupgap.FunnelgroupgapValidator",
        "._funnelgap.FunnelgapValidator",
        "._funnelareacolorway.FunnelareacolorwayValidator",
        "._font.FontValidator",
        "._extendtreemapcolors.ExtendtreemapcolorsValidator",
        "._extendsunburstcolors.ExtendsunburstcolorsValidator",
        "._extendpiecolors.ExtendpiecolorsValidator",
        "._extendiciclecolors.ExtendiciclecolorsValidator",
        "._extendfunnelareacolors.ExtendfunnelareacolorsValidator",
        "._editrevision.EditrevisionValidator",
        "._dragmode.DragmodeValidator",
        "._datarevision.DatarevisionValidator",
        "._computed.ComputedValidator",
        "._colorway.ColorwayValidator",
        "._colorscale.ColorscaleValidator",
        "._coloraxis.ColoraxisValidator",
        "._clickmode.ClickmodeValidator",
        "._calendar.CalendarValidator",
        "._boxmode.BoxmodeValidator",
        "._boxgroupgap.BoxgroupgapValidator",
        "._boxgap.BoxgapValidator",
        "._barnorm.BarnormValidator",
        "._barmode.BarmodeValidator",
        "._bargroupgap.BargroupgapValidator",
        "._bargap.BargapValidator",
        "._barcornerradius.BarcornerradiusValidator",
        "._autotypenumbers.AutotypenumbersValidator",
        "._autosize.AutosizeValidator",
        "._annotationdefaults.AnnotationdefaultsValidator",
        "._annotations.AnnotationsValidator",
        "._activeshape.ActiveshapeValidator",
        "._activeselection.ActiveselectionValidator",
    ],
)
