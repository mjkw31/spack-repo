# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmertest(RPackage):
	"""Tests in Linear Mixed Effects Models.

	Provides p-values in type I, II or III anova and summary tables for lmer
	model fits (cf. lme4) via Satterthwaite's degrees of freedom method. A
	Kenward-Roger method is also available via the pbkrtest package. Model
	selection methods include step, drop1 and anova-like tables for random
	effects (ranova). Methods for Least-Square means (LS-means) and tests of
	linear contrasts of fixed effects are also available."""

	cran = "lmerTest"

	version("3.1-3", md5="9dcd5c0277debea42b1e05ecf98ad6cd")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-lme4@1.1.10:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
