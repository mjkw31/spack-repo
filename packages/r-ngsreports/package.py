# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNgsreports(RPackage):
	"""Load FastqQC reports and other NGS related files

	This package provides methods and object classes for parsing FastQC reports and output summaries from other NGS tools into R. As well as parsing files, multiple plotting methods have been implemented for visualising the parsed data. Plots can be generated as static ggplot objects or interactive plotly objects.
	"""
	
	homepage = "https://github.com/smped/ngsReports"
	bioc = "ngsReports" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ngsReports_2.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ngsReports/ngsReports_2.4.0.tar.gz"]

	version("2.4.0", md5="c2d8c1f7a1869275420e05125fb1b420")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-patchwork@1.1.1:", type=("build", "run"))
	depends_on("r-tibble@1.3.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-plotly@4.9.4:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect@0.2.3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
