# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoubleml(RPackage):
	"""Double Machine Learning in R

	Implementation of the double/debiased machine learning framework of
    Chernozhukov et al. (2018) <doi:10.1111/ectj.12097> for partially linear
    regression models, partially linear instrumental variable regression models,
    interactive regression models and interactive instrumental variable
    regression models. 'DoubleML' allows estimation of the nuisance parts in
    these models by machine learning methods and computation of the Neyman
    orthogonal score functions. 'DoubleML' is built on top of 'mlr3' and the
    'mlr3' ecosystem. The object-oriented implementation of 'DoubleML' based on
    the 'R6' package is very flexible. 
	"""
	
	homepage = "https://docs.doubleml.org/stable/index.html"
	cran = "DoubleML" 

	version("0.5.3", md5="16f4033121c06f1ecd86319e491e5bf0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-mlr3@0.5:", type=("build", "run"))
	depends_on("r-mlr3tuning@0.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-clustergeneration", type=("build", "run"))
	depends_on("r-readstata13", type=("build", "run"))
	depends_on("r-mlr3learners@0.3:", type=("build", "run"))
	depends_on("r-mlr3misc", type=("build", "run"))
