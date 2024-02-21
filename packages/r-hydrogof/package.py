# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydrogof(RPackage):
	"""Goodness-of-Fit Functions for Comparison of Simulated and Observed
	Hydrological Time Series.

	S3 functions implementing both statistical and graphical goodness-of-fit
	measures between observed and simulated values, mainly oriented to be used
	during the calibration, validation, and application of hydrological models.
	Missing values in observed and/or simulated values can be removed before
	computations. Comments / questions / collaboration of any kind are very
	welcomed."""

	cran = "hydroGOF"

	version("0.5-4", md5="5abb111f6ab352678e15672ed09ec601")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-zoo@1.7.2:", type=("build", "run"))
	depends_on("r-hydrotsm@0.5.0:", type=("build", "run"))
	depends_on("r-xts@0.8.2:", type=("build", "run"))
