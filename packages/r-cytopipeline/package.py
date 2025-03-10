# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytopipeline(RPackage):
	"""Automation and visualization of flow cytometry data analysis pipelines

	This package provides support for automation and visualization of flow cytometry data analysis pipelines. In the current state, the package focuses on the preprocessing and quality control part. The framework is based on two main S4 classes, i.e. CytoPipeline and CytoProcessingStep. The pipeline steps are linked to corresponding R functions - that are either provided in the CytoPipeline package itself, or exported from a third party package, or coded by the user her/himself. The processing steps need to be specified centrally and explicitly using either a json input file or through step by step creation of a CytoPipeline object with dedicated methods. After having run the pipeline, obtained results at all steps can be retrieved and visualized thanks to file caching (the running facility uses a BiocFileCache implementation). The package provides also specific visualization tools like pipeline workflow summary display, and 1D/2D comparison plots of obtained flowFrames at various steps of the pipeline.
	"""
	
	homepage = "https://uclouvain-cbio.github.io/CytoPipeline"
	bioc = "CytoPipeline" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CytoPipeline_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CytoPipeline/CytoPipeline_1.2.0.tar.gz"]

	version("1.2.0", md5="a4ed3b88553c7115d7dce368a0fda5a5")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2@3.4.1:", type=("build", "run"))
	depends_on("r-ggcyto", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-peacoqc", type=("build", "run"))
	depends_on("r-flowai", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
