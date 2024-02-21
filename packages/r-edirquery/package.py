# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdirquery(RPackage):
	"""Query the EDIR Database For Specific Gene

	EDIRquery provides a tool to search for genes of interest within the Exome Database of Interspersed Repeats (EDIR). A gene name is a required input, and users can additionally specify repeat sequence lengths, minimum and maximum distance between sequences, and whether to allow a 1-bp mismatch. Outputs include a summary of results by repeat length, as well as a dataframe of query results. Example data provided includes a subset of the data for the gene GAA (ENSG00000171298). To query the full database requires providing a path to the downloaded database files as a parameter.
	"""
	
	bioc = "EDIRquery" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/EDIRquery_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/EDIRquery/EDIRquery_1.2.0.tar.gz"]

	version("1.2.0", md5="ff19937af17cf0a7a874b986192d6b1c")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-tibble@3.1.6:", type=("build", "run"))
	depends_on("r-tictoc@1.0.1:", type=("build", "run"))
	depends_on("r-readr@2.1.2:", type=("build", "run"))
	depends_on("r-interactionset@1.22:", type=("build", "run"))
	depends_on("r-genomicranges@1.46.1:", type=("build", "run"))
