# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapfabia(RPackage):
	"""hapFabia: Identification of very short segments of identity by descent (IBD) characterized by rare variants in large sequencing data

	A package to identify very short IBD segments in large sequencing data by FABIA biclustering. Two haplotypes are identical by descent (IBD) if they share a segment that both inherited from a common ancestor. Current IBD methods reliably detect long IBD segments because many minor alleles in the segment are concordant between the two haplotypes. However, many cohort studies contain unrelated individuals which share only short IBD segments. This package provides software to identify short IBD segments in sequencing data. Knowledge of short IBD segments are relevant for phasing of genotyping data, association studies, and for population genetics, where they shed light on the evolutionary history of humans. The package supports VCF formats, is based on sparse matrix operations, and provides visualization of haplotype clusters in different formats.
	"""
	
	homepage = "http://www.bioinf.jku.at/software/hapFabia/hapFabia.html"
	bioc = "hapFabia" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/hapFabia_1.44.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/hapFabia/hapFabia_1.44.0.tar.gz"]

	version("1.44.0", md5="a14370aec9e86245541aea68b90c3812")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-fabia@2.3.1:", type=("build", "run"))
