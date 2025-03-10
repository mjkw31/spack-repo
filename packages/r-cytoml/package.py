# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytoml(RPackage):
	"""A GatingML Interface for Cross Platform Cytometry Data Sharing

	Uses platform-specific implemenations of the GatingML2.0 standard to exchange gated cytometry data with other software platforms.
	"""
	
	homepage = "https://github.com/RGLab/CytoML"
	bioc = "CytoML"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CytoML_2.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CytoML/CytoML_2.14.0.tar.gz"]

	version("2.14.0", md5="4b0060416cdeef7876cb9aaeb81dbaf7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cytolib", type=("build", "run"))
	depends_on("r-flowcore@1.99.10:", type=("build", "run"))
	depends_on("r-flowworkspace", type=("build", "run"))
	depends_on("r-opencyto@1.99.2:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggcyto@1.11.4:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-bh@1.62.0.1:", type=("build", "run"))
	depends_on("r-rprotobuflib", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("libxml2", type=("build", "link", "run"))
