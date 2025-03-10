# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnabarcodecompatibility(RPackage):
	"""A Tool for Optimizing Combinations of DNA Barcodes Used in Multiplexed Experiments on Next Generation Sequencing Platforms

	The package allows one to obtain optimised combinations of DNA barcodes to be used for multiplex sequencing. In each barcode combination, barcodes are pooled with respect to Illumina chemistry constraints. Combinations can be filtered to keep those that are robust against substitution and insertion/deletion errors thereby facilitating the demultiplexing step. In addition, the package provides an optimiser function to further favor the selection of barcode combinations with least heterogeneity in barcode usage.
	"""
	
	bioc = "DNABarcodeCompatibility" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DNABarcodeCompatibility_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DNABarcodeCompatibility/DNABarcodeCompatibility_1.18.0.tar.gz"]

	version("1.18.0", md5="b1e2988c254cf089a2f887abf139b7bf")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dnabarcodes", type=("build", "run"))
