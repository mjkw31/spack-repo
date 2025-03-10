# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyebias(RPackage):
	"""The GASSCO method for correcting for slide-dependent gene-specific dye bias

	Many two-colour hybridizations suffer from a dye bias that is both gene-specific and slide-specific. The former depends on the content of the nucleotide used for labeling; the latter depends on the labeling percentage. The slide-dependency was hitherto not recognized, and made addressing the artefact impossible.  Given a reasonable number of dye-swapped pairs of hybridizations, or of same vs. same hybridizations, both the gene- and slide-biases can be estimated and corrected using the GASSCO method (Margaritis et al., Mol. Sys. Biol. 5:266 (2009), doi:10.1038/msb.2009.21)
	"""
	
	homepage = "http://www.holstegelab.nl/publications/margaritis_lijnzaad"
	bioc = "dyebias" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/dyebias_1.62.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/dyebias/dyebias_1.62.0.tar.gz"]

	version("1.62.0", md5="2b3e10379a29b0cb931514e06fe7259f")

	depends_on("r@1.4.1:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
