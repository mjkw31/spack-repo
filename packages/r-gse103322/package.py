# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGse103322(RPackage):
	"""GEO accession data GSE103322 as a SingleCellExperiment

	Single cell RNA-Seq data for 5902 cells from 18 patients with oral cavity head and neck squamous cell carcinoma available as GEO accession [GSE103322] (http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103322). GSE103322 data have been parsed into a SincleCellExperiment object available in ExperimentHub.
	"""
	
	bioc = "GSE103322" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/GSE103322_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/GSE103322/GSE103322_1.8.0.tar.gz"]

	version("1.8.0", md5="3816b430b716edaaa0ef22dba38cf58e", url="https://www.bioconductor.org/packages/release/data/experiment/src/contrib/GSE103322_1.8.0.tar.gz")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))

	# experiment