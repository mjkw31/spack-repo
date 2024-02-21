# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTspredit(RPackage):
	"""Time Series Prediction Integrated Tuning

	Prediction is one of the most important activities while working with time series. There are many alternative ways to model the time series. Finding the right one is challenging to model them. Most data-driven models (either statistical or machine learning) demand tuning. Setting them right is mandatory for good predictions. It is even more complex since time series prediction also demands choosing a data pre-processing that complies with the chosen model. Many time series frameworks have features to build and tune models. The package differs as it provides a framework that seamlessly integrates tuning data pre-processing activities with the building of models. The package provides functions for defining and conducting time series prediction, including data pre(post)processing, decomposition, tuning, modeling, prediction, and accuracy assessment. More information is available at Izau et al. <doi:10.5753/sbbd.2022.224330>.
	"""
	
	homepage = "https://github.com/cefet-rj-dal/daltoolbox"
	cran = "tspredit" 

	version("1.0.747", md5="52696139e4e6251c264da1092587fc48")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-smotefamily", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-fselector", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-mfilter", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-kfas", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
	depends_on("r-daltoolbox", type=("build", "run"))
