# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStructuralvariantannotation(RPackage):
	"""Variant annotations for structural variants

	StructuralVariantAnnotation provides a framework for analysis of structural variants within the Bioconductor ecosystem. This package contains contains useful helper functions for dealing with structural variants in VCF format. The packages contains functions for parsing VCFs from a number of popular callers as well as functions for dealing with breakpoints involving two separate genomic loci encoded as GRanges objects.
	"""
	
	bioc = "StructuralVariantAnnotation" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/StructuralVariantAnnotation_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/StructuralVariantAnnotation/StructuralVariantAnnotation_1.18.0.tar.gz"]

	version("1.18.0", md5="d72d8c88083ed0fc9319afa075360841")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
