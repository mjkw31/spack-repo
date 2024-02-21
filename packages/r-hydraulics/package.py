# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydraulics(RPackage):
	"""Basic Pipe and Open Channel Hydraulics

	Functions for basic hydraulic calculations related to 
    water flow in circular pipes both flowing full (under pressure), and 
    partially full (gravity flow), and trapezoidal open channels. For 
    pressure flow this includes friction loss calculations by solving 
    the Darcy-Weisbach equation for head loss, flow or diameter, 
    plotting a Moody diagram, matching a pump characteristic curve to a system 
    curve, and solving for flows in a pipe network using the Hardy-Cross method. 
    The Darcy-Weisbach friction factor is calculated using the Colebrook 
    (or Colebrook-White equation), the basis of the Moody diagram, the original 
    citation being Colebrook (1939) <doi:10.1680/ijoti.1939.13150>. For gravity 
    flow, the Manning equation is used, again solving for missing parameters. 
    The derivation of and solutions using the Darcy-Weisbach equation and the
    Manning equation are outlined in many fluid mechanics texts such as 
    Finnemore and Franzini (2002, ISBN:978-0072432022). Some gradually- and 
    rapidly-varied flow functions are included. For the Manning equation
    solutions, this package uses modifications of original code from the 'iemisc' 
    package by Irucka Embry.
	"""
	
	homepage = "https://github.com/EdM44/hydraulics"
	cran = "hydraulics" 

	version("0.6.1", md5="d27b3f24744746e85cef3351e8855cd4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
