# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElfgen(RPackage):
	"""Ecological Limit Function Model Generation and Analysis Toolkit

	
	A toolset for generating Ecological Limit Function (ELF) models and evaluating potential species loss resulting from flow change, based on the 'elfgen' framework. ELFs describe the relation between aquatic species richness (fish or benthic macroinvertebrates) and stream size characteristics (streamflow or drainage area). Journal publications are available outlining framework methodology (Kleiner et al. (2020) <doi:10.1111/1752-1688.12876>) and application (Rapp et al. (2020) <doi:10.1111/1752-1688.12877>).
	"""
	
	homepage = "https://github.com/HARPgroup/elfgen"
	cran = "elfgen" 

	version("2.3.3", md5="070212cd67a1e54f38efaca22da169a6")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-testit", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-sbtools", type=("build", "run"))
	depends_on("r-nhdplustools", type=("build", "run"))
