# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoastgsa(RPackage):
	"""Rotation based gene set analysis

	This package implements a variety of functions useful for gene set analysis using rotations to approximate the null distribution. It contributes with the implementation of seven test statistic scores that can be used with different goals and interpretations. Several functions are available to complement the statistical results with graphical representations.
	"""
	
	bioc = "roastgsa" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/roastgsa_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/roastgsa/roastgsa_1.0.0.tar.gz"]

	version("1.0.0", md5="83d20d90ed18c719222042ae3d9f46d3")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
