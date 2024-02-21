# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurrogate(RPackage):
	"""Evaluation of Surrogate Endpoints in Clinical Trials

	In a clinical trial, it frequently occurs that the most credible outcome to evaluate the effectiveness of a new therapy (the true endpoint) is difficult to measure. In such a situation, it can be an effective strategy to replace the true endpoint by a (bio)marker that is easier to measure and that allows for a prediction of the treatment effect on the true endpoint (a surrogate endpoint). The package 'Surrogate' allows for an evaluation of the appropriateness of a candidate surrogate endpoint based on the meta-analytic, information-theoretic, and causal-inference frameworks. Part of this software has been developed using funding provided from the European Union's Seventh Framework Programme for research, technological development and demonstration under Grant Agreement no 602552.
	"""
	
	homepage = "https://github.com/florianstijven/Surrogate-development"
	cran = "Surrogate" 

	version("3.2.1", md5="c9830b781540c7fc78e84f283eeb7e53")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-logistf", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-kdecopula", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rvinecopulib", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
