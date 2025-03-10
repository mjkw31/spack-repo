# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqc(RPackage):
	"""RNA-seq data generated from SEQC (MAQC-III) study

	The SEQC/MAQC-III Consortium has produced benchmark RNA-seq data for the assessment of RNA sequencing technologies and data analysis methods (Nat Biotechnol, 2014). Billions of sequence reads have been generated from ten different sequencing sites. This package contains the summarized read count data for ~2000 sequencing libraries. It also includes all the exon-exon junctions discovered from the study. TaqMan RT-PCR data for ~1000 genes and ERCC spike-in sequence data are included in this package as well.
	"""
	
	homepage = "http://bioconductor.org/packages/release/data/experiment/html/seqc.html"
	bioc = "seqc" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/seqc_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/seqc/seqc_1.36.0.tar.gz"]

	version("1.36.0", md5="105a278c97aca90968641aec403c1219")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

	# experiment