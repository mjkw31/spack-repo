# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidysummarizedexperiment(RPackage):
	"""Brings SummarizedExperiment to the Tidyverse

	The tidySummarizedExperiment package provides a set of tools for creating and manipulating tidy data representations of SummarizedExperiment objects. SummarizedExperiment is a widely used data structure in bioinformatics for storing high-throughput genomic data, such as gene expression or DNA sequencing data. The tidySummarizedExperiment package introduces a tidy framework for working with SummarizedExperiment objects. It allows users to convert their data into a tidy format, where each observation is a row and each variable is a column. This tidy representation simplifies data manipulation, integration with other tidyverse packages, and enables seamless integration with the broader ecosystem of tidy tools for data analysis.
	"""
	
	homepage = "https://github.com/stemangiola/tidySummarizedExperiment"
	bioc = "tidySummarizedExperiment" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/tidySummarizedExperiment_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/tidySummarizedExperiment/tidySummarizedExperiment_1.12.0.tar.gz"]

	version("1.12.0", md5="a7962f90a1d5e582e22a5c6e1f5e46da")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ttservice", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble@3.0.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fansi", type=("build", "run"))
	depends_on("r-pkgconfig", type=("build", "run"))
