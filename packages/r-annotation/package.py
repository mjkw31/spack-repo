# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotation(RPackage):
	"""Genomic Annotation Resources

	Annotation resources make up a significant proportion of the Bioconductor project. And there are also a diverse set of online resources available which are accessed using specific packages.  This walkthrough will describe the most popular of these resources and give some high level examples on how to use them.
	"""
	
	homepage = "http://bioconductor.org/packages/annotation"
	bioc = "annotation" 
	urls = ["https://www.bioconductor.org/packages/release/workflows/src/contrib/annotation_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/workflows/src/contrib/Archive/annotation/annotation_1.26.0.tar.gz"]

	version("1.26.0", md5="bb13a9e2713ee77e2919b5f8a55f844f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-organism-dplyr", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
	depends_on("r-txdb-mmusculus-ucsc-mm10-ensgene", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-homo-sapiens", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-txdb-athaliana-biomart-plantsmart22", type=("build", "run"))

	# workflow