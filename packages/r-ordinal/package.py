# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdinal(RPackage):
	"""Regression Models for Ordinal Data.

	Implementation of cumulative link (mixed) models also known as ordered
	regression models, proportional odds models, proportional hazards models
	for grouped survival times and ordered logit/probit/... models. Estimation
	is via maximum likelihood and mixed models are fitted with the Laplace
	approximation and adaptive Gauss-Hermite quadrature. Multiple random effect
	terms are allowed and they may be nested, crossed or partially
	nested/crossed. Restrictions of symmetry and equidistance can be imposed on
	the thresholds (cut-points/intercepts). Standard model methods are
	available (summary, anova, drop-methods, step, confint, predict etc.) in
	addition to profile methods and slice methods for visualizing the
	likelihood function and checking convergence."""

	cran = "ordinal"

	version("2023.12-4", md5="a14e655e739d633b0d4e19220509f638")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
