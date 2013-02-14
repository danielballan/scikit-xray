"""
   LMfit-py provides a Least-Squares Minimization routine and
   class with a simple, flexible approach to parameterizing a
   model for fitting to data.  Named Parameters can be held
   fixed or freely adjusted in the fit, or held between lower
   and upper bounds.  If the separate asteval module has been
   installed, parameters can be constrained as a simple
   mathematical expression of other Parameters.

   version: 0.7
   last update:  14-Sept-2012
   License: BSD
   Author:  Matthew Newville <newville@cars.uchicago.edu>
            Center for Advanced Radiation Sources,
            The University of Chicago
"""
__version__ = '0.7.1'
from .minimizer import minimize, Minimizer, MinimizerException
from .parameter import Parameter, Parameters
from .confidence import conf_interval, conf_interval2d
from .printfuncs import (fit_report, ci_report,
                         report_fit, report_ci, report_errors)

__all__ = ['minimize', 'Minimizer', 'Parameter', 'Parameters',
           'conf_interval', 'conf_interval2d',
           'fit_report', 'ci_report', 'report_errors',
           'report_fit', 'report_ci']
