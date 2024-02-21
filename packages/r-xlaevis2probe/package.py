# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXlaevis2probe(RPackage):
	"""Probe sequence data for microarrays of type xlaevis2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was X_laevis_2_probe_tab.
	"""
	
	bioc = "xlaevis2probe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/xlaevis2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/xlaevis2probe/xlaevis2probe_2.18.0.tar.gz"]

	version("2.18.0", md5="d86f8a05e106eb3123435da233ff851d")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation