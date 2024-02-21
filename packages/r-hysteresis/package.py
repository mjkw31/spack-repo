# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHysteresis(RPackage):
	"""Tools for Modeling Rate-Dependent Hysteretic Processes and
Ellipses

	Fit, summarize and plot sinusoidal hysteretic processes using:
    two-step simple harmonic least squares, ellipse-specific non-linear least
    squares, the direct method, geometric least squares or linear least squares.
	"""
	
	cran = "hysteresis" 

	version("2.7", md5="fd7fa5b07144c1c48e56208f79a31665")

	depends_on("r-car", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
