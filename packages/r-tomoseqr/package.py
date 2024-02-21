# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTomoseqr(RPackage):
	"""R Package for Analyzing Tomo-seq Data

	`tomoseqr` is an R package for analyzing Tomo-seq data. Tomo-seq is a genome-wide RNA tomography method that combines combining high-throughput RNA sequencing with cryosectioning for spatially resolved transcriptomics. `tomoseqr` reconstructs 3D expression patterns from tomo-seq data and visualizes the reconstructed 3D expression patterns.
	"""
	
	bioc = "tomoseqr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/tomoseqr_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/tomoseqr/tomoseqr_1.6.0.tar.gz"]

	version("1.6.0", md5="b881e4b272396cc4696d840658ec0ef5")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
