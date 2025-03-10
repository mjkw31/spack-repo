# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbttest(RPackage):
	"""Multiple Beta t-Tests

	MBttest method was developed from beta t-test method of Baggerly et al(2003). Compared to baySeq (Hard castle and Kelly 2010), DESeq (Anders and Huber 2010) and exact test (Robinson and Smyth 2007, 2008) and the GLM of McCarthy et al(2012), MBttest is of high work efficiency,that is, it has high power, high conservativeness of FDR estimation and high stability. MBttest is suit- able to transcriptomic data, tag data, SAGE data (count data) from small samples or a few replicate libraries. It can be used to identify genes, mRNA isoforms or tags differentially expressed between two conditions.
	"""
	
	bioc = "MBttest" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MBttest_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MBttest/MBttest_1.30.0.tar.gz"]

	version("1.30.0", md5="35c603063456aab63ffa0ebfc67a3c16")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
