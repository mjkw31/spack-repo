# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmbayes(RPackage):
	"""Performing Bayesian Inference for Repeated-Measures Designs

	A Bayesian credible interval is interpreted with respect to posterior probability, 
	and this interpretation is far more intuitive than that of a frequentist confidence interval. 
	However, standard highest-density intervals can be wide due to between-subjects variability and tends 
	to hide within-subjects effects, rendering its relationship with the Bayes factor less clear 
	in within-subjects (repeated-measures) designs. 
	This urgent issue can be addressed by using within-subjects intervals in within-subjects designs, 
	which integrate four methods including the Loftus-Masson (1994) <doi:10.3758/BF03210951>, 
	the Rouder-Morey-Speckman-Province (2012) <doi:10.1016/j.jmp.2012.08.001>,
	the Nathoo-Kilshaw-Masson (2018) <doi:10.1016/j.jmp.2018.07.005>, 
	and the Heck (2019) <doi:10.31234/osf.io/whp8t> interval estimates.
	"""
	
	homepage = "https://github.com/zhengxiaoUVic/rmBayes"
	cran = "rmBayes"

	version("0.1.15", md5="bcd0e3bf3e14dd948ef741af0a2249e7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
