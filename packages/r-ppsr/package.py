# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpsr(RPackage):
	"""Predictive Power Score

	The PPS is an asymmetric, data-type-agnostic score that can detect 
    linear or non-linear relationships between two columns. The score ranges 
    from 0 (no predictive power) to 1 (perfect predictive power). It can be useful
    for data exploration purposes, in the same way correlation analysis is.
    For more information on PPS, see Wetschoreck (2020) <https://towardsdatascience.com/rip-correlation-introducing-the-predictive-power-score-3d90808b9598> 
    or github <https://github.com/paulvanderlaken/ppsr>.
	"""
	
	cran = "ppsr" 

	version("0.0.2", md5="842932de2c0b61319b2f55e382d1064d")

	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-parsnip@0.1.5:", type=("build", "run"))
	depends_on("r-rpart@4.1.15:", type=("build", "run"))
	depends_on("r-withr@2.4.1:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
