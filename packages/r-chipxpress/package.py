# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipxpress(RPackage):
	"""ChIPXpress: enhanced transcription factor target gene identification from ChIP-seq and ChIP-chip data using publicly available gene expression profiles

	ChIPXpress takes as input predicted TF bound genes from ChIPx data and uses a corresponding database of gene expression profiles downloaded from NCBI GEO to rank the TF bound targets in order of which gene is most likely to be functional TF target.
	"""
	
	bioc = "ChIPXpress" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ChIPXpress_1.46.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ChIPXpress/ChIPXpress_1.46.0.tar.gz"]

	version("1.46.0", md5="bed7bbe60d0a51fb667cee9b01e4c407")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-chipxpressdata", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-frma", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-biganalytics", type=("build", "run"))
