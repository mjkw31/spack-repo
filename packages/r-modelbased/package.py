# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelbased(RPackage):
	"""Estimation of Model-Based Predictions, Contrasts and Means

	Implements a general interface for model-based estimations
    for a wide variety of models (see list of supported models using the
    function 'insight::supported_models()'), used in the computation of
    marginal means, contrast analysis and predictions.
	"""
	
	homepage = "https://easystats.github.io/modelbased/"
	cran = "modelbased" 

	version("0.8.6", md5="01c727579b728f6c01988c78d47f3e4a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayestestr@0.13:", type=("build", "run"))
	depends_on("r-datawizard@0.6.2:", type=("build", "run"))
	depends_on("r-effectsize@0.8.1:", type=("build", "run"))
	depends_on("r-insight@0.18.5:", type=("build", "run"))
	depends_on("r-parameters@0.19:", type=("build", "run"))
	depends_on("r-performance@0.10:", type=("build", "run"))
