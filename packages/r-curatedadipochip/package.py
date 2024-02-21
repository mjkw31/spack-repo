# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedadipochip(RPackage):
	"""A Curated ChIP-Seq Dataset of MDI-induced Differentiated Adipocytes (3T3-L1)

	A curated dataset of publicly available ChIP-sequencing of transcription factors, chromatin remodelers and histone modifications in the 3T3-L1 pre-adipocyte cell line. The package document the data collection, pre-processing and processing of the data. In addition to the documentation, the package contains the scripts that was used to generated the data.
	"""
	
	homepage = "https://github.com/MahShaaban/curatedAdipoChIP"
	bioc = "curatedAdipoChIP" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/curatedAdipoChIP_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/curatedAdipoChIP/curatedAdipoChIP_1.18.0.tar.gz"]

	version("1.18.0", md5="0074cb63250ac197dad12e4138d47463")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

	# experiment