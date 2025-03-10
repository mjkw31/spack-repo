# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBindingsitefinder(RPackage):
	"""Binding site defintion based on iCLIP data

	Precise knowledge on the binding sites of an RNA-binding protein (RBP) is key to understand (post-) transcriptional regulatory processes. Here we present a workflow that describes how exact binding sites can be defined from iCLIP data. The package provides functions for binding site definition and result visualization. For details please see the vignette.
	"""
	
	bioc = "BindingSiteFinder" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BindingSiteFinder_2.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BindingSiteFinder/BindingSiteFinder_2.0.0.tar.gz"]

	version("2.0.0", md5="b54f11a27c1f6f55b4cc60ad8986e029")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-ggdist", type=("build", "run"))
