# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplatter(RPackage):
	"""Simple Simulation of Single-cell RNA Sequencing Data

	Splatter is a package for the simulation of single-cell RNA sequencing count data. It provides a simple interface for creating complex simulations that are reproducible and well-documented. Parameters can be estimated from real data and functions are provided for comparing real and simulated datasets.
	"""
	
	homepage = "https://github.com/Oshlack/splatter"
	bioc = "splatter" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/splatter_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/splatter/splatter_1.26.0.tar.gz"]

	version("1.26.0", md5="1afec799cae913802068b5b20b32a598")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
