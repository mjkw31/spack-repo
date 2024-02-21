# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3cluster(RPackage):
	"""Cluster Extension for 'mlr3'

	Extends the 'mlr3' package with cluster analysis.
	"""
	
	homepage = "https://mlr3cluster.mlr-org.com"
	cran = "mlr3cluster" 

	version("0.1.8", md5="b590b83bc4b9274f67eb694d161a3e96")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mlr3@0.14:", type=("build", "run"))
	depends_on("r-backports@1.1.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mlr3misc@0.9.4:", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
