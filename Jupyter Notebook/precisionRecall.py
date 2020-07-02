# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:29:29 2020

@author: Carlota
"""

# -*- coding: utf-8 -*-
"""
Script to plot recall-precision values with f-measure equi-potential lines.
Created on Dec 16, 2009
@author: Jörn Hees
"""

import scipy as sc
import pylab as pl
import itertools as it
import numpy

def fmeasure(p, r):
    """Calculates the fmeasure for precision p and recall r."""
    return (2*p*r / (p+r))


def _fmeasureCurve(f, p):
    """For a given f1 value and precision get the recall value.
    The f1 measure is defined as: f(p,r) = 2*p*r / (p + r).
    If you want to plot "equipotential-lines" into a precision/recall diagramm
    (recall (y) over precision (x)), for a given fixed f value we get this
    function by solving for r:
    """
    return (f * p / (2 * p - f))


def _plotFMeasures(fstepsize=.1, stepsize=0.001):
    """Plots 10 fmeasure Curves into the current canvas."""
    p = sc.arange(0., 1., stepsize)[1:]
    for f in sc.arange(0., 1., fstepsize)[1:]:
        points = [(x, _fmeasureCurve(f, x)) for x in p
                  if 0 < _fmeasureCurve(f, x) <= 1.5]
        xs, ys = zip(*points)
        curve, = pl.plot(xs, ys, "--", color="gray", linewidth=0.5)  # , label=r"$f=%.1f$"%f) # exclude labels, for legend
        # bad hack:
        # gets the 10th last datapoint, from that goes a bit to the left, and a bit down
        pl.annotate(r"$F1=%.1f$" % f, xy=(xs[-10], ys[-10]), xytext=(xs[-10] - 0.1, ys[-10] - 0.035), size="small", color="gray")

# def _contourPlotFMeasure():
#    delta = 0.01
#    x = sc.arange(0.,1.,delta)
#    y = sc.arange(0.,1.,delta)
#    X,Y = sc.meshgrid(x,y)
#    cs = pl.contour(X,Y,fmeasure,sc.arange(0.1,1.0,0.1)) # FIXME: make an array out of fmeasure first
#    pl.clabel(cs, inline=1, fontsize=10)

#colors = "bgrcmyk"  # 7 is a prime, so we'll loop over all combinations of colors and markers, when zipping their cycles
#markers = "so^>v<dph8"  # +x taken out, as no color.

# # if you don't believe the prime loop:
# icons = set()
# for i,j in it.izip(it.cycle(colors),it.cycle(markers)):
#    if (i,j) in icons: break
#    icons.add((i,j))
# print len(icons), len(colors)*len(markers)


def plotPrecisionRecallDiagram(points, labels, colors, size, loc="best"):
    """Plot (precision,recall) values with 10 f-Measure equipotential lines.
    Plots into the current canvas.
    Points is a list of (precision,recall) pairs.
    Optionally you can also provide labels (list of strings), which will be
    used to create a legend, which is located at loc.
    """
    if labels:
        ax = pl.axes([0.1, 0.1, 0.7, 0.8])  # llc_x, llc_y, width, height
    else:
        ax = pl.gca()
    #pl.title(title)
    pl.xlabel("Precision")
    pl.ylabel("Recall")
    _plotFMeasures()

    # _contourPlotFMeasure()

    if points is not None:
        #getColor = it.cycle(colors).next
        #getMarker = it.cycle(markers).next

        scps = []  # scatter points
        for i, (x, y) in enumerate(points):
            label = None
            #if labels:
            #    label = labels[i]
            #print (i, x, y, label)
            scp = ax.scatter(x, y, label=label, s=size, linewidths=0.75,
                             facecolor=colors[i], alpha=0.75, marker='o')
            scps.append(scp)
            # pl.plot(x,y, label=label, marker=getMarker(), markeredgewidth=0.75, markerfacecolor=getColor())
            # if labels: pl.text(x, y, label, fontsize="x-small")
        if labels is not None:
            legend = labels
            # pl.legend(scps, labels, loc=loc, scatterpoints=1, numpoints=1, fancybox=True) # passing scps & labels explicitly to work around a bug with legend seeming to miss out the 2nd scatterplot
            pl.legend(scps, legend, loc=(1.01, 0), scatterpoints=1, numpoints=1, fancybox=True)  # passing scps & labels explicitly to work around a bug with legend seeming to miss out the 2nd scatterplot
    pl.axis([-0.02, 1.02, -0.02, 1.02])  # xmin, xmax, ymin, ymax


#if __name__ == '__main__':
    # plotPrecisionRecallDiagram(points=[(0.9,0.95), (0.9,0.6), (0.7,0.9), (0.25,0.9)], labels=["foaf 0.5", "foaf 0.75", "foaf 0.25", "bar"])
#    plotPrecisionRecallDiagram("footitle", sc.rand(15, 2), ["item " + str(i) for i in range(15)])
#    pl.show()