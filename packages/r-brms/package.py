# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrms(RPackage):
	"""Bayesian Regression Models using 'Stan'.

	Fit Bayesian generalized (non-)linear multivariate multilevel models using
	'Stan' for full Bayesian inference. A wide range of distributions and link
	functions are supported, allowing users to fit - among others - linear,
	robust linear, count data, survival, response times, ordinal,
	zero-inflated, hurdle, and even self-defined mixture models all in a
	multilevel context. Further modeling options include non-linear and smooth
	terms, auto-correlation structures, censored data, meta-analytic standard
	errors, and quite a few more. In addition, all parameters of the response
	distribution can be predicted in order to perform distributional
	regression. Prior specifications are flexible and explicitly encourage
	users to apply prior distributions that actually reflect their beliefs.
	Model fit can easily be assessed and compared with posterior predictive
	checks and leave-one-out cross-validation.  References: Burkner (2017)
	<doi:10.18637/jss.v080.i01>; Burkner (2018) <doi:10.32614/RJ-2018-017>;
	Carpenter et al. (2017) <doi:10.18637/jss.v076.i01>."""

	cran = "brms"

	version("2.20.4", md5="cd5e8124a77500735c1bc1a9ca19f2c0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-loo@2.3.1:", type=("build", "run"))
	depends_on("r-posterior@1:", type=("build", "run"))
	depends_on("r-matrix@1.1.1:", type=("build", "run"))
	depends_on("r-mgcv@1.8.13:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-bayesplot@1.5:", type=("build", "run"))
	depends_on("r-shinystan@2.4:", type=("build", "run"))
	depends_on("r-bridgesampling@0.3.0:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-future@1.19:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
