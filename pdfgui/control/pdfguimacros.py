########################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
########################################################################

"""Methods for macros used in pdfgui."""
from controlerrors import ControlValueError, ControlTypeError

def makeRSeries(control, fit, maxfirst = None, maxlast = None, maxstep = None,
        minfirst = None, minlast = None, minstep = None):
    """Make an series of fits with an increasing r-range.

    The new fits are appended to the end of any current fits in the control.

    control     --  The control object that will contain the fits
    fit         --  The prototype fit
    maxfirst    --  The first value of the maximum of the fit range
    maxlast     --  The last value of the maximum of the fit range
    maxstep     --  The step size of the maximum of the fit range
    minfirst    --  The first value of the minimum of the fit range
    minlast     --  The last value of the minimum of the fit range
    minstep     --  The step size of the minimum of the fit range

    returns a list of the new fit organization objects
    """
    # Check to see if the input values are correct.

    # MIN-MIN: FIRST < LAST
    if minfirst is not None and minlast is not None\
            and not minfirst < minlast:
        message = "The first value of the minimum (%.2f)\
                 \nmust be less than the last value of the\
                 \nminimum (%.2f)" % (minfirst, minlast)
        raise ControlValueError, message

    # MAX-MAX: FIRST < LAST
    if maxfirst is not None and maxlast is not None\
            and not maxfirst < maxlast:
        message = "The first value of the maximum (%.2f)\
                 \nmust be less than the last value of the\
                 \nmaximum (%.2f)" % (maxfirst, maxlast)
        raise ControlValueError, message

    # MAX > MIN: FIRST-FIRST
    if maxfirst is not None and minfirst is not None\
            and not maxfirst > minfirst:
        message = "The first value of the fit maximum (%.2f)\
                 \nmust be greater than first value of the fit\
                 \nminimum (%.2f)." % (maxfirst, minfirst)
        raise ControlValueError, message

    # MAX > MIN: LAST-LAST
    if maxlast is not None and minlast is not None\
            and not maxlast > minlast:
        message = "The last value of the fit maximum (%.2f)\
                 \nmust be greater than last value of the fit\
                 \nminimum (%.2f)." % (maxlast, minlast)
        raise ControlValueError, message

    # STEP > 0
    message = "Step size (%.2f) must be greater than 0."
    if maxstep is not None and not maxstep > 0:
        raise ControlValueError, message % maxstep
    if minstep is not None and not minstep > 0:
        raise ControlValueError, message % minstep

    # Check to see that either max or min is fully specified
    maxlist = [maxfirst, maxlast]
    minlist = [minfirst, minlast]
    if maxlist.count(None) == 1 or minlist.count(None) == 1:
        raise ControlValueError, "First and last values are partially specified"
    if maxstep is None and minstep is None:
        raise ControlValueError, "Either minstep or maxstep must be specified."

    maxlist = []
    minlist = []
    if maxfirst is not None:
        if maxstep is None: maxstep = minstep
        maxrange = int((maxlast-maxfirst)/(1.0*maxstep)+1)
        maxlist = [maxfirst + i*maxstep for i in range(maxrange)]
    if minfirst is not None:
        if minstep is None: minstep = maxstep
        minrange = int((minlast-minfirst)/(1.0*minstep)+1)
        minlist = [minfirst + i*minstep for i in range(minrange)]

    # Resize the lists to the length of the shortest
    serieslen = min(len(maxlist), len(minlist))
    if serieslen != 0:
        maxlist = maxlist[:serieslen]
        minlist = minlist[:serieslen]
    else:
        serieslen =  max(len(maxlist), len(minlist))

    basename = fit.name
    fits = []
    namelist = [item.name for item in control.fits]

    newname = ''
    lastname = ''
    fitcopy = control.copy(fit)
    # Duplicate the original fit and change the appropriate parameters.
    for i in range(serieslen):
        lastname = newname

        # Loop over datasets
        for ds in fitcopy.datasets:

            if minlist:
                fitrmin = minlist[i]
            else:
                fitrmin = ds.fitrmin
            if maxlist:
                fitrmax = maxlist[i]
            else:
                fitrmax = ds.fitrmax

            # Check to see that the values are in bounds and sensical
            if fitrmin < ds.rmin or fitrmin >= ds.rmax:
                message = "Fit minimum (%.2f) is outside the data range\
                           \n[%.2f, %.2f].\
                           \nAdjust the range of the series."\
                           % (fitrmin, ds.rmin, ds.rmax)
                raise ControlValueError, message
            if fitrmax <= ds.rmin or fitrmax > ds.rmax:
                message = "Fit maximum (%.2f) is outside the data range\
                           \n[%.2f, %.2f].\
                           \nAdjust the range of the series."\
                           % (fitrmax, ds.rmin, ds.rmax)
                raise ControlValueError, message
            if fitrmin >= fitrmax:
                message = "Fit minimum (%.2f) is greater than the\
                           \nmaximum (%.2f).\
                           \nIncrease maxstep or reduce minstep." % (fitrmin, fitrmax)
                raise ControlValueError, message


            # Set the values if all is well
            if minlist:
                ds.fitrmin = fitrmin
            if maxlist:
                ds.fitrmax = fitrmax

        # Set the parameters to the previous fit's name, if one exists.
        if lastname:
            parval = "=%s" % lastname
            for par in fitcopy.parameters.values():
                par.setInitial(parval)

        # Now paste the copy into the control.
        newname = "%s-(%.2f,%.2f)" % (basename, fitrmin, fitrmax)
        o = control.paste(fitcopy, new_name = newname)
        fits.append(o)

    return [f.organization() for f in fits]


if __name__ == "__main__":
    from pdfguicontrol import PDFGuiControl
    control = PDFGuiControl()
    control.load("../../tests/testdata/ni.ddp")
    fit = control.fits[0]
    olist = makeRSeries(control, fit, 5, 20, 5)
    print '\n'.join([fit[0].name for fit in olist])

# version
__id__ = "$Id$"

# End of file