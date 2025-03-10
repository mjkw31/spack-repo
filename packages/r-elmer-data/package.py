# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElmerData(RPackage):
	"""Data for the ELMER package

	Supporting data for the ELMER package. It includes: - elmer.data.example.promoter: mae.promoter - elmer.data.example: data - EPIC.hg38.manifest - EPIC.hg19.manifest - hm450.hg38.manifest - hm450.hg19.manifest - hocomoco.table - human.TF - LUSC_meth_refined: Meth - LUSC_RNA_refined: GeneExp - Probes.motif.hg19.450K - Probes.motif.hg19.EPIC - Probes.motif.hg38.450K - Probes.motif.hg38.EPIC - TF.family - TF.subfamily - Human_genes__GRCh37_p13 - Human_genes__GRCh38_p12 - Human_genes__GRCh37_p13__tss - Human_genes__GRCh38_p12__tss
	"""
	
	bioc = "ELMER.data" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/ELMER.data_2.26.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/ELMER.data/ELMER.data_2.26.0.tar.gz"]

	version("2.26.0", md5="565ea1aa52f3f61d16b7560859ed7a3a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

	# experiment