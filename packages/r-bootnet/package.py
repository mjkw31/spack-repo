# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootnet(RPackage):
	"""Bootstrap Methods for Various Network Estimation Routines

	Bootstrap methods to assess accuracy and stability of estimated network structures
              and centrality indices <doi:10.3758/s13428-017-0862-1>. Allows for flexible 
              specification of any undirected network estimation procedure in R, and offers 
              default sets for various estimation routines.
	"""
	
	cran = "bootnet" 

	version("1.5.6", md5="4ab42f64f64f042cc1aba0f301a37c85")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-isingfit@0.4:", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-dplyr@0.3.0.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-isingsampler@0.2.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-mgm@1.2:", type=("build", "run"))
	depends_on("r-networktoolbox@1.1:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-networktools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
