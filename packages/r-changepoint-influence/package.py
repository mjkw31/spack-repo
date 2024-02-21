# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChangepointInfluence(RPackage):
	"""Package to Calculate the Influence of the Data on a Changepoint
Segmentation

	Allows users to input their data, segmentation and function used for the segmentation (and additional arguments) and the package calculates the influence of the data on the changepoint locations, see Wilms et al. (2021) <arXiv:2107.10572>.  Currently this can only be used with the changepoint package functions to identify changes, but we plan to extend this.  There are options for different types of graphics to assess the influence.
	"""
	
	homepage = "https://github.com/rkillick/changepoint.influence/"
	cran = "changepoint.influence" 

	version("1.0.1", md5="8148656efd1734aac416b6f8882b0bec")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
