import sys
from _plotly_utils.importers import relative_import

__all__, __getattr__, __dir__ = relative_import(
    __name__,
    [],
    [
        "._zerolinewidth.ZerolinewidthValidator",
        "._zerolinecolor.ZerolinecolorValidator",
        "._zeroline.ZerolineValidator",
        "._visible.VisibleValidator",
        "._type.TypeValidator",
        "._title.TitleValidator",
        "._tickwidth.TickwidthValidator",
        "._tickvalssrc.TickvalssrcValidator",
        "._tickvals.TickvalsValidator",
        "._ticktextsrc.TicktextsrcValidator",
        "._ticktext.TicktextValidator",
        "._ticksuffix.TicksuffixValidator",
        "._ticks.TicksValidator",
        "._tickprefix.TickprefixValidator",
        "._tickmode.TickmodeValidator",
        "._ticklen.TicklenValidator",
        "._tickformatstopdefaults.TickformatstopdefaultsValidator",
        "._tickformatstops.TickformatstopsValidator",
        "._tickformat.TickformatValidator",
        "._tickfont.TickfontValidator",
        "._tickcolor.TickcolorValidator",
        "._tickangle.TickangleValidator",
        "._tick0.Tick0Validator",
        "._spikethickness.SpikethicknessValidator",
        "._spikesides.SpikesidesValidator",
        "._spikecolor.SpikecolorValidator",
        "._showticksuffix.ShowticksuffixValidator",
        "._showtickprefix.ShowtickprefixValidator",
        "._showticklabels.ShowticklabelsValidator",
        "._showspikes.ShowspikesValidator",
        "._showline.ShowlineValidator",
        "._showgrid.ShowgridValidator",
        "._showexponent.ShowexponentValidator",
        "._showbackground.ShowbackgroundValidator",
        "._showaxeslabels.ShowaxeslabelsValidator",
        "._separatethousands.SeparatethousandsValidator",
        "._rangemode.RangemodeValidator",
        "._range.RangeValidator",
        "._nticks.NticksValidator",
        "._mirror.MirrorValidator",
        "._minexponent.MinexponentValidator",
        "._minallowed.MinallowedValidator",
        "._maxallowed.MaxallowedValidator",
        "._linewidth.LinewidthValidator",
        "._linecolor.LinecolorValidator",
        "._labelalias.LabelaliasValidator",
        "._hoverformat.HoverformatValidator",
        "._gridwidth.GridwidthValidator",
        "._gridcolor.GridcolorValidator",
        "._exponentformat.ExponentformatValidator",
        "._dtick.DtickValidator",
        "._color.ColorValidator",
        "._categoryorder.CategoryorderValidator",
        "._categoryarraysrc.CategoryarraysrcValidator",
        "._categoryarray.CategoryarrayValidator",
        "._calendar.CalendarValidator",
        "._backgroundcolor.BackgroundcolorValidator",
        "._autotypenumbers.AutotypenumbersValidator",
        "._autorangeoptions.AutorangeoptionsValidator",
        "._autorange.AutorangeValidator",
    ],
)
