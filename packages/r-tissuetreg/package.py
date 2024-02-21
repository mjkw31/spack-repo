# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTissuetreg(RPackage):
	"""TWGBS and RNA-seq data from tissue T regulatory cells from mice

	The package provides ready to use epigenomes (obtained from TWGBS) and transcriptomes (RNA-seq) from various tissues as obtained in the study (Delacher and Imbusch 2017, PMID: 28783152). Regulatory T cells (Treg cells) perform two distinct functions: they maintain self-tolerance, and they support organ homeostasis by differentiating into specialized tissue Treg cells. The underlying dataset characterises the epigenetic and transcriptomic modifications for specialized tissue Treg cells.
	"""
	
	homepage = "https://github.com/cimbusch/tissueTreg"
	bioc = "tissueTreg" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/tissueTreg_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/tissueTreg/tissueTreg_1.22.0.tar.gz"]

	version("1.22.0", md5="5d975c08b7a19af832c4468ecb04c58b")

	depends_on("r@3.5:", type=("build", "run"))

	# experiment