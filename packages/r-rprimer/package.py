# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprimer(RPackage):
	"""Design Degenerate Oligos from a Multiple DNA Sequence Alignment

	Functions, workflow, and a Shiny application for visualizing sequence conservation and designing degenerate primers, probes, and (RT)-(q/d)PCR assays from a multiple DNA sequence alignment. The results can be presented in data frame format and visualized as dashboard-like plots. For more information, please see the package vignette.
	"""
	
	homepage = "https://github.com/sofpn/rprimer"
	bioc = "rprimer" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rprimer_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rprimer/rprimer_1.6.0.tar.gz"]

	version("1.6.0", md5="f866266895669cd0e898d1ffb0df86fa")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinyfeedback", type=("build", "run"))
