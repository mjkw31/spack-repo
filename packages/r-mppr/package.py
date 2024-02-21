# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMppr(RPackage):
	"""Multi-Parent Population QTL Analysis

	Analysis of experimental multi-parent populations to detect regions
             of the genome (called quantitative trait loci, QTLs) influencing
             phenotypic traits measured in unique and multiple environments.
             The population must be composed of crosses between a set of at
             least three parents (e.g. factorial design, 'diallel', or nested
             association mapping). The functions cover data processing,
             QTL detection, and results visualization. The implemented methodology
             is described in Garin, Wimmer, Mezmouk, Malosetti and van Eeuwijk (2017)
             <doi:10.1007/s00122-017-2923-3> as well as in Garin, Malosetti
             and van Eeuwijk (2020) <doi: 10.1007/s00122-020-03621-0>.
	"""
	
	homepage = "https://github.com/vincentgarin/mppR"
	cran = "mppR" 

	version("1.4.0", md5="6df5533429c0d8099290b9eecc5a7e77")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
