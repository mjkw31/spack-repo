# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetagxovarian(RPackage):
	"""Transcriptomic Ovarian Cancer Datasets

	A collection of Ovarian Cancer Transcriptomic Datasets that are part of the MetaGxData package compendium.
	"""
	
	bioc = "MetaGxOvarian" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/MetaGxOvarian_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/MetaGxOvarian/MetaGxOvarian_1.22.0.tar.gz"]

	version("1.22.0", md5="f76dc6c912d3a8936f81509ba6559286")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))

	# experiment