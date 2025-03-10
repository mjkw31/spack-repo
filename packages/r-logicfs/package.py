# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogicfs(RPackage):
	"""Identification of SNP Interactions

	Identification of interactions between binary variables using Logic Regression. Can, e.g., be used to find interesting SNP interactions. Contains also a bagging version of logic regression for classification.
	"""
	
	bioc = "logicFS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/logicFS_2.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/logicFS/logicFS_2.22.0.tar.gz"]

	version("2.22.0", md5="af46ee02e89efc5057af01be3f530a4f")

	depends_on("r-logicreg", type=("build", "run"))
	depends_on("r-mcbiopi", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
