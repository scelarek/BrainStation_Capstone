import pytest
from covsirphy import ScatterPlot, scatter_plot
from covsirphy import UnExecutedError


def test_plot(japan_df, imgfile):
    df = japan_df.rename(columns={"Positive": "x", "Discharged": "y"})
    # Create a scatter plot
    scatter_plot(df, filename=imgfile)


def test_error(japan_df, imgfile):
    df = japan_df.rename(columns={"Positive": "x", "Discharged": "y"})
    # Plotting not done
    with ScatterPlot(filename=imgfile) as sp:
        with pytest.raises(UnExecutedError):
            sp.line_straight()
    # Cannot show a legend
    with ScatterPlot(filename=imgfile) as sp:
        sp.plot(data=df)
        with pytest.raises(NotImplementedError):
            sp.legend()
        with pytest.raises(NotImplementedError):
            sp.legend_hide()
