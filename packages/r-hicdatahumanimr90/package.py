# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicdatahumanimr90(RPackage):
	"""Human IMR90 Fibroblast HiC data from Dixon et al. 2012

	The HiC data from Human Fibroblast IMR90 cell line (HindIII restriction) was retrieved from the GEO website, accession number GSE35156 (http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE35156). The raw reads were processed as explained in Dixon et al. (Nature 2012).
	"""
	
	bioc = "HiCDataHumanIMR90" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/HiCDataHumanIMR90_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/HiCDataHumanIMR90/HiCDataHumanIMR90_1.22.0.tar.gz"]

	version("1.22.0", md5="02854f68384130b0bcd3d0f84d94b856", url="https://www.bioconductor.org/packages/release/data/experiment/src/contrib/HiCDataHumanIMR90_1.22.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))

	# experiment