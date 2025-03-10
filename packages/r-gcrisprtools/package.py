# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcrisprtools(RPackage):
	"""Suite of Functions for Pooled Crispr Screen QC and Analysis

	Set of tools for evaluating pooled high-throughput screening experiments, typically employing CRISPR/Cas9 or shRNA expression cassettes. Contains methods for interrogating library and cassette behavior within an experiment, identifying differentially abundant cassettes, aggregating signals to identify candidate targets for empirical validation, hypothesis testing, and comprehensive reporting. Version 2.0 extends these applications to include a variety of tools for contextualizing and integrating signals across many experiments, incorporates extended signal enrichment methodologies via the "sparrow" package, and streamlines many formal requirements to aid in interpretablity.
	"""
	
	bioc = "gCrisprTools" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gCrisprTools_2.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gCrisprTools/gCrisprTools_2.8.0.tar.gz"]

	version("2.8.0", md5="113ef693d51de0459865934e9a16d90a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-robustrankaggreg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
