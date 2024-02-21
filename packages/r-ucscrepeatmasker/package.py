# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUcscrepeatmasker(RPackage):
	"""UCSC RepeatMasker AnnotationHub resource metadata

	Store UCSC RepeatMasker AnnotationHub resource metadata. Provide provenance and citation information for UCSC RepeatMasker AnnotationHub resources. Illustrate in a vignette how to access those resources.
	"""
	
	bioc = "UCSCRepeatMasker" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/UCSCRepeatMasker_3.15.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/UCSCRepeatMasker/UCSCRepeatMasker_3.15.2.tar.gz"]

	version("3.15.2", md5="ad19a6fbd936e478af88fa21bc918a29")

	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))

	# annotation