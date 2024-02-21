# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastcpd(RPackage):
	"""Fast Change Point Detection via Sequential Gradient Descent

	Implements fast change point detection algorithm based on the
    paper "Sequential Gradient Descent and Quasi-Newton's Method for
    Change-Point Analysis" by Xianyang Zhang, Trisha Dawn
    <https://proceedings.mlr.press/v206/zhang23b.html>. The algorithm is
    based on dynamic programming with pruning and sequential gradient
    descent. It is able to detect change points a magnitude faster than
    the vanilla Pruned Exact Linear Time(PELT). The package includes
    examples of linear regression, logistic regression, Poisson
    regression, penalized linear regression data, and whole lot more
    examples with custom cost function in case the user wants to use their
    own cost function.
	"""
	
	homepage = "https://fastcpd.xingchi.li"
	cran = "fastcpd" 

	version("0.10.3", md5="bef88d895ea1da41e3a1b5bc51ab3637")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fastglm", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
